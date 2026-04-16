"""
Instagram Profile Scanner - Camada de Ingestão

Coleta dados brutos de perfis do Instagram usando Playwright.
Preserva HTML, screenshots e JSON para auditoria e reprocessamento.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any, List
from playwright.sync_api import sync_playwright, Page, BrowserContext


class InstagramScraper:
    """Scraper de perfis do Instagram com Playwright."""
    
    BASE_URL = "https://www.instagram.com"
    
    def __init__(self, output_dir: str, headless: bool = True):
        self.output_dir = Path(output_dir)
        self.headless = headless
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None
        
    def _create_run_directory(self, username: str) -> Path:
        """Cria estrutura de diretórios para uma execução."""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        run_id = f"{timestamp}_{username}"
        run_dir = self.output_dir / run_id
        
        # Estrutura bronze/silver/gold
        (run_dir / "bronze").mkdir(parents=True, exist_ok=True)
        (run_dir / "silver").mkdir(parents=True, exist_ok=True)
        (run_dir / "gold").mkdir(parents=True, exist_ok=True)
        
        return run_dir
    
    def _save_metadata(self, run_dir: Path, username: str, mode: str):
        """Salva metadados da execução."""
        metadata = {
            "run_id": run_dir.name,
            "username": username,
            "mode": mode,
            "scraped_at": datetime.now().isoformat(),
            "headless": self.headless,
            "base_url": self.BASE_URL
        }
        
        with open(run_dir / "bronze" / "run_metadata.json", "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    def initialize_browser(self):
        """Inicializa o navegador Playwright."""
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=self.headless)
        self.context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        self.page = self.context.new_page()
        
    def close(self):
        """Fecha o navegador."""
        if self.context:
            self.context.browser.close()
    
    def navigate_to_profile(self, username: str) -> bool:
        """Navega para o perfil do Instagram."""
        url = f"{self.BASE_URL}/{username}/"
        
        try:
            self.page.goto(url, wait_until="networkidle", timeout=30000)
            
            # Verifica se a página existe
            if "Página não encontrada" in self.page.content() or self.page.url != url:
                print(f"Perfil @{username} não encontrado ou privado.")
                return False
            
            # Aguarda carregamento do conteúdo principal
            self.page.wait_for_selector("article, main", timeout=10000)
            
            # Scroll para carregar conteúdo lazy-loaded
            self._scroll_page()
            
            return True
            
        except Exception as e:
            print(f"Erro ao navegar para {url}: {e}")
            return False
    
    def _scroll_page(self, scrolls: int = 3):
        """Realiza scroll para carregar conteúdo dinâmico."""
        for i in range(scrolls):
            self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            self.page.wait_for_timeout(1000)
            self.page.evaluate("window.scrollTo(0, 0)")
    
    def extract_profile_data(self) -> Dict[str, Any]:
        """Extrai dados básicos do perfil."""
        profile_data = {
            "username": None,
            "display_name": None,
            "bio_text": None,
            "category": None,
            "followers_count": None,
            "following_count": None,
            "posts_count": None,
            "external_url": None,
            "is_verified": False,
            "is_business": False,
            "profile_pic_url": None
        }
        
        try:
            # Tenta múltiplos seletores para cada campo
            selectors = {
                "username": ["h2._aacl._aacs._aact._aacx._aacy", "span._ap3a._aaco._aacu._aacj"],
                "display_name": ["h1._ap3a._aaco._aacu._aacj"],
                "bio_text": ["span._ap3a._aaco._aacu._aacj"],
                "external_url": ["a._ap36[href]"],
                "followers_count": ["meta[property='og:description']"],
                "posts_count": ["li._acut:first-child span._acut"],
                "following_count": ["li._acut:nth-child(2) span._acut"],
            }
            
            # Username da URL
            profile_data["username"] = self.page.url.strip("/").split("/")[-1]
            
            # Bio
            bio_selector = "span._ap3a._aaco._aacu._aacj"
            bio_elements = self.page.query_selector_all(bio_selector)
            if bio_elements and len(bio_elements) > 0:
                # Pega o segundo elemento (geralmente é a bio)
                for el in bio_elements:
                    text = el.inner_text()
                    if len(text) > 10 and len(text) < 500:
                        profile_data["bio_text"] = text
                        break
            
            # Link externo
            link_el = self.page.query_selector("a._ap36[href]")
            if link_el:
                profile_data["external_url"] = link_el.get_attribute("href")
            
            # Contadores via meta description
            meta_desc = self.page.query_selector("meta[property='og:description']")
            if meta_desc:
                content = meta_desc.get_attribute("content")
                if content:
                    # Extrai números do texto
                    import re
                    numbers = re.findall(r'\d+[.,]?\d*', content)
                    if numbers:
                        profile_data["followers_display"] = content
            
            # Verificação
            verified_badge = self.page.query_selector("svg[aria-label='Verificado']")
            profile_data["is_verified"] = verified_badge is not None
            
        except Exception as e:
            print(f"Erro ao extrair dados do perfil: {e}")
        
        return profile_data
    
    def extract_posts(self, limit: int = 12) -> List[Dict[str, Any]]:
        """Extrai dados dos posts recentes."""
        posts = []
        
        try:
            # Seleciona artigos (posts)
            articles = self.page.query_selector_all("article")
            
            for i, article in enumerate(articles[:limit]):
                post_data = {
                    "index": i,
                    "shortcode": None,
                    "content_type": "image",  # image, video, reel, carousel
                    "caption_text": None,
                    "likes_count": None,
                    "comments_count": None,
                    "published_at": None,
                    "hashtags": [],
                    "mentions": [],
                    "thumbnail_path": None
                }
                
                # Link do post
                link_el = article.query_selector("a[href*='/p/'], a[href*='/reel/']")
                if link_el:
                    href = link_el.get_attribute("href")
                    if href:
                        post_data["shortcode"] = href.strip("/").split("/")[-1]
                        if "/reel/" in href:
                            post_data["content_type"] = "reel"
                        elif "/video/" in href:
                            post_data["content_type"] = "video"
                
                # Legenda
                caption_el = article.query_selector("span._ap3a._aaco._aacu._aacj")
                if caption_el:
                    caption = caption_el.inner_text()
                    post_data["caption_text"] = caption
                    
                    # Extrai hashtags
                    import re
                    hashtags = re.findall(r'#\w+', caption)
                    post_data["hashtags"] = hashtags
                    
                    # Extrai menções
                    mentions = re.findall(r'@\w+', caption)
                    post_data["mentions"] = mentions
                
                # Curtidas e comentários (pode exigir clique)
                likes_el = article.query_selector("span._aano")
                if likes_el:
                    likes_text = likes_el.inner_text()
                    post_data["likes_display"] = likes_text
                
                posts.append(post_data)
            
        except Exception as e:
            print(f"Erro ao extrair posts: {e}")
        
        return posts
    
    def take_screenshot(self, run_dir: Path, username: str):
        """Tira screenshot do perfil."""
        try:
            screenshot_path = run_dir / "bronze" / "profile_screenshot.png"
            self.page.screenshot(path=str(screenshot_path), full_page=True)
            print(f"Screenshot salvo em: {screenshot_path}")
        except Exception as e:
            print(f"Erro ao tirar screenshot: {e}")
    
    def save_raw_html(self, run_dir: Path, username: str):
        """Salva o HTML bruto da página."""
        try:
            html_path = run_dir / "bronze" / "raw_profile.html"
            html_content = self.page.content()
            
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            
            print(f"HTML bruto salvo em: {html_path}")
        except Exception as e:
            print(f"Erro ao salvar HTML: {e}")
    
    def scan(self, username: str, mode: str = "fast") -> Dict[str, Any]:
        """
        Executa o scan completo do perfil.
        
        Args:
            username: Username do Instagram (sem @)
            mode: "fast" (12 posts) ou "full" (60 posts)
        
        Returns:
            Dicionário com dados coletados e caminho da execução
        """
        print(f"\n{'='*60}")
        print(f"INICIANDO SCAN: @{username}")
        print(f"Modo: {mode}")
        print(f"{'='*60}\n")
        
        # Cria diretório da execução
        run_dir = self._create_run_directory(username)
        self._save_metadata(run_dir, username, mode)
        
        # Inicializa navegador
        self.initialize_browser()
        
        try:
            # Navega para o perfil
            if not self.navigate_to_profile(username):
                return {"success": False, "error": "Perfil não encontrado", "run_dir": str(run_dir)}
            
            # Salva HTML bruto e screenshot
            self.save_raw_html(run_dir, username)
            self.take_screenshot(run_dir, username)
            
            # Extrai dados do perfil
            profile_data = self.extract_profile_data()
            
            # Define limite de posts
            post_limit = 12 if mode == "fast" else 60
            
            # Extrai posts
            posts_data = self.extract_posts(limit=post_limit)
            
            # Salva dados brutos em JSON
            raw_data = {
                "profile": profile_data,
                "posts": posts_data,
                "scraped_at": datetime.now().isoformat()
            }
            
            with open(run_dir / "bronze" / "raw_profile.json", "w", encoding="utf-8") as f:
                json.dump(raw_data, f, indent=2, ensure_ascii=False)
            
            print(f"\nDados brutos salvos em: {run_dir / 'bronze'}")
            print(f"Posts coletados: {len(posts_data)}")
            
            return {
                "success": True,
                "run_dir": str(run_dir),
                "run_id": run_dir.name,
                "profile": profile_data,
                "posts": posts_data,
                "post_count": len(posts_data)
            }
            
        finally:
            self.close()


def main():
    parser = argparse.ArgumentParser(description="Scanner de perfis do Instagram")
    parser.add_argument("--username", required=True, help="Username do Instagram (sem @)")
    parser.add_argument("--mode", choices=["fast", "full"], default="fast", 
                       help="Modo de scan: fast (12 posts) ou full (60 posts)")
    parser.add_argument("--output-dir", default="./runs", help="Diretório de saída")
    parser.add_argument("--headless", action="store_true", default=True,
                       help="Executar navegador em modo headless")
    
    args = parser.parse_args()
    
    # Cria scraper e executa scan
    scraper = InstagramScraper(output_dir=args.output_dir, headless=args.headless)
    result = scraper.scan(username=args.username, mode=args.mode)
    
    if result["success"]:
        print(f"\n✅ Scan concluído com sucesso!")
        print(f"Run ID: {result['run_id']}")
        print(f"Diretório: {result['run_dir']}")
        return 0
    else:
        print(f"\n❌ Erro no scan: {result.get('error', 'Desconhecido')}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
