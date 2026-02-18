# Migration Plan: Top 5 Medium Articles

**Goal:** Migrate your highest-earning Medium articles to your blog to establish authority and capture SEO credit.

---

## Why Migrate?

1. **SEO Ownership**: These articles have proven they rank well. Get Google to index YOUR domain for these searches.
2. **Authority Signal**: A new blog with 5 quality posts looks established, not empty.
3. **Traffic Capture**: Future searches will find your domain first, building your email list.
4. **Affiliate Opportunities**: Add affiliate links to your versions (can't do this on Medium).

---

## Top 5 Articles to Migrate

Based on your Medium stats (from STATS.md):

### 1. Unlocking Sports Betting with Python — MIGRATED
- **Stats**: $32.26 earned, 6,700 views, 34.3% read rate
- **Location**: `posts/sports-betting-python/index.qmd`
- **Affiliate opportunity**: DraftKings/FanDuel sign-up links ($50-100 CPA)

### 2. Analyzing NBA Data Using Python and APIs — MIGRATED
- **Stats**: $13.45 earned, 14,100 views, 41.1% read rate
- **Location**: `posts/analyzing-nba-data/index.qmd`
- **Affiliate opportunity**: DataCamp Python courses, NBA API courses

### 3. Analyze NBA Stats with the NBA API and Python — MIGRATED
- **Stats**: $12.47 earned, 3,800 views, 28.9% read rate
- **Location**: `posts/nba-stats-api-python/index.qmd`
- **Affiliate opportunity**: Python courses, sports analytics tools

### 4. Using Google Trends API with Python
- **Stats**: $7.58 earned, 4,300 views, 44.9% read rate
- **Target**: `posts/google-trends-api-python/index.qmd`
- **New title**: Keep same or "How to Use the Google Trends API with Python"
- **Affiliate opportunity**: Python courses, web scraping tools

### 5. Easy Live Sports Odds: A Guide to Google Sheets
- **Stats**: $2.86 earned, 1,990 views, 27.4% read rate
- **Target**: `posts/live-sports-odds-google-sheets/index.qmd`
- **Note**: Lower-code piece, different audience than the Python tutorials

---

## Migration Process (Per Article)

### Step 1: Create the post folder

```bash
mkdir -p posts/post-slug/images
cp _templates/post-template.qmd posts/post-slug/index.qmd
```

### Step 2: Copy and convert content
1. Open the article on Medium
2. Copy the full text (including code blocks)
3. Convert to Quarto format in the `index.qmd`

**Update YAML frontmatter:**
```yaml
---
title: "Original Title Here"
description: "Short 1-2 sentence summary"
author: "Ben Ballard"
date: "YYYY-MM-DD"  # Use original Medium publish date
categories: [sports, python, betting, apis]
image: images/featured.png
draft: false
execute:
  eval: false
  echo: true
  warning: false
---
```

**Convert code blocks** to Quarto format:
````markdown
```{python}
# Your code here
```
````

### Step 3: Download/Recreate Images

**Option A: Download from Medium**
1. Right-click images in your Medium post
2. Save to `post-slug/images/`
3. Reference in markdown: `![Alt text](images/chart.png)`

**Option B: Regenerate from Code**
1. Run the original notebook code locally
2. Save outputs to `images/` folder
3. Better quality and you own the files

### Step 4: Test Locally
```bash
quarto preview
```

Check:
- All images load correctly
- Code blocks render properly
- Links work
- Looks good on mobile (resize browser window)

### Step 5: Publish
```bash
git add .
git commit -m "Migrate: [Article Title]"
git push origin main
```

### Step 6: Update Medium Post

**Add a redirect notice at the top of the Medium version:**
> **Update (Feb 2026):** This article has been updated and expanded on [BenDiagrams](https://bendiagrams.com/sports/article-slug). The code examples now include 2024-2025 season data and interactive visualizations.

**Why not delete the Medium post?**
- It's still earning you money ($32/article over time)
- Drives traffic to your blog via the redirect notice
- Shows up in Medium search, introducing readers to your brand

---

## Migration Checklist

### Article 1: Unlocking Sports Betting with Python — DONE
- [x] Copy content from Medium
- [x] Create `sports/sports-betting-python/index.qmd`
- [x] Convert to Quarto format
- [x] Download/recreate all images
- [ ] Add updated 2025-2026 betting data
- [ ] Add DraftKings affiliate link
- [ ] Test locally with `quarto preview`
- [ ] Update Medium post with redirect notice
- [ ] Submit to Google Search Console

### Article 2: Analyzing NBA Data Using Python and APIs — DONE
- [x] Copy content from Medium
- [x] Create `sports/analyzing-nba-data/index.qmd`
- [x] Convert to Quarto format
- [x] Download/recreate all images
- [ ] Update with 2024-2025 NBA season data
- [ ] Add affiliate links (Python courses)
- [ ] Test locally
- [ ] Update Medium post
- [ ] Submit to Google Search Console

### Article 3: Analyze NBA Stats with the NBA API and Python — DONE
- [x] Copy content from Medium
- [x] Create `sports/nba-stats-api-python/index.qmd`
- [x] Convert to Quarto format
- [x] Download/recreate all images
- [ ] Update with latest NBA API endpoints
- [ ] Add affiliate links
- [ ] Test locally
- [ ] Update Medium post
- [ ] Submit to Google Search Console

### Article 4: Using Google Trends API with Python — NOT STARTED
- [ ] Copy content from Medium
- [ ] Create `posts/google-trends-api-python/index.qmd`
- [ ] Convert to Quarto format
- [ ] Download/recreate all images
- [ ] Verify code still works (APIs change)
- [ ] Add affiliate links
- [ ] Test locally
- [ ] Publish to blog
- [ ] Update Medium post
- [ ] Submit to Google Search Console

### Article 5: Easy Live Sports Odds: Google Sheets — NOT STARTED
- [ ] Copy content from Medium
- [ ] Create `posts/live-sports-odds-google-sheets/index.qmd`
- [ ] Convert to Quarto format
- [ ] Download/recreate all images
- [ ] Test locally
- [ ] Publish to blog
- [ ] Update Medium post
- [ ] Submit to Google Search Console

---

## Post-Migration SEO Checklist

After migrating all 5 articles:

### Google Search Console
1. Sign up at [search.google.com/search-console](https://search.google.com/search-console)
2. Verify ownership of `bendiagrams.com`
3. Submit sitemap: `https://bendiagrams.com/sitemap.xml`
4. Request indexing for each migrated article

### Internal Linking
- [ ] Add "Related Posts" section to each article
- [ ] Link between similar topics (NBA posts link to each other)
- [ ] Link from homepage to migrated articles

### Social Sharing
- [ ] Share each migrated article on LinkedIn
- [ ] Share on Twitter/X
- [ ] Tag relevant people/communities
- [ ] Use YOUR domain in all shares (not Medium links)

---

## Timeline

**Week 1:**
- ~~Migrate Articles 1, 2 & 3~~ (done)
- Set up Google Search Console
- Submit for indexing

**Week 2:**
- Migrate Articles 4 & 5
- Add internal links between posts
- Share on social media

**Week 3:**
- Add affiliate links to all posts
- Update Medium posts with redirect notices

**Total remaining effort:** ~3-4 hours spread over 2 weeks

---

## Expected Results (3-6 months)

**SEO Impact:**
- Your domain starts ranking for "NBA API Python", "sports betting Python", etc.
- Google search traffic: 50-100 visits/month initially
- Grows to 200-500 visits/month by month 6

**Revenue:**
- Medium posts continue earning (~$50/year)
- Your blog posts earn via affiliates ($20-50/month by month 6)

**The multiplier effect:** Every article on YOUR domain builds YOUR asset, not Medium's.
