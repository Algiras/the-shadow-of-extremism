# Utility Tools

## Resource Scraper

Downloads and archives all web resources cited in the book for offline review.

### Setup

```bash
pip install -r requirements.txt
```

### Usage

```bash
python scrape_resources.py
```

This will:
- Extract all URLs from book chapters and reference files
- Download each resource
- Save to `references/downloaded/` with metadata
- Generate a report of success/failures

### Output Structure

```
references/downloaded/
├── example.com_article-title.html
├── example.com_article-title.html.meta.txt
└── ...
```

Metadata files include:
- Original URL
- Download timestamp
- HTTP status code
