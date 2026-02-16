# CLAUDE.md — Project Instructions

## Repo Overview

This repo has two parts:

1. **Article project folders** (root level) — Jupyter notebooks + articles for Medium
   - `cfb-data-analysis/`, `google-trends/`, `sports-betting-odds-api/`, etc.
   - Each folder: notebook + `article.md` + `README.md` + optional `data/` and `images/`

2. **Quarto blog site** (`bendiagrams-site/`) — Static site deployed to GitHub Pages
   - Live at: `https://bendiagrams.com`
   - 4 content buckets: `sports/`, `economics/`, `code/`, `toolbox/`
   - Post structure: `bucket/post-slug/index.qmd` (each post gets its own folder)
   - Templates: `_templates/post-template.qmd`, `_templates/tool-template.qmd`
   - Config: `_quarto.yml`

## Deployment

Push to `main` → GitHub Actions (`.github/workflows/publish.yml`) builds `bendiagrams-site/` → deploys to `gh-pages` branch → live in ~2-3 minutes.

## Key Docs

| Doc | Location | Purpose |
|-----|----------|---------|
| STATS.md | repo root | Medium analytics — lifetime data, revenue by category, what works. Updated monthly. |
| STRATEGY.md | repo root | Growth strategy — franchise model, publishing cadence, distribution |
| SECURITY.md | repo root | Public repo security — .gitignore, code hiding, freeze strategy |
| MIGRATION.md | bendiagrams-site/ | Migrating top Medium articles to the Quarto site |
| GETTING-STARTED.md | bendiagrams-site/ | Quick reference for creating posts and using the site |
| SETUP.md | bendiagrams-site/ | Deployment setup, custom domain, Google Analytics |

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

1. Publish to BenDiagrams site (push to `main`)
2. Wait 2-3 days for Google to index
3. Cross-post to Medium with canonical URL pointing to site
4. Syndicate to Dev.to + Hashnode (canonical URL)
5. Share on Mastodon

See [STRATEGY.md](STRATEGY.md) for the full franchise model and distribution details.
