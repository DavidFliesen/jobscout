# ◈ Job Scout
### Agentic Intelligence Daily Mission Briefing System

**Job Scout** is an AI-powered job search tool that deploys an intelligent agent each day to scan company career pages, LinkedIn, Indeed, and major job boards for opportunities matching your configured skill profile. Upload your resume and results are scored **0–100** with a plain-English explanation — then exported as TXT, Word, or PDF.

**Live:** [davidfliesen.github.io/jobscout](https://davidfliesen.github.io/jobscout/)

---

## Features

- **Agentic web search** — Claude AI with live web search scans job boards and career pages in real time
- **Resume / document upload** — upload a PDF or TXT resume and Job Scout auto-populates your skills, companies, locations, and preferences in one step
- **Numeric match scoring (0–100)** — with a profile loaded, every lead is scored against your actual qualifications with a breakdown explaining the number
- **HOT / WARM / COLD rating** — 75–100 = apply now, 50–74 = worth a look, 0–49 = stretch role
- **Configurable targets** — set your own companies, skill keywords, locations, and job board sources
- **Search preferences** — toggle filters like Remote Only, Veteran Friendly, No Relocation, and more
- **Job Search Sources** — toggleable list of boards to search; add your own with + ADD
- **Debug panel** — preview the exact prompt sent to the AI, validate your config, and inspect the raw response
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
        |-- POST /parse-resume  (resume upload + AI extraction)
        |-- POST /scout         (agentic job search)
        v
Hugging Face Space  --  FastAPI proxy (app.py)
        |
        v  Anthropic API + web_search tool
Claude Sonnet 4.6 (claude-sonnet-4-6) + Live Web Search
```

The frontend is a single static HTML file hosted on GitHub Pages. The backend is a lightweight FastAPI proxy hosted free on Hugging Face Spaces that holds your Anthropic API key securely and handles two endpoints — resume parsing and job search.

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

### 4. Upload Your Resume (Optional but Recommended)

1. In the **Profile Setup** panel, click **Choose File** and select your resume (PDF or TXT)
2. Click **Analyze & Populate**
3. Claude reads the document and automatically fills in your skills, companies, locations, and preferences
4. Your profile is saved and used to generate numeric match scores on every future mission

---

## Repo Structure

```
jobscout/
├── index.html          # Full frontend — UI, configuration, scoring, export, all JS
├── app.py              # FastAPI backend proxy for Hugging Face Spaces
├── requirements.txt    # fastapi, uvicorn, anthropic
├── Dockerfile          # HF Spaces Docker config (port 7860)
└── README.md           # This file
```

---

## Navigation

The page has a top navigation bar with links to each section:

| Link | Section |
|------|---------|
| PROFILE | Resume upload and profile status |
| SCOUT | Backend config, target companies, skills, locations, sources, preferences, launch |
| SOURCES | Job board source toggles |
| HOW TO | Step-by-step usage guide |
| ABOUT | About Job Scout and the developer |
| PORTFOLIO | External link to developer portfolio |

---

## Configuration Panels

| Panel | Purpose |
|-------|---------|
| **Backend Config** | Paste and save your Hugging Face Space URL |
| **Profile Setup** | Upload resume or career document for auto-population and numeric scoring |
| **Target Companies** | Specific employers to check — add or remove freely |
| **Skill Keywords** | Matched against job descriptions |
| **Locations / Work Mode** | Acceptable work locations (both `City ST` and `City, ST` formats work) |
| **Job Search Sources** | Toggleable job boards — add your own with + ADD |
| **Search Preferences** | Remote Only, Veteran Friendly, No Relocation, travel preference, and more |

---

## Debug Panel

Three buttons above the Launch button provide full transparency into how the tool works:

| Button | What it shows |
|--------|--------------|
| **DEBUG PANEL** | Toggles the debug panel open or closed |
| **PREVIEW PROMPT** | The exact text sent to the AI — verify your companies, skills, and locations are formatted correctly |
| **VALIDATE CONFIG** | Checklist of your full configuration with warnings for potential issues — company name length, missing state abbreviations, backend URL status, profile status |

After a mission runs, the **RAW RESPONSE** tab shows the full JSON returned by the AI.

---

## Scoring System

| Score | Rating | Meaning |
|-------|--------|---------|
| 75–100 | HOT | Strong match — apply now |
| 50–74 | WARM | Good fit — worth a closer look |
| 0–49 | COLD | Partial match — stretch role |

With a resume uploaded, scoring is numeric (0–100) based on:
- Must-have skill matches (up to 15 points each)
- Nice-to-have skill matches (up to 5 points each)
- Location and remote fit (up to 10 points)
- Industry alignment (up to 10 points)

Without a resume, scoring uses qualitative HOT / WARM / COLD only.

---

## Export Options

After each mission, leads can be exported as:

| Format | Contents |
|--------|---------|
| **TXT** | Plain text with all leads, summaries, scores, and three URLs per job |
| **Word .DOCX** | Formatted document with color-coded score badges, skill tags, score breakdown, and live hyperlinks |
| **PDF** | Print-ready page — open in browser and use Print > Save as PDF |

---

## Import / Export Config

All settings save automatically in your browser. To sync to another device:

1. Click **Export Config** — copies a JSON snippet to your clipboard
2. On the other device, click **Import Config** and paste
3. All companies, skills, locations, sources, preferences, and profile data are restored instantly

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, JavaScript (vanilla ES5) |
| Frontend Hosting | GitHub Pages |
| Backend | Python, FastAPI, Uvicorn |
| Backend Hosting | Hugging Face Spaces (Docker, free tier) |
| AI Model | Anthropic Claude Sonnet 4.6 (`claude-sonnet-4-6`) |
| Search | Anthropic web_search tool (live results) |
| Word Export | docx.js 8.5.0 (CDN) |

---

## Notes

- The Hugging Face free tier may take **30–60 seconds to wake up** on the first request of the day — this is normal, the loading animation will wait
- Job Scout uses AI-powered web search — always verify leads directly before applying
- Apply only through official company channels
- Both `City ST` and `City, ST` location formats work — the AI understands both
- Company names like "Newport News Shipbuilding HII" are understood correctly — if no results appear for a specific company it means no current postings were found, not that the name was wrong
- localStorage is per-browser and per-device — use Export / Import Config to sync across devices

---

## Developer

**David Fliesen** — Hybrid AI and Multimedia Developer, Summerville SC

- Portfolio: [davidfliesen.github.io](https://davidfliesen.github.io)
- LinkedIn: [linkedin.com/in/fliesen](https://linkedin.com/in/fliesen/)
- Sisters of Summerville: [sisters-of-summerville.github.io](https://sisters-of-summerville.github.io)

---

*Built with FastAPI · Hugging Face Spaces · Anthropic Claude Sonnet 4.6 · GitHub Pages*
