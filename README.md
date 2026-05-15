# ◈ Job Scout
### Agentic Intelligence Daily Mission Briefing System

**Job Scout** is an AI-powered job search tool that deploys an intelligent agent each day to scan company career pages, LinkedIn, Indeed, and major job boards for opportunities matching your configured skill profile. Results are scored **HOT**, **WARM**, or **COLD** with a plain-English explanation of why each role fits — then exported as TXT, Word, or PDF.

**Live:** [davidfliesen.github.io/jobscout](https://davidfliesen.github.io/jobscout/)

---

## Features

- **Agentic web search** — Claude AI with live web search scans job boards and career pages in real time
- **Configurable targets** — set your own companies, skill keywords, locations, and job board sources
- **HOT / WARM / COLD scoring** — every lead ranked by fit with a plain-English explanation
- **Search preferences** — toggle filters like Remote Only, Veteran Friendly, No Relocation, and more
- **Export briefings** — save results as TXT, Word .DOCX (with live hyperlinks), or print-ready PDF
- **Persistent settings** — all configuration saves to localStorage and persists between sessions
- **Import / Export config** — transfer your full configuration to another device via JSON snippet
- **No login required** — runs entirely in the browser once the backend is configured

---

## Architecture

```
Browser (GitHub Pages)
        |
        v
Job Scout frontend  --  index.html
        |
        v  fetch /scout
Hugging Face Space  --  FastAPI proxy (app.py)
        |
        v  Anthropic API + web_search tool
Claude Sonnet + Live Web Search
```

The frontend is a single static HTML file hosted on GitHub Pages. The backend is a lightweight FastAPI proxy hosted free on Hugging Face Spaces that holds your Anthropic API key securely and relays requests to the Claude API with web search enabled.

---

## Setup

### 1. Backend — Hugging Face Spaces

Create a new Space at [huggingface.co](https://huggingface.co):

- **SDK:** Docker
- **Visibility:** Public

Upload these three files to the Space:

| File | Purpose |
|------|---------|
| `app.py` | FastAPI proxy server |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Container config (port 7860) |

Then go to **Settings > Variables and Secrets > New Secret** and add:

| Key | Value |
|-----|-------|
| `ANTHROPIC_API_KEY` | Your Anthropic API key from [console.anthropic.com](https://console.anthropic.com) |

Your permanent backend URL will be:
```
https://YOUR-HF-USERNAME-YOUR-SPACE-NAME.hf.space
```

### 2. Frontend — GitHub Pages

Fork or clone this repo. Enable GitHub Pages under **Settings > Pages > Deploy from branch > main / root**.

Your Job Scout will be live at:
```
https://YOUR-GITHUB-USERNAME.github.io/jobscout/
```

### 3. Connect Backend to Frontend (One Time Only)

1. Open your Job Scout page in a browser
2. Paste your Hugging Face Space URL into the **Backend Config** panel
3. Click **Save URL** then **Test** to confirm the connection
4. The URL is saved to localStorage and remembered on every future visit

---

## Repo Structure

```
jobscout/
├── index.html          # Full frontend — UI, configuration, export, all JS
├── app.py              # FastAPI backend proxy for Hugging Face Spaces
├── requirements.txt    # fastapi, uvicorn, anthropic
├── Dockerfile          # HF Spaces Docker config
└── README.md           # This file
```

---

## Configuration

All settings are saved in your browser automatically. Use the panels on the page to configure:

- **Target Companies** — specific employers to check
- **Skill Keywords** — matched against job descriptions
- **Locations / Work Mode** — acceptable work locations
- **Job Search Sources** — job boards and career sites to search (toggleable, add your own with + ADD)
- **Search Preferences** — Remote Only, Veteran Friendly, No Relocation, travel preference, and more

To copy your configuration to another device, use **Export Config** (copies JSON to clipboard) and **Import Config** (paste to restore).

---

## Export Options

After each mission, leads can be exported as:

| Format | Contents |
|--------|---------|
| **TXT** | Plain text with all leads, summaries, and three URLs per job |
| **Word .DOCX** | Formatted document with color-coded badges, skill tags, and live hyperlinks |
| **PDF** | Print-ready page — open in browser and use Print > Save as PDF |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, JavaScript (vanilla ES5) |
| Frontend Hosting | GitHub Pages |
| Backend | Python, FastAPI, Uvicorn |
| Backend Hosting | Hugging Face Spaces (Docker, free tier) |
| AI Model | Anthropic Claude Sonnet (claude-sonnet-4-20250514) |
| Search | Anthropic web_search tool (live results) |
| Word Export | docx.js 8.5.0 (CDN) |

---

## Notes

- The Hugging Face free tier may take **30-60 seconds to wake up** on the first request of the day
- Job Scout uses AI-powered web search — always verify leads directly before applying
- Apply only through official company channels
- localStorage is per-browser and per-device — use Export/Import Config to sync across devices

---

## Developer

**David Fliesen** — Hybrid AI and Multimedia Developer, Summerville SC

- Portfolio: [davidfliesen.github.io](https://davidfliesen.github.io)
- LinkedIn: [linkedin.com/in/fliesen](https://linkedin.com/in/fliesen/)
- Sisters of Summerville: [sisters-of-summerville.github.io](https://sisters-of-summerville.github.io)

---

*Built with FastAPI · Hugging Face Spaces · Anthropic Claude · GitHub Pages*
