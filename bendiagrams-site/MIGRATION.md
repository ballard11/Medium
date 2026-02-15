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

### 1. Unlocking Sports Betting with Python
- **Stats**: $32.26 earned, 6,700 views, 56% read ratio
- **Target bucket**: `/sports/`
- **New title**: Keep same or "How to Unlock Sports Betting Data with Python and APIs"
- **Affiliate opportunity**: DraftKings/FanDuel sign-up links ($50-100 CPA)

### 2. Analyzing NBA Data Using Python and APIs
- **Stats**: $13.45 earned, 14,100 views, 39% read ratio
- **Target bucket**: `/sports/`
- **New title**: Keep same
- **Affiliate opportunity**: DataCamp Python courses, NBA API courses

### 3. Analyze NBA Stats with the NBA API and Python
- **Stats**: $12.47 earned, 3,800 views, 61% read ratio
- **Target bucket**: `/sports/`
- **New title**: Keep same or merge with #2 if too similar
- **Affiliate opportunity**: Python courses, sports analytics tools

### 4. How to Scrape Google Trends Data
- **Stats**: $4.92 earned, 2,300 views
- **Target bucket**: `/code/`
- **New title**: "How to Scrape Google Trends Data with Python"
- **Affiliate opportunity**: Python courses, web scraping tools

### 5. Using Python and APIs to Analyze the NBA
- **Stats**: $3.60 earned, 2,500 views
- **Target bucket**: `/sports/`
- **New title**: Keep or merge with other NBA posts
- **Note**: May be similar to #2 and #3 - review before migrating

---

## Migration Process (Per Article)

### Step 1: Copy Original Content
1. Open the article on Medium
2. Copy the full text (including code blocks)
3. Create new `.qmd` file in appropriate bucket:
   ```bash
   touch bendiagrams-site/sports/unlocking-sports-betting-python.qmd
   ```

### Step 2: Convert to Quarto Format

**Update YAML frontmatter:**
```yaml
---
title: "Original Title Here"
description: "Short 1-2 sentence summary"
author: "Ben Ballard"
date: "YYYY-MM-DD"  # Use original Medium publish date
categories: [sports, python, betting, apis]
image: image.png  # You'll need to save the featured image
draft: false
execute:
  freeze: true
  echo: true
  warning: false
jupyter: python3
---
```

**Convert text:**
- Regular paragraphs stay as-is
- Code blocks: Change from Medium's format to:
  ````markdown
  ```{python}
  # Your code here
  ```
  ````

**Add outputs:**
- If the original showed outputs, add them as separate Python blocks:
  ````markdown
  ```{python}
  print("Output here")
  ```
  ````

### Step 3: Download/Recreate Images

**Option A: Download from Medium**
1. Right-click images in your Medium post
2. Save to `bendiagrams-site/sports/images/`
3. Reference in markdown: `![Alt text](images/chart.png)`

**Option B: Regenerate from Code**
1. If the article had code that generated charts, run it locally
2. Save outputs to `images/` folder
3. Better quality and you own the files

### Step 4: Enhance (This is Your Chance!)

Since you're migrating, make improvements:

**Add:**
- Updated data (e.g., 2024-2025 season instead of 2020)
- Interactive Plotly charts instead of static images
- Affiliate links at strategic points
- Email signup CTA at the bottom
- "Updated [date]" note at the top

**Remove:**
- Any Medium-specific references
- Outdated information
- Links to other Medium articles (replace with your blog links)

### Step 5: Test Locally
```bash
cd bendiagrams-site
quarto preview
```

Check:
- All images load correctly
- Code blocks render properly
- Links work
- Looks good on mobile (resize browser window)

### Step 6: Publish
```bash
git add .
git commit -m "Migrate: [Article Title]"
git push origin main
```

### Step 7: Update Medium Post

