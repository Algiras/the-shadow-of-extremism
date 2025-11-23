# Audiobook Generation

Scripts to convert the book to audiobook format using ElevenLabs TTS.

## Setup

```bash
# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate  # On Mac/Linux
# .venv\Scripts\activate   # On Windows

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` from the root directory and add your ElevenLabs API key:

```bash
cp ../.env.example ../.env
# Edit .env and add your ELEVENLABS_API_KEY
```

## Usage

```bash
python scripts/generate_audiobook.py
```

Output will be in `output/` (excluded from git).
