# The Shadow of Extremism

A comprehensive exploration of Islamic extremism through history, ideology, and pathways to reform.

## Project Structure

```
the-shadow-of-extremism/
├── books/              # Book source files (Quarto)
│   ├── *.qmd          # Chapter files (~49k words)
│   └── _quarto.yml    # Book configuration
├── audiobook/          # Audiobook generation (TTS)
│   ├── scripts/       # Python scripts
│   └── requirements.txt
├── tools/              # Utility scripts
│   └── scrape_resources.py  # Download cited web resources
├── references/         # Research notes and sources
└── .github/workflows/  # CI/CD (auto PDF/EPUB/DOCX)
```

## About

This book traces the **Extremism Cycle** - a 7-phase framework showing how extremism emerges, peaks, and collapses across civilizations.

**Stats**: ~49,000 words | ~180-185 pages | 28 chapters

## Quick Start

### Build the Book

```bash
# Install Quarto: https://quarto.org/
quarto render books --to pdf    # or epub, docx
```

Output in `books/_output/`

### Generate Audiobook

```bash
cd audiobook
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Add your ElevenLabs API key to .env
cp ../.env.example ../.env

python scripts/generate_audiobook.py
```

### Scrape Web Resources

```bash
cd tools
pip install -r requirements.txt
python scrape_resources.py
```

## GitHub Actions

Automatically renders PDF/EPUB/DOCX on every push. Download from Actions tab.

## License

© 2025 Algimantas Krasauskas. All rights reserved.
