#!/usr/bin/env python3
"""
Resource Scraper for The Shadow of Extremism
Downloads and archives web resources cited in the book for offline review.
"""

import os
import re
import requests
from pathlib import Path
from urllib.parse import urlparse
from datetime import datetime

# Configuration
REFERENCES_DIR = Path("references/downloaded")
REFERENCES_DIR.mkdir(parents=True, exist_ok=True)

def extract_urls_from_markdown(file_path):
    """Extract all URLs from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match markdown links [text](url) and plain URLs
    url_pattern = r'https?://[^\s\)>]+'
    urls = re.findall(url_pattern, content)
    return list(set(urls))  # Remove duplicates

def sanitize_filename(url):
    """Create a safe filename from URL."""
    parsed = urlparse(url)
    domain = parsed.netloc.replace('www.', '')
    path = parsed.path.strip('/').replace('/', '_')
    return f"{domain}_{path or 'index'}.html"

def download_url(url, output_dir):
    """Download a URL and save it locally."""
    try:
        response = requests.get(url, timeout=10, headers={
            'User-Agent': 'Mozilla/5.0 (Research purposes)'
        })
        response.raise_for_status()
        
        filename = sanitize_filename(url)
        output_path = output_dir / filename
        
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        # Save metadata
        meta_path = output_dir / f"{filename}.meta.txt"
        with open(meta_path, 'w') as f:
            f.write(f"URL: {url}\n")
            f.write(f"Downloaded: {datetime.now().isoformat()}\n")
            f.write(f"Status: {response.status_code}\n")
        
        print(f"✓ Downloaded: {url}")
        return True
    except Exception as e:
        print(f"✗ Failed: {url} - {str(e)}")
        return False

def main():
    """Main function to scrape all references."""
    # Find all markdown files in the project
    markdown_files = list(Path("books").glob("*.qmd")) + \
                    list(Path("references").glob("**/*.md"))
    
    all_urls = []
    for file_path in markdown_files:
        urls = extract_urls_from_markdown(file_path)
        all_urls.extend(urls)
    
    all_urls = list(set(all_urls))  # Remove duplicates
    
    print(f"\nFound {len(all_urls)} unique URLs to download\n")
    
    # Download each URL
    success = 0
    for url in all_urls:
        if download_url(url, REFERENCES_DIR):
            success += 1
    
    print(f"\n{'='*60}")
    print(f"Downloaded {success}/{len(all_urls)} resources")
    print(f"Saved to: {REFERENCES_DIR.absolute()}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
