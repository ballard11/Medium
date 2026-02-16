# Medium Posts

Analysis notebooks and articles for [medium.com/@ben.g.ballard](https://medium.com/@ben.g.ballard).

**Blog:** [bendiagrams.com](https://bendiagrams.com) — Quarto site deployed via GitHub Pages

**40 stories published** | **~43K views** | **$85.44 lifetime earnings** | See [STATS.md](STATS.md) for full analytics.

## Docs

| Doc | Purpose |
|-----|---------|
| [STRATEGY.md](STRATEGY.md) | Growth strategy — franchise model, publishing cadence, distribution plan |
| [STATS.md](STATS.md) | Analytics dashboard — lifetime data, revenue by category. Updated monthly. |
| [SECURITY.md](SECURITY.md) | Public repo security — .gitignore, code hiding, freeze strategy |

## Repo Structure

```
├── bendiagrams-site/         # Quarto blog (bendiagrams.com)
│   ├── sports/               # Sports & Odds posts
│   ├── economics/            # Economics posts
│   ├── code/                 # Code & Labs posts
│   ├── toolbox/              # Quick-reference tool cards
│   └── _templates/           # Post and toolbox templates
├── cfb-data-analysis/        # College football analysis (CFBD API)
├── google-trends/            # Google Trends API analysis
├── sports-betting-odds-api/  # Sports betting with The Odds API
├── archived/                 # Inactive projects and old scripts
└── .github/workflows/        # GitHub Actions (auto-deploy on push)
```

## Active Projects

| Folder | Topic | Published Stories |
|--------|-------|-------------------|
| `cfb-data-analysis/` | College football scoring (CFBD API) | CFB Talent Trends, CFB Recap, Portal P1 & P2 |
| `google-trends/` | Keyword trends (pytrends) | Using Google Trends API, Mastering Google Trends |
| `sports-betting-odds-api/` | Sports betting with The Odds API | Unlocking Sports Betting with Python |

## Publishing Workflow

1. Do analysis in Jupyter notebook → `project-name/analysis.ipynb`
2. Draft article as Quarto post → `bendiagrams-site/bucket/post-slug/index.qmd`
3. Push to `main` → GitHub Actions deploys to [bendiagrams.com](https://bendiagrams.com)
4. Wait 2-3 days for Google indexing
5. Cross-post to Medium with canonical URL pointing to site
6. Syndicate to Dev.to + Hashnode → share on Mastodon

See [STRATEGY.md](STRATEGY.md) for the full cadence and distribution plan.

## Setup

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the repo root with your API keys:
   ```env
   ODDS_API_KEY=your_odds_api_key
   MEDIUM_TOKEN=your_medium_integration_token
   CFBD_API_KEY=your_college_football_data_api_key
   CHART_STUDIO_USERNAME=your_plotly_username
   CHART_STUDIO_API_KEY=your_plotly_api_key
   ```

## Local Development

```bash
cd bendiagrams-site
quarto preview          # Local dev server with auto-refresh
quarto render           # Build to _site/ without serving
```
