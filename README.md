<div align="center">
  <img src="books/cover.png" alt="The Shadow of Extremism Book Cover" width="400"/>
</div>

# The Shadow of Extremism

**A Journey Through History, Ideology, and the Path to Reform**

[![Book Status](https://img.shields.io/badge/status-publication%20ready-green)](https://github.com/Algiras/the-shadow-of-extremism)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![AI: Gemini 3.0](https://img.shields.io/badge/AI-Gemini%203.0-blue)](https://deepmind.google/technologies/gemini/)

---

## 📖 About This Project

**"The Shadow of Extremism"** is an **experimental AI-generated book** exploring how extremist movements emerge, sustain themselves, and collapse across cultures—from ISIS to the Inquisition, from Buddhist nationalism to secular revolutionary terror.

**What This Actually Is:**
This book was created as a **2-day experiment** to test the capabilities of modern Large Language Models (LLMs) in synthesizing complex historical, theological, and sociological analysis. It demonstrates what AI systems can produce when given proper guidance, curated inputs, and human oversight—in just 48 hours.

**The Experiment:**
- **Timeline**: Created in just **2 days**, not years or even months of traditional research
- **Method**: AI-driven research, synthesis, and drafting with human guidance and verification
- **Goal**: Explore the boundaries of AI-generated scholarly content at unprecedented speed
- **Result**: A comprehensive 200-page analysis identifying **5 Universal Dynamics** of extremism
- **The Tools**: Google Gemini 3.0 (Experimental Thinking Mode) + Anthropic Claude working in tandem

**Read Online**: [algiras.github.io/the-shadow-of-extremism](https://algiras.github.io/the-shadow-of-extremism/)

---

## 🔍 Feedback Welcome

**I'm particularly interested in feedback on:**

- **Factual accuracy** - Are the historical claims correct? Theological interpretations sound?
- **AI limitations** - Where does the AI-generated analysis fall short?
- **Source quality** - Are the AI-curated sources appropriate and credible?
- **Logical coherence** - Does the 5 Dynamics framework hold up under scrutiny?
- **Bias detection** - What perspectives or voices are missing?

### How to Contribute

1. **Read the book** online or download the [PDF/EPUB](https://github.com/Algiras/the-shadow-of-extremism/releases)
2. **Submit feedback** via:
   - GitHub Issues: [Report errors or suggest improvements](https://github.com/Algiras/the-shadow-of-extremism/issues)
   - GitHub Discussions: [Discuss AI-generated content quality](https://github.com/Algiras/the-shadow-of-extremism/discussions)
   - Email: [Contact the author](https://github.com/Algiras)

This is an **experiment in AI-augmented research**. Your critique helps us understand both the potential and limitations of this approach.

---

## 🤖 The AI Experiment: How This Was Made

This book is a **proof-of-concept** demonstrating what modern LLMs can create when properly guided—using entirely **free tools**.

### The Primary Tool: Google Antigravity

This entire book was created using **Google Antigravity**, Google's new AI coding assistant (free tier), powered by **Gemini 3.0 in Experimental Thinking Mode**. No subscriptions, no research grants, no institutional access—just free tokens and **2 days**.

### What AI Did
- **Research**: Analyzed primary sources in classical Arabic, Ottoman Turkish, and Latin
- **Synthesis**: Identified structural patterns across 7 different religious/ideological movements
- **Drafting**: Generated initial content based on scholarly frameworks
- **Visuals**: Created infographics and diagrams

### What the Human Did
- **Guided**: Provided prompts, frameworks, and intellectual direction
- **Curated**: Selected sources and verified claims against established scholarship
- **Reviewed**: Edited for coherence, accuracy, and to remove AI hallucinations
- **Accepted responsibility**: All errors, interpretations, and conclusions are mine

### Limitations to Acknowledge
- **Not traditional scholarship**: This wasn't researched over years in archives
- **AI-curated sources**: While verified, the breadth may not match human expertise
- **Verification challenges**: Some claims may reflect AI synthesis rather than scholarly consensus
- **Experimental**: This is testing what's possible, not claiming definitive answers

### How to Replicate This Methodology

Want to try this yourself? Here's the workflow:

1. **Open Antigravity** (free tier): Start conversational research sessions
2. **Prompt strategically**: E.g., "Analyze [source] using [framework], cite primary texts"
3. **Iterate through conversation**: Refine outputs through follow-up questions
4. **Verify relentlessly**: Cross-check AI claims against established sources
5. **Curate ruthlessly**: Keep what's good, discard hallucinations, edit for clarity
6. **Assemble and refine**: Compile into coherent structure with human insight

**Time investment**: Just **2 days** for a 200-page comparative analysis

**The Value**: This demonstrates how AI can democratize complex research and make sophisticated analysis accessible—at zero cost and unprecedented speed. The combination of Gemini 3.0 (with Experimental Thinking Mode) and Claude is *that powerful*. Anyone with internet access can now attempt similar synthesis.
---

## 🏗️ Project Structure

```
bookie/
├── pyproject.toml        # Python project configuration (dependencies, scripts)
├── Makefile              # Task runner for common operations
├── scripts/              # Utility scripts (lint checking, validation)
├── audiobook/            # Audiobook generation tools
├── tools/                # Additional utilities
├── books/                # Book content (Quarto markdown)
│   ├── index.qmd         # Introduction
│   ├── 01-20.qmd         # Main chapters
│   ├── 21-25.qmd         # Appendices and back matter
│   └── _quarto.yml       # Book configuration
└── .github/workflows/    # CI/CD (automatic builds)
```

---

## 🛠️ Building Locally

### Prerequisites
- [Quarto](https://quarto.org/docs/get-started/) (latest version)
- [TeX Live](https://www.tug.org/texlive/) (for PDF)
- Amiri font (for Arabic text rendering)
- Python 3.8+ (for utility scripts)

### Quick Start

```bash
# Install Python dependencies and scripts
make install

# Run content validation
make lint-check    # Check markdown formatting
make scan-chars    # Scan for invalid characters

# Render the book
cd books
quarto render --to html    # Generate HTML version
quarto render --to pdf     # Generate PDF version
quarto render --to epub    # Generate EPUB version

# Serve locally with live reload
quarto preview books
```

### Available Make Commands

```bash
make help          # Show all available commands
make install       # Install project in development mode
make lint-check    # Validate markdown formatting
make scan-chars    # Scan for invalid characters in content
make clean         # Remove build artifacts
```

### Using Python Scripts Directly

After running `make install`, scripts are available as commands:

```bash
lint-check         # Check markdown formatting in books/
scan-chars         # Scan for invalid characters
```

---

## 📜 License

**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**

You are free to:
- **Share** — copy and redistribute the material
- **Adapt** — remix, transform, and build upon the material

Under the following terms:
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made
- **NonCommercial** — You may not use the material for commercial purposes without permission
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license

[Full License Text](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

## 🙏 Acknowledgements

See [Acknowledgements](https://algiras.github.io/the-shadow-of-extremism/acknowledgements.html) for the full list of contributors.

Special thanks to my wife, a fierce defender of free speech, and my mother, a historian whose methodology shaped this work.

---

## 💬 Contact & Support

- **GitHub**: [Algiras](https://github.com/Algiras)
- **LinkedIn**: [Algimantas Krasauskas](https://www.linkedin.com/in/asimplek/)
- **Support**: [Buy me a coffee](https://buymeacoffee.com/algiras) to fund audiobook production

---

**Note**: This is a living document. All feedback, corrections, and suggestions are welcome as we work toward a final published version.
