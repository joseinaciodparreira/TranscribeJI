#!/usr/bin/env python3
"""
Instagram Scanner - Coletor Principal
Camada 1: Ingestão de dados brutos

Coleta perfil, posts, reels, destaques e metadados do Instagram.
Preserva dados brutos para auditoria e reprocessamento.
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext
import yaml


class InstagramCollector:
    """Coletor de dados do Instagram usando Playwright."""
    
    def __init__(self, config_path: str = "config.yaml"):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
        
        self.output_base = Path(self.config.get('output_base', './output'))
        self.cache_dir = Path(self.config.get('cache_dir', './cache'))
        self.auth_mode = self.config.get('auth_mode', 'public')
        self.cookies_file = self.config.get('cookies_file')
        self.timeout = self.config.get('timeout_seconds', 60) * 1000
        
        # Rate limiting
        self.request_delay = self.config.get('request_delay_ms', 2000) / 1000
        self.max_retries = self.config.get('max_retries', 3)
        self.backoff_factor = self.config.get('backoff_factor', 2)
        
        # Configurações de coleta
        self.scroll_delay = self.config.get('scroll_delay_ms', 500) / 1000
        self.screenshot_enabled = self.config.get('screenshot_enabled', True)
        self.html_raw_save = self.config.get('html_raw_save', True)
        
        # Logging
        self.logs: List[Dict] = []
        
    def log(self, level: str, message: str, **kwargs):
        """Registra log estruturado."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "level": level,
            "message": message,
            **kwargs
        }
        self.logs.append(entry)
        print(f"[{level}] {message}")
    
    def _wait_and_retry(self, func, *args, **kwargs):
        """Executa função com retry e backoff exponencial."""
        last_error = None
        for attempt in range(self.max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_error = e
                if attempt < self.max_retries - 1:
                    wait_time = self.backoff_factor ** attempt
                    self.log("WARNING", f"Tentativa {attempt + 1} falhou. Aguardando {wait_time}s...", error=str(e))
                    time.sleep(wait_time)
                else:
                    self.log("ERROR", f"Falha após {self.max_retries} tentativas", error=str(e))
                    raise last_error
        raise last_error
    
    def _setup_context(self, context: BrowserContext):
        """Configura o contexto do navegador."""
        context.set_default_timeout(self.timeout)
        
        # Carrega cookies se estiver em modo autenticado
        if self.auth_mode == 'authenticated' and self.cookies_file:
            cookies_path = Path(self.cookies_file)
            if cookies_path.exists():
                with open(cookies_path, 'r') as f:
                    cookies = json.load(f)
                context.add_cookies(cookies)
                self.log("INFO", "Cookies carregados para autenticação")
    
    def _navigate_to_profile(self, page: Page, username: str):
        """Navega para o perfil do Instagram."""
        url = f"https://www.instagram.com/{username}/"
        self.log("INFO", f"Navegando para {url}")
        
        page.goto(url, wait_until="domcontentloaded")
        time.sleep(2)
        
        # Verifica se a página existe
        if "Página não encontrada" in page.content() or "not found" in page.content().lower():
            raise ValueError(f"Perfil @{username} não encontrado ou é privado")
    
    def _extract_profile_data(self, page: Page) -> Dict[str, Any]:
        """Extrai dados básicos do perfil."""
        self.log("INFO", "Extraindo dados do perfil...")
        
        data = {
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
            "profile_pic_url": None,
            "scraped_at": datetime.now().isoformat()
        }
        
        # Script de extração
        profile_script = """
        () => {
            let data = {
                username: null,
                display_name: null,
                bio_text: null,
                followers: null,
                following: null,
                posts: null,
                external_url: null,
                is_verified: false,
                category: null
            };
            
            // Nome de exibição
            const h1 = document.querySelector('h2');
            if (h1) {
                data.display_name = h1.textContent.trim();
            }
            
            // Bio via meta description
            const metaDesc = document.querySelector('meta[name="description"]');
            if (metaDesc) {
                const desc = metaDesc.getAttribute('content');
                if (desc) {
                    const parts = desc.split('. ');
                    data.bio_text = parts[0];
                }
            }
            
            // Contadores
            const sections = document.querySelectorAll('section');
            sections.forEach(section => {
                const text = section.textContent;
                if (text.includes('seguidores') || text.includes('seguindo') || text.includes('publicações') || text.includes('posts')) {
                    const spans = section.querySelectorAll('span');
                    spans.forEach(span => {
                        const s = span.textContent.trim();
                        if (s.includes('seguidores')) {
                            data.followers = s.replace(/[^0-9.,KMB]/g, '');
                        } else if (s.includes('seguindo')) {
                            data.following = s.replace(/[^0-9.,KMB]/g, '');
                        } else if (s.includes('publicações') || s.includes('posts')) {
                            data.posts = s.replace(/[^0-9.,KMB]/g, '');
                        }
                    });
                }
            });
            
            // Link externo
            const links = document.querySelectorAll('a');
            links.forEach(link => {
                const href = link.getAttribute('href');
                if (href && !href.includes('instagram.com') && href.startsWith('http')) {
                    data.external_url = href;
                }
            });
            
            // Verificação
            const verified = document.querySelector('svg[aria-label="Verificado"], svg[aria-label="Verified"]');
            data.is_verified = !!verified;
            
            return data;
        }
        """
        
        try:
            result = page.evaluate(profile_script)
            data["username"] = result.get('username')
            data["display_name"] = result.get('display_name')
            data["bio_text"] = result.get('bio_text')
            data["followers_count"] = result.get('followers')
            data["following_count"] = result.get('following')
            data["posts_count"] = result.get('posts')
            data["external_url"] = result.get('external_url')
            data["is_verified"] = result.get('is_verified', False)
        except Exception as e:
            self.log("WARNING", f"Erro ao extrair dados via script: {e}")
        
        # Fallback: meta tags
        if not data["display_name"]:
            try:
                og_title = page.query_selector('meta[property="og:title"]')
                if og_title:
                    content = og_title.get_attribute('content')
                    if content:
                        data["display_name"] = content.split(' • ')[0]
            except:
                pass
        
        if not data["bio_text"]:
            try:
                og_desc = page.query_selector('meta[property="og:description"]')
                if og_desc:
                    content = og_desc.get_attribute('content')
                    if content:
                        data["bio_text"] = content.split('.')[0]
            except:
                pass
        
        return data
    
    def _extract_posts(self, page: Page, max_posts: int = 12) -> List[Dict[str, Any]]:
        """Extrai posts recentes do perfil."""
        self.log("INFO", f"Extraindo até {max_posts} posts...")
        
        posts = []
        seen_shortcodes = set()
        
        last_height = page.evaluate("document.body.scrollHeight")
        scroll_attempts = 0
        max_scroll_attempts = max_posts // 3 + 5
        
        while len(posts) < max_posts and scroll_attempts < max_scroll_attempts:
            post_elements = page.query_selector_all('article, div[role="button"][tabindex="0"]')
            
            for element in post_elements[:max_posts * 2]:
                try:
                    shortcode_elem = element.query_selector('a[href*="/p/"], a[href*="/reel/"]')
                    if shortcode_elem:
                        href = shortcode_elem.get_attribute('href')
                        if href:
                            shortcode = href.split('/p/')[-1].split('/reel/')[-1].strip('/')
                            if shortcode and shortcode not in seen_shortcodes:
                                seen_shortcodes.add(shortcode)
                                post_data = self._extract_single_post(page, element, shortcode)
                                if post_data:
                                    posts.append(post_data)
                                    if len(posts) >= max_posts:
                                        break
                except Exception as e:
                    self.log("DEBUG", f"Erro ao extrair post: {e}")
                    continue
            
            if len(posts) >= max_posts:
                break
                
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(self.scroll_delay)
            
            new_height = page.evaluate("document.body.scrollHeight")
            if new_height == last_height:
                scroll_attempts += 1
                if scroll_attempts >= 2:
                    break
            last_height = new_height
            scroll_attempts += 1
        
        self.log("INFO", f"Extraídos {len(posts)} posts")
        return posts
    
    def _extract_single_post(self, page: Page, element, shortcode: str) -> Optional[Dict[str, Any]]:
        """Extrai dados de um único post."""
        try:
            post_data = {
                "shortcode": shortcode,
                "post_id": None,
                "content_type": "image",
                "caption_text": None,
                "published_at": None,
                "likes_count": None,
                "comments_count": None,
                "hashtags": [],
                "mentions": [],
                "thumbnail_url": None,
                "is_pinned": False,
                "scraped_at": datetime.now().isoformat()
            }
            
            img_elem = element.query_selector('img')
            if img_elem:
                alt_text = img_elem.get_attribute('alt')
                if alt_text:
                    post_data["caption_text"] = alt_text
            
            video_elem = element.query_selector('video')
            if video_elem:
                post_data["content_type"] = "video"
            
            reel_badge = element.query_selector('svg[aria-label="Reel"]')
            if reel_badge:
                post_data["content_type"] = "reel"
            
            return post_data
            
        except Exception as e:
            self.log("DEBUG", f"Erro ao extrair post {shortcode}: {e}")
            return None
    
    def _save_raw_data(self, run_dir: Path, profile: Dict, posts: List, html: str, screenshot: bytes = None):
        """Salva dados brutos na camada bronze."""
        bronze_dir = run_dir / "bronze"
        bronze_dir.mkdir(parents=True, exist_ok=True)
        
        if self.html_raw_save:
            html_path = bronze_dir / "raw_profile.html"
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html)
            self.log("INFO", f"HTML salvo em {html_path}")
        
        if screenshot and self.screenshot_enabled:
            screenshot_path = bronze_dir / "profile_screenshot.png"
            with open(screenshot_path, 'wb') as f:
                f.write(screenshot)
            self.log("INFO", f"Screenshot salvo em {screenshot_path}")
        
        profile_path = bronze_dir / "raw_profile.json"
        with open(profile_path, 'w', encoding='utf-8') as f:
            json.dump(profile, f, indent=2, ensure_ascii=False)
        
        posts_path = bronze_dir / "raw_posts.json"
        with open(posts_path, 'w', encoding='utf-8') as f:
            json.dump(posts, f, indent=2, ensure_ascii=False)
        
        metadata = {
            "run_id": run_dir.name,
            "scraped_at": datetime.now().isoformat(),
            "mode": self.auth_mode,
            "posts_collected": len(posts),
            "config_used": {
                "max_posts": len(posts),
                "screenshot": self.screenshot_enabled,
                "html_save": self.html_raw_save
            }
        }
        metadata_path = bronze_dir / "run_metadata.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    def scan(self, username: str, mode: str = "fast") -> Dict[str, Any]:
        """Executa o scan de um perfil."""
        self.log("INFO", f"Iniciando scan de @{username} no modo {mode}")
        
        posts_map = {
            "fast": self.config.get('default_posts_fast', 12),
            "full": self.config.get('default_posts_full', 60),
            "deep": self.config.get('default_posts_deep', 100)
        }
        max_posts = posts_map.get(mode, 12)
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        run_dir = self.output_base / f"{timestamp}_{username}"
        run_dir.mkdir(parents=True, exist_ok=True)
        
        result = {
            "success": False,
            "username": username,
            "mode": mode,
            "run_dir": str(run_dir),
            "profile": None,
            "posts": [],
            "error": None
        }
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                viewport={"width": 1920, "height": 1080},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            
            self._setup_context(context)
            page = context.new_page()
            
            try:
                self._wait_and_retry(self._navigate_to_profile, page, username)
                page.wait_for_load_state("networkidle", timeout=30000)
                time.sleep(2)
                
                profile_data = self._extract_profile_data(page)
                result["profile"] = profile_data
                
                posts_data = self._extract_posts(page, max_posts)
                result["posts"] = posts_data
                
                screenshot = None
                if self.screenshot_enabled:
                    screenshot = page.screenshot(full_page=True)
                
                html_content = page.content()
                self._save_raw_data(run_dir, profile_data, posts_data, html_content, screenshot)
                
                result["success"] = True
                self.log("INFO", f"Scan completado com sucesso: {len(posts_data)} posts coletados")
                
            except Exception as e:
                result["error"] = str(e)
                self.log("ERROR", f"Falha no scan: {e}")
                
                error_log = {
                    "error": str(e),
                    "timestamp": datetime.now().isoformat(),
                    "username": username,
                    "mode": mode
                }
                error_path = run_dir / "error.json"
                with open(error_path, 'w', encoding='utf-8') as f:
                    json.dump(error_log, f, indent=2, ensure_ascii=False)
                
            finally:
                browser.close()
        
        logs_path = run_dir / "scan_logs.json"
        with open(logs_path, 'w', encoding='utf-8') as f:
            json.dump(self.logs, f, indent=2, ensure_ascii=False)
        
        return result


def main():
    parser = argparse.ArgumentParser(description="Instagram Scanner - Coletor de Perfis")
    parser.add_argument("--username", "-u", required=True, help="Username do Instagram (sem @)")
    parser.add_argument("--mode", "-m", default="fast", choices=["fast", "full", "deep"],
                       help="Modo de scan: fast (12 posts), full (60 posts), deep (100+ posts)")
    parser.add_argument("--config", "-c", default="config.yaml", help="Caminho para arquivo de configuração")
    
    args = parser.parse_args()
    
    collector = InstagramCollector(config_path=args.config)
    result = collector.scan(username=args.username, mode=args.mode)
    
    if result["success"]:
        print(f"\n✅ Scan completado!")
        print(f"📁 Diretório: {result['run_dir']}")
        print(f"👤 Perfil: @{result['username']}")
        print(f"📊 Posts coletados: {len(result['posts'])}")
        return 0
    else:
        print(f"\n❌ Scan falhou: {result['error']}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
