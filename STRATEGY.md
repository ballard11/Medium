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

## Strategy 2: The "Distribution" Upgrade (Stop Self-Publishing)

Your big hit was published under "Ben Ballard" (self-published). This relies 100% on SEO.

**The Fix:** Submit your next draft to a major publication.

**Target Publications:**
- Level Up Coding
- Python in Plain English
- Towards Data Science
- PyCoder's Weekly

**Why:** They have 100k+ followers. If they accept your story, they push it to their newsletter. This generates "Member Read Time" immediately, rather than waiting for Google.

**The "Boost" Factor:** Editors of these pubs can nominate stories for a Medium Boost. A Boosted story often earns $100–$500 in a single week.

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
3. **Submit** the first sequel to Level Up Coding or Python in Plain English
4. **Set the Tuesday/Friday cadence** and stick to it for 4 weeks
5. **Review [STATS.md](STATS.md) monthly** to track what's working

---

## Publishing Workflow

```
1. Do analysis in Jupyter notebook     →  project-name/analysis.ipynb
2. Write polished article in markdown  →  project-name/article.md
3. Publish as draft to Medium          →  python publish.py project-name
4. Review on Medium, edit, then go public
5. Update project README.md with Medium URL and stats
6. Update STATS.md monthly from medium.com/me/stats
```