**Add a redirect notice at the top of the Medium version:**
> **📌 Update (Feb 2026):** This article has been updated and expanded on [BenDiagrams](https://ballard11.github.io/Medium/sports/article-slug). The code examples now include 2024-2025 season data and interactive visualizations.

**Why not delete the Medium post?**
- It's still earning you money ($32/article over time)
- Drives traffic to your blog via the redirect notice
- Shows up in Medium search, introducing readers to your brand

---

## Migration Checklist

### Article 1: Unlocking Sports Betting with Python
- [ ] Copy content from Medium
- [ ] Create `.qmd` file in `/sports/`
- [ ] Convert to Quarto format
- [ ] Download/recreate all images
- [ ] Add updated 2024-2025 betting data
- [ ] Add DraftKings affiliate link
- [ ] Add email signup CTA
- [ ] Test locally with `quarto preview`
- [ ] Publish to blog
- [ ] Update Medium post with redirect notice
- [ ] Submit to Google Search Console

### Article 2: Analyzing NBA Data Using Python and APIs
- [ ] Copy content from Medium
- [ ] Create `.qmd` file in `/sports/`
- [ ] Convert to Quarto format
- [ ] Download/recreate all images
- [ ] Update with 2024-2025 NBA season data
- [ ] Add affiliate links (Python courses)
- [ ] Add email signup CTA
- [ ] Test locally
- [ ] Publish to blog
- [ ] Update Medium post
- [ ] Submit to Google Search Console

### Article 3: Analyze NBA Stats with the NBA API and Python
- [ ] Decide: Migrate separately or merge with Article 2?
- [ ] Copy content from Medium
- [ ] Create `.qmd` file in `/sports/`
- [ ] Convert to Quarto format
- [ ] Download/recreate all images
- [ ] Update with latest NBA API endpoints
- [ ] Add affiliate links
- [ ] Add email signup CTA
- [ ] Test locally
- [ ] Publish to blog
- [ ] Update Medium post
- [ ] Submit to Google Search Console

### Article 4: How to Scrape Google Trends Data
- [ ] Copy content from Medium
- [ ] Create `.qmd` file in `/code/`
- [ ] Convert to Quarto format
- [ ] Download/recreate all images
- [ ] Verify code still works (APIs change)
- [ ] Add web scraping tool affiliate links
- [ ] Add email signup CTA
- [ ] Test locally
- [ ] Publish to blog
- [ ] Update Medium post
- [ ] Submit to Google Search Console

### Article 5: Using Python and APIs to Analyze the NBA
- [ ] Review: Is this too similar to Articles 2 & 3?
- [ ] If migrating: Follow same process as above
- [ ] If merging: Combine best parts into Article 2 or 3

---

## Post-Migration SEO Checklist

After migrating all 5 articles:

### Google Search Console
1. Sign up at [search.google.com/search-console](https://search.google.com/search-console)
2. Verify ownership of `ballard11.github.io/Medium`
3. Submit sitemap: `https://ballard11.github.io/Medium/sitemap.xml`
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
- Migrate Articles 1 & 2 (your top earners)
- Set up Google Search Console
- Submit for indexing

**Week 2:**
- Migrate Articles 3 & 4
- Add internal links between posts
- Share on social media

**Week 3:**
- Review Article 5 (migrate or merge decision)
- Add affiliate links to all posts
- Update Medium posts with redirect notices

**Total effort:** ~6-8 hours spread over 3 weeks

---

## Expected Results (3-6 months)

**SEO Impact:**
- Your domain starts ranking for "NBA API Python", "sports betting Python", etc.
- Google search traffic: 50-100 visits/month initially
- Grows to 200-500 visits/month by month 6

**Email List:**
- 5-10 signups/month from organic search
- Compounds over time

**Revenue:**
- Medium posts continue earning (~$50/year)
- Your blog posts earn via affiliates ($20-50/month by month 6)
- Email list enables sponsorships when you hit 500+ subs

**The multiplier effect:** Every article on YOUR domain builds YOUR asset, not Medium's.

---

## Questions?

If you hit issues during migration:
- Quarto formatting problems? Check [Quarto docs](https://quarto.org/docs/authoring/)
- Image issues? Make sure paths are relative to the `.qmd` file
- Code not running? Verify `execute: freeze: true` is set
- Can't find original images? Use `archive.org` to view old versions of your Medium posts

Ready to start? Begin with Article 1 (highest earner) to validate the process.
