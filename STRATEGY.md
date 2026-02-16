# Medium Growth Strategy

**Goal:** Scale from ~$2.50/month to $250/month on Medium Partner Program
**Author:** Ben Ballard — [medium.com/@ben.g.ballard](https://medium.com/@ben.g.ballard)
**Date:** February 2026
**Data backing:** [STATS.md](STATS.md) — updated monthly from [medium.com/me/stats](https://medium.com/me/stats?publishedAt=DESC)

---

## The Core Insight

The top-performing story is **"Unlocking Sports Betting with Python"** (Dec 16, 2023). Everything in this strategy builds outward from that proven winner.

The numbers behind this *(from [STATS.md](STATS.md))*:
- 5 stories = 80.3% of all revenue ($68.62 / $85.44)
- All 5 are "How to [API] with Python" tutorials
- Sports Betting category: **$12.21/story** vs. $2.14 overall average
- Short player profiles: **$0.08/story** — a 150x difference
- Optimal length: **6–8 minutes** ($6.82 avg earnings vs. $1.29 for 2–3 min)

---

## Strategy 1: The "Franchise" (Don't Reinvent the Wheel)

You found a winner. Instead of writing about random data science topics, build a franchise around this specific success.

**Why it works:** You already have authority here. Google trusts you on "Odds API Python."

**The Play:** Write sequels, not standalone posts.

| # | Sequel Idea |
|---|-------------|
| 1 | "Building a Streamlit App for Live Odds (Part 2 of the Betting Series)" |
| 2 | "Backtesting my Dec 2023 Betting Strategy: Did I make money?" |
| 3 | "Moving from The Odds API to the NFL: A Python Guide" |

**Key Rule:** Link every new story back to the original hit. This creates a "reading loop" that multiplies earnings.

---

## Strategy 2: Distribution — Syndication vs. Prestige

Every article falls into one of two distribution tracks.

### Category A: Syndication (Automated Reposting)

These platforms support **canonical URLs**, so Google knows Medium is the original. Script these alongside your Medium publish.

| Platform | Handle | Why |
|----------|--------|-----|
| **Dev.to** | [@ben_ballard_11](https://dev.to/ben_ballard_11) | Huge developer audience, very API-friendly |
| **Hashnode** | [@BenBallard](https://hashnode.com/@BenBallard) | Slightly more senior vibe, supports canonical URLs |
| **Mastodon** | [@benballrd11](https://mastodon.social/@benballrd11) | Share links + short summaries for each post |

**Routine flow:** Publish to BenDiagrams site → cross-post to Medium (canonical URL to site) → syndicate to Dev.to + Hashnode (canonical URL) → share on Mastodon.

### Category B: Prestige Targets (Resume Builders)

You cannot auto-post here. You **pitch** these. Reserve for quarterly "big" projects (NBA bot results, crime data analysis, etc.).

| Target | Why | Pitch Style |
|--------|-----|-------------|
| **Towards Data Science** (Medium pub) | 600k+ followers, you're already on Medium — submit drafts here instead of self-publishing | Standard Medium draft submission |
| **Level Up Coding** / **Python in Plain English** | 100k+ followers, newsletter push, editors can nominate for Medium Boost ($100–$500/week) | Medium draft submission |
| **KDnuggets** | Gold standard for Data Science. "Senior Data Scientist" badge of honor | Guest post pitch |
| **HackerNoon** | Love edgy tech stories ("How I beat the sportsbooks"). High acceptance rate if code is good | Guest post pitch |
| **PyCoder's Weekly** | Newsletter with massive reach | Submit link after publishing |

### Category C: Citizen Journalism (The "Naptown Crimebot" Hook)

Local papers are starved for technical talent — they have writers but zero data engineers.

**Your Pitch:** "I built a robot that reads the police blotter so you don't have to."

| Target | Notes |
|--------|-------|
| **Eye On Annapolis** | Digital-first, hyper-local. Pitch a monthly "Crime Data Summary" column via their Contact/Submit News form |
| **The Baltimore Banner** | Non-profit, data journalism focus. Pitch "Using RAG/LLMs to analyze Maryland crime data" |
| **Capital Gazette** | Traditional paper. Submit Op-Ed on "Transparency in Annapolis Police Data" citing your project |
| **Bellingcat** (reach goal) | World's top open-source investigation group. Article idea: "How to scrape and map local police data using Python (A Guide for Local Journalists)" — practically a guaranteed job interview for any Data Journalism role |

### The "Boost" Factor

Editors of Medium publications can nominate stories for a **Medium Boost**. A Boosted story often earns $100–$500 in a single week. This is why submitting to pubs (Category B) matters more than self-publishing.

---

## Strategy 3: The "Refresh" Tactic (Low Effort, High Reward)

Your top story is from Dec 2023. In the tech world, 2-year-old code often breaks or looks stale.

**The Play:** Write a "2026 Update" version.

- **Title:** "Unlocking Sports Betting with Python in 2026: Updated APIs & Libraries"
- **Content:** Copy the old notebook, update the libraries, add one new chart, publish as a fresh story.
- **Link:** Put an "Update: Read the 2026 version here" link at the very top of the old viral story.

**Result:** You funnel passive Google traffic from the old story into the new, paying story.

---

## Strategy 4: Consistency via VS Code + Agent Workflow

To hit $250, you need volume. You can't rely on one hit every 6 months.

### The Cadence: 2 Stories Per Week (8/month)

This is the tipping point where hobbyists become serious earners. Target: $250/month in 3-4 months.

### The "Heavy / Light" Split

Writing two deep-dive tutorials every week leads to burnout. Use a split strategy:

| Day | Type | Description |
|-----|------|-------------|
| **Tuesday** | "Anchor" (Heavy) | Deep technical tutorial. Code blocks, GitHub links, data analysis. This is for SEO and long-term authority. |
| **Friday** | "Update" (Light) | Shorter, lighter piece. Model results, quick tips, one-error fixes. Keeps followers engaged and signals activity to the algorithm. |

### Weekly Rotation

| Week | Tuesday (Heavy) | Friday (Light) |
|------|-----------------|----------------|
| 1 | Analysis — full technical tutorial | Quick Tip — one library or error |
| 2 | Tutorial — code-heavy walkthrough | Results — "here's what the model did" |
| 3 | Analysis — new dataset or API | Business Insight — results-heavy, less code |
| 4 | Tutorial — sequel to a past hit | Quick Tip — short and focused |

### The Agent Advantage

This is where the VS Code + Claude workflow pays off:

1. **You:** Write the code in Jupyter for the "Heavy" post
2. **Agent:** Extracts code to markdown for the Tuesday post
3. **Agent:** Takes your code results and drafts the "Friday Update" (e.g., "Summary of results: We lost $5 this week, here is why...")

**Result:** Two posts for the effort of one analysis session.

---

## Why 2x/Week Changes the Math

### Binge-Read Effect
Medium's algorithm loves "binge sessions." If a reader finishes your Part 1 on Tuesday and a related Part 2 is already available, they click through. Two reads from one person counts significantly more for earnings than two random reads — it signals **Member Retention**.

### Faster Data Feedback
With 8 posts per month, you get 8x the data points. You learn quickly whether your audience prefers code tutorials vs. betting results vs. data visualization tips. This lets you pivot the franchise strategy weeks earlier if something isn't landing.

### Franchise Speed
You can build a 4-part "NBA Betting System" series in two weeks instead of one month. This keeps momentum alive before readers forget who you are.

---

## Immediate Next Steps

1. **Refresh** the "Unlocking Sports Betting" story with a 2026 update
2. **Draft 3 sequel outlines** based on the original post's code
3. **Submit** the first sequel to **Towards Data Science** or **Level Up Coding** (prestige path)
4. **Set up syndication accounts** — Dev.to profile, verify Hashnode (@BenBallard), Mastodon (@benballrd11)
5. **Set the Tuesday/Friday cadence** and stick to it for 4 weeks
6. **First prestige pitch** — when the Naptown Crimebot project is ready, pitch Eye On Annapolis
7. **Review [STATS.md](STATS.md) monthly** to track what's working

---

## Publishing Workflow

```
1. Do analysis in Jupyter notebook        →  project-name/analysis.ipynb
2. Draft article as Quarto post           →  bendiagrams-site/bucket/post-slug/index.qmd
3. Preview locally                        →  quarto preview
4. Publish to BenDiagrams site            →  git push origin main
5. Wait 2-3 days for Google indexing
6. Cross-post to Medium                   →  medium.com/p/import (set canonical URL to site)
7. Syndicate to Dev.to + Hashnode         →  canonical URL pointing to site
8. Share on Mastodon
9. Update STATS.md monthly from medium.com/me/stats
```
