# CLAUDE.md — Project Instructions

## Repo Overview

The repo root is the Quarto project. Two clear zones:

1. **`posts/`** — Published blog posts (`.qmd` files, source of truth)
   - One folder per post: `posts/post-slug/index.qmd`
   - Uses `categories:` YAML front matter (e.g. `[sports]`, `[economics]`) — no category subfolders

2. **`toolbox/`** — Reference pages (`.qmd`), separate from posts

3. **`analysis/`** — Scratch exploration only. Not part of the site.
   - `analysis/cfb-data-analysis/`, `analysis/google-trends/`, etc.
   - `*.ipynb` files here are gitignored

4. **Site config at root:** `_quarto.yml`, `index.qmd`, `about.qmd`, `_templates/`

## Deployment

Push to `main` → GitHub Actions (`.github/workflows/publish.yml`) runs `quarto render` at repo root → deploys `_site/` to `gh-pages` branch → live at `https://bendiagrams.com` in ~2-3 minutes.

## Key Docs

| Doc | Purpose |
|-----|---------|
| STATS.md | Medium analytics — lifetime data, revenue by category, what works. Updated monthly. |
| MIGRATION.md | Active checklist for migrating remaining Medium articles to the site. Delete when done. |

## File Authority & Agent Scope

- **Single source of truth:** All `.qmd` files are the authoritative source for blog content, narrative, and finalized code.
- **Agent scope:** Only read, write, and modify `.qmd` files. Do not interact with, parse, or generate `.ipynb` files.
- **Human sandbox:** The user uses `.ipynb` files as temporary scratchpads for interactive exploration. These are not tracked in version control.
- **Concurrency rule:** Do not modify a `.qmd` file if the user says they are actively working in its `.ipynb` counterpart. Wait for the user to manually sync their code back to the `.qmd` before resuming edits.

## Writing Style

**Core formula:** Show code → Show output → Explain in plain English

- Conversational tone: "Let's take a look", "So what data did we really get?"
- First-person, active voice: "I'll show you how to..."
- Show nested code inline (don't abstract into helper functions)
- Hardcoded examples with real IDs and dates
- Display outputs immediately after every operation
- Progressive complexity — each block builds on previous
- Target length: 6-8 minutes (sweet spot per STATS.md analysis)
- No academic/formal tone. No theory before code.

## Security — Critical

- **Never commit API keys.** Use placeholders: `API_KEY = 'YOUR_API_KEY'`
- **`.env` at repo root** (gitignored) stores all secrets
- **API keys in `.env`:** ODDS_API_KEY, MEDIUM_TOKEN, CFBD_API_KEY, CHART_STUDIO_USERNAME, CHART_STUDIO_API_KEY
- Use `#| echo: false` in Quarto to hide proprietary code
- Use `execute: freeze: true` for posts with sensitive analysis
- See SECURITY.md for full details

## User Preferences

- No public GitHub issues on the site (repo-actions removed from _quarto.yml)
- Newsletter is deferred — no signup forms yet
- Keep things simple — no over-engineering
- Custom domain: `bendiagrams.com` (live, configured in `_quarto.yml` and `CNAME`)
- Google Analytics: active (`G-7SD1391XRV`)
- Author: Ben Ballard — medium.com/@ben.g.ballard
- Social: [GitHub](https://github.com/ballard11) | [LinkedIn](https://www.linkedin.com/in/ben-ballard-44969313/) | [Medium](https://medium.com/@ben.g.ballard)

## Publishing Workflow

**Goal:** 2x/week (Tuesday anchor + Friday update), ~75 min per article

### Weekly Cadence

| Day | Task |
|-----|------|
| **Mon** | Pick topic → AI drafts notebook |
| **Tue** | Review notebook (30 min) → Publish **Anchor** post (deep tutorial) |
| **Wed** | AI drafts Friday's lighter piece from the same analysis |
| **Thu** | Review article draft (20 min) |
| **Fri** | Publish **Update** post (results, tips, quick wins) → Final review (10 min) |

### Distribution (after each publish)

1. Push to `main` → live on BenDiagrams
2. Wait 2-3 days for Google to index
3. Cross-post to Medium — import from URL, set canonical to site
4. Syndicate: [Dev.to/@ben_ballard_11](https://dev.to/ben_ballard_11) + [Hashnode/@BenBallard](https://hashnode.com/@BenBallard) (canonical URL)
5. Share on [Mastodon/@benballrd11](https://mastodon.social/@benballrd11)

### Creating a Post

```bash
mkdir -p posts/my-post-slug
cp _templates/post-template.qmd posts/my-post-slug/index.qmd
```

Key YAML fields: `title`, `description`, `date`, `categories: [sports]`, `image`, `draft: false`

```bash
quarto preview       # local dev server
git push origin main # deploy
```
