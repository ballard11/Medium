# BenDiagrams

A data science lab for sports analytics, economic trends, and code experiments.

🌐 **Live Site:** [ballard11.github.io/Medium](https://ballard11.github.io/Medium)
📝 **Medium:** [@ben.g.ballard](https://medium.com/@ben.g.ballard)
🔧 **Tech Stack:** Quarto + GitHub Pages + Python

---

## What Is This?

**BenDiagrams** is my learning lab where I apply the Feynman Technique to data science: learning by teaching, teaching by doing, doing by showing the code.

Every post includes:
- Real code (Python, Pandas, Plotly)
- Real data (APIs, datasets, live sources)
- Real results (interactive charts, analysis, insights)

### Three Content Buckets

1. **[Sports & Odds](/sports/)** - Betting algorithms, player props, sports analytics
2. **[Economics & Trends](/economics/)** - Inflation tracking, CPI analysis, macro indicators
3. **[Code & Labs](/code/)** - Tutorials, API integrations, Python how-tos

---

## Publishing Strategy

**Primary:** Publish on this blog (I own it, SEO credit goes to me)
**Secondary:** Cross-post to Medium 2-3 days later with canonical URLs (discovery + monetization)

**Why?** Build an asset I control while still leveraging Medium's distribution.

---

## Tech Stack

### Core
- **Quarto** - Static site generator that combines Jupyter notebooks + markdown
- **GitHub Pages** - Free hosting with custom domain
- **GitHub Actions** - Auto-deployment on `git push`
- **Python** - Data analysis, visualization, modeling

### Python Libraries
- Pandas, NumPy (data manipulation)
- Matplotlib, Plotly (visualization)
- cfbd, requests (API clients)
- Jupyter (notebooks)

### Services
- **Google Analytics** - Traffic tracking
- **ConvertKit** - Email list (coming soon)
- **Namecheap** - Domain registration

**Total cost:** ~$12/year (domain only)

---

## Project Structure

```
bendiagrams-site/
├── _quarto.yml              # Main site configuration
├── index.qmd                # Homepage
├── about.qmd                # About page
├── styles.css               # Custom styling
├── custom.scss              # SASS variables
├── CNAME                    # Custom domain config
├── requirements.txt         # Python dependencies
│
├── sports/                  # Sports & Odds bucket
│   ├── index.qmd            # Sports listing page
│   └── *.qmd                # Individual posts
│
├── economics/               # Economics & Trends bucket
│   ├── index.qmd            # Economics listing page
│   └── *.qmd                # Individual posts
│
├── code/                    # Code & Labs bucket
│   ├── index.qmd            # Code listing page
│   └── *.qmd                # Individual posts
│
├── _templates/              # Post templates
│   └── post-template.qmd    # Standard post structure
│
└── .github/workflows/       # CI/CD
    └── publish.yml          # Auto-deployment workflow
```

---

## Local Development

### Prerequisites
- [Quarto](https://quarto.org/docs/get-started/) installed
- Python 3.11+
- Git

### Setup

```bash
# Clone the repo
git clone https://github.com/ballard11/bendiagrams-site.git
cd bendiagrams-site

# Install Python dependencies
pip install -r requirements.txt

# Preview locally (auto-refreshes on changes)
quarto preview
```

Opens at `http://localhost:XXXX`

### Create New Post

```bash
# Copy template to appropriate bucket
cp _templates/post-template.qmd sports/my-new-post.qmd

# Edit the file
code sports/my-new-post.qmd

# Preview
quarto preview
```

### Deploy to Production

```bash
# Stage changes
git add .

# Commit with clear message
git commit -m "Add [post title]"

# Push (triggers auto-deployment via GitHub Actions)
git push origin main
```

**Site updates in ~2 minutes.**

---

## Writing Guidelines

### Post Structure (Template)

Every post follows this pattern:

1. **Hook** - Relatable opening, personal, conversational
2. **Value Prop** - "I'll show you how to [specific outcome]"
3. **Progressive Building** - Step-by-step code → output → explanation
4. **Visualizations** - Interactive charts (Plotly preferred)
5. **Insights** - What the data actually means
6. **Personal Closing** - Future plans, call to engage

### Code Style

✅ **Do:**
- Show code → show output → explain in plain English
- Use inline logic, nested loops (don't abstract into helper functions)
- Hardcoded examples with real IDs/dates
- Comments that explain *intent*: `# Replace with your actual API key`
- Display outputs immediately after code blocks

❌ **Don't:**
- Pre-define helper functions at the start
- Use complex `.env` path resolution
- Explain theory before showing code
- Use academic/formal tone

### Tone

- **Conversational**: "Let's take a look", "So what data did we really get?"
- **Personal**: "I'm very excited", "I plan to revisit this"
- **Confident**: "Money Back Guarantee. Just get your own API key."
- **Helpful**: "I've made it for you easy below"
- Active voice, first-person perspective

---

## Deployment

### Automatic Deployment

Every push to `main` triggers GitHub Actions:

1. Installs Quarto and Python dependencies
2. Renders all `.qmd` files to HTML
3. Deploys to `gh-pages` branch
4. Updates live site

**Check deployment status:** [Actions tab](https://github.com/ballard11/bendiagrams-site/actions)

### Custom Domain Setup

**Domain:** `ballard11.github.io/Medium` (configured in CNAME file)

**DNS Records** (at domain registrar):
- 4 A records pointing to GitHub IPs
- 1 CNAME for www subdomain

**GitHub Settings:**
- Custom domain: `ballard11.github.io/Medium`
- Enforce HTTPS: ✅ Enabled

See [SETUP.md](SETUP.md) for detailed instructions.

---

## Content Migration

Currently migrating top 5 Medium articles (~$67 in earnings, 30K+ views) to establish authority.

See [MIGRATION.md](MIGRATION.md) for the migration plan.

---

## Workflow

**Goal:** 2 posts/week with ~75 min per article

### Weekly Timeline

| Day | Activity | Time |
|-----|----------|------|
| **Mon** | Pick topic + brief | 15 min |
| **Tue** | AI drafts → Review locally | 30 min |
| **Wed** | Refine → Publish to blog | 10 min |
| **Fri** | Import to Medium (2-3 days later) | 10 min |

**Total:** ~65 minutes per article

See [workflow.md](../memory/workflow.md) for complete details.

---

## Monetization Strategy

### Current: Medium Partner Program
- ~$85 earned from 43K views (lifetime)
- Expected: $100-150/year with cross-posting

### Phase 2: Email List + Sponsorships
- ConvertKit signup forms (coming soon)
- Target: 500+ subscribers by Q3 2026
- Sponsorship rate: $500-2K per post
- Potential: $2K-5K/year

### Phase 3: Affiliate Links
- Sports betting: DraftKings, FanDuel ($50-100 CPA)
- Python courses: DataCamp, Coursera (30-50% commission)
- Tools: APIs, data services
- Potential: $1K-3K/year

### Phase 4: Products (Future)
- Sports analytics course
- Python tutorials
- Consulting from portfolio
- Potential: $5K-20K/year

**Total realistic revenue by end of 2026:** $8K-25K
**vs. Medium-only:** ~$85/year

---

## Success Metrics

### Content (Current)
- ✅ Quarto blog infrastructure built
- ✅ 2x/week publishing workflow documented
- 🔄 Migrating top 5 Medium articles
- 📅 Publishing 2 new posts/week (starting [date])

### Growth (6 months)
- 100+ email subscribers
- 2,000+ monthly blog visitors
- 10K+ Medium views/month
- Google search traffic established

### Monetization (12 months)
- $500+ from Medium Partner Program
- $2K+ from sponsorships/affiliates
- 500+ email subscribers
- First product/course launched

---

## Contributing

This is a personal blog, but if you find errors or have suggestions:

1. **Typos/errors:** [Open an issue](https://github.com/ballard11/bendiagrams-site/issues)
2. **Code improvements:** [Submit a PR](https://github.com/ballard11/bendiagrams-site/pulls)
3. **Content suggestions:** [Drop a comment on the blog](https://ballard11.github.io/Medium) or find me on [Medium](https://medium.com/@ben.g.ballard)

---

## License

- **Content** (posts, articles): © Ben Ballard, All Rights Reserved
- **Code** (examples, snippets in posts): MIT License - use freely
- **Infrastructure** (Quarto config, templates): MIT License

---

## Contact

- **Medium:** [@ben.g.ballard](https://medium.com/@ben.g.ballard)
- **LinkedIn:** [Ben Ballard](https://www.linkedin.com/in/ben-ballard-44969313/)
- **GitHub:** [@ballard11](https://github.com/ballard11)

---

**Built with [Quarto](https://quarto.org) • Hosted on [GitHub Pages](https://pages.github.com)**
