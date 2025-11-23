# The Shadow of Extremism

A comprehensive exploration of Islamic extremism through history, ideology, and pathways to reform.

## Project Structure

```
bookie/
├── books/              # Book source files (Quarto)
│   ├── *.qmd          # Chapter files
│   └── _quarto.yml    # Book configuration
├── audiobook/          # Audiobook generation
│   └── scripts/       # Python scripts for TTS
├── api/                # Optional API for book data
│   └── main.py        # FastAPI server
├── references/         # Research notes and sources
└── .github/           # CI/CD workflows
```

## About

This book traces the **Extremism Cycle** - a 7-phase framework showing how extremism emerges, peaks, and collapses across civilizations.

**Current Status**: ~49,000 words / ~180-185 pages

## Building the Book

### Prerequisites
- [Quarto](https://quarto.org/) (latest version)
- LaTeX distribution (TinyTeX recommended)

### Local Rendering

```bash
# PDF
quarto render books --to pdf

# EPUB
quarto render books --to epub

# DOCX
quarto render books --to docx
```

Outputs will be in `books/_output/` (excluded from git)

### Automated Builds

GitHub Actions automatically renders all formats on every push to `main`. Artifacts are available in the Actions tab.

## Audiobook Generation

```bash
cd audiobook
python scripts/generate_audiobook.py
```

Requires ElevenLabs API key in `.env` file.

## License

© 2025 Algimantas Krasauskas. All rights reserved.
