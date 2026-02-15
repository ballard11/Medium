# Getting Started: Your Complete Blog Setup

**Status:** ✅ All infrastructure built and ready for deployment

**What just happened:** I built your complete Quarto blog infrastructure for "The Modeled World" based on your project brief. Everything is ready except for 3 manual steps (domain purchase, GitHub repo creation, and config placeholders).

---

## 📁 What Was Created

### Core Files
- ✅ `_quarto.yml` - Main configuration (navigation, theme, analytics)
- ✅ `index.qmd` - Homepage with auto-listing of latest posts
- ✅ `about.qmd` - About page template
- ✅ `styles.css` + `custom.scss` - Custom styling with dark mode support

### Three Content Buckets
- ✅ `sports/index.qmd` - Sports & Odds listing page
- ✅ `economics/index.qmd` - Economics & Trends listing page
- ✅ `code/index.qmd` - Code & Labs listing page

### Templates & Workflows
- ✅ `_templates/post-template.qmd` - Standard post structure in your Medium style
- ✅ `.github/workflows/publish.yml` - Auto-deployment via GitHub Actions
- ✅ `.gitignore` - Protects API keys, data files, secrets

### Documentation
- ✅ `README.md` - Project overview and tech stack
- ✅ `SETUP.md` - Complete deployment instructions
- ✅ `MIGRATION.md` - How to migrate your top 5 Medium articles
- ✅ `requirements.txt` - Python dependencies

### Example Post
- ✅ `sports/oklahoma-football-evolution.qmd` - Your Oklahoma analysis, formatted for the blog

### Domain Config
- ✅ `CNAME` - Contains `modeledworld.com` for custom domain

### Workflow Updates
- ✅ Updated `~/.claude/memory/workflow.md` - New Quarto publishing workflow documented

---

## 🚀 Next Steps (3 Manual Tasks)

### 1. Purchase Domain (5 minutes)
Go to [Namecheap](https://namecheap.com) or [Google Domains](https://domains.google.com):
- Search for `modeledworld.com` (or your preferred domain)
- Purchase (~$12/year)
- **Don't configure DNS yet** - you'll do that after GitHub setup

### 2. Create GitHub Repository (5 minutes)

**Option A: Via GitHub Web Interface**
1. Go to [github.com/new](https://github.com/new)
2. Repository name: `the-modeled-world`
3. **IMPORTANT:** Make it **Private** (since we're skipping comments)
4. Do NOT initialize with README (we have files already)
5. Click "Create repository"

**Option B: Via GitHub CLI** (if you have `gh` installed)
```bash
cd "the-modeled-world"
gh repo create the-modeled-world --private --source=. --remote=origin
```

### 3. Update Configuration Placeholders (10 minutes)

Open `_quarto.yml` and replace these placeholders:

```yaml
# Line ~8
repo-url: "https://github.com/YOUR_USERNAME/the-modeled-world"
# Replace YOUR_USERNAME with your actual GitHub username

# Line ~22
href: "https://github.com/YOUR_USERNAME"
# Replace YOUR_USERNAME

# Line ~24
href: "https://twitter.com/YOUR_HANDLE"
# Replace YOUR_HANDLE with your Twitter/X handle (or remove if you don't want this)

# Line ~42
creator: "@YOUR_HANDLE"
# Replace with your Twitter handle

# Line ~47
google-analytics: "G-XXXXXXXXXX"
# Replace with your GA4 measurement ID (or leave as-is to set up later)
```

**Also update these files:**
- `README.md` - Search for `YOUR_USERNAME` and replace (3 occurrences)
- `index.qmd` - Update GitHub issue link (line ~38)

---

## 🎯 First Deployment (15 minutes)

### Step 1: Initialize Git and Push

From the `the-modeled-world/` directory:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Quarto blog infrastructure"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/the-modeled-world.git

# Push to main branch
git branch -M main
git push -u origin main
```

### Step 2: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages** (left sidebar)
3. Under "Build and deployment":
   - Source: **Deploy from a branch**
   - Branch: Select `gh-pages` / `(root)` (will be created automatically)
4. Click **Save**

### Step 3: Wait for First Deploy

1. Go to **Actions** tab in your repo
2. Watch the "Publish Quarto Site" workflow run
3. Takes ~2-3 minutes
4. When complete, your site is live at: `https://YOUR_USERNAME.github.io/the-modeled-world/`

### Step 4: Configure Custom Domain

**In your domain registrar (Namecheap/Google Domains):**

Add these DNS records:

| Type | Name | Value | TTL |
|------|------|-------|-----|
| A | @ | 185.199.108.153 | 3600 |
| A | @ | 185.199.109.153 | 3600 |
| A | @ | 185.199.110.153 | 3600 |
| A | @ | 185.199.111.153 | 3600 |
| CNAME | www | YOUR_USERNAME.github.io | 3600 |

**In GitHub Settings → Pages:**
1. Custom domain: Enter `modeledworld.com`
2. Click **Save**
3. Wait for DNS check (5-30 minutes)
4. Enable **Enforce HTTPS** when available

**DNS propagation:** 15 minutes to 48 hours (usually 30 minutes)

---

## ✍️ Your First New Post

### Step 1: Copy the Template

```bash
cd the-modeled-world

# Create a new sports post
cp _templates/post-template.qmd sports/my-first-post.qmd

# Open in VS Code
code sports/my-first-post.qmd
```

### Step 2: Update YAML Frontmatter

Change these fields:
- `title:` - Your post title
- `description:` - 1-2 sentence summary
- `date:` - Use `today` or `"2026-02-15"`
- `categories:` - e.g., `[sports, nba, python]`
- `image:` - Featured image filename (create `sports/images/` folder)
- `draft:` - Set to `false` when ready to publish

### Step 3: Write Your Post

Follow the template structure:
1. Hook (relatable opening)
2. Value prop ("I'll show you how to...")
3. Progressive building (code → output → explain)
4. Visualizations
5. Personal closing

**Remember:**
- Show code, then output, then explain
- Inline logic (no helper functions upfront)
- Conversational tone: "Let's take a look..."
- Use `#| eval: false` if you don't want code to execute during render

### Step 4: Preview Locally

```bash
quarto preview
```

Opens at `http://localhost:XXXX` with auto-refresh.

### Step 5: Publish

```bash
git add .
git commit -m "Add my first post"
git push origin main
```

**Your post goes live in ~2 minutes.**

### Step 6: Cross-Post to Medium (2-3 Days Later)

1. Wait 2-3 days for Google to index your post
2. Go to [medium.com/p/import](https://medium.com/p/import)
3. Enter: `https://modeledworld.com/sports/my-first-post.html`
4. Verify canonical URL in Medium editor settings
5. Publish or save as draft

---

## 📊 Example Post Ready

I've already created your first example post:
- **File:** `sports/oklahoma-football-evolution.qmd`
- **Content:** Your Oklahoma football analysis (2020-2025)
- **Status:** Ready to publish

**To publish it:**

```bash
cd the-modeled-world
git add sports/oklahoma-football-evolution.qmd
git commit -m "Add Oklahoma football evolution analysis"
git push origin main
```

After deploy completes, it will be live at:
`https://modeledworld.com/sports/oklahoma-football-evolution.html`

---

## 📈 Migration Plan

Your top 5 Medium articles are ready to migrate. See [MIGRATION.md](MIGRATION.md) for the complete checklist.

**Quick overview:**
1. **Unlocking Sports Betting with Python** - $32.26, 6.7K views
2. **Analyzing NBA Data Using Python and APIs** - $13.45, 14.1K views
3. **Analyze NBA Stats with the NBA API** - $12.47, 3.8K views
4. **How to Scrape Google Trends Data** - $4.92, 2.3K views
5. **Using Python and APIs to Analyze the NBA** - $3.60, 2.5K views

**Timeline:** 6-8 hours spread over 3 weeks to migrate all 5.

---

## 🛠️ Common Commands

### Preview Locally
```bash
cd the-modeled-world
quarto preview
```

### Create New Post
```bash
# Sports post
cp _templates/post-template.qmd sports/new-post.qmd

# Economics post
cp _templates/post-template.qmd economics/new-post.qmd

# Code post
cp _templates/post-template.qmd code/new-post.qmd
```

### Publish to Blog
```bash
git add .
git commit -m "Add [post title]"
git push origin main
```

### Check Deployment Status
Go to: `https://github.com/YOUR_USERNAME/the-modeled-world/actions`

### Render Without Preview
```bash
quarto render
```
Output goes to `_site/` folder

---

## 🎨 Customization Ideas (Later)

Once you're comfortable with the basics:

### Brand Colors
Edit `custom.scss` to add your brand colors:
```scss
$primary: #007bff;  // Change to your brand color
```

### ConvertKit Email Signup
1. Sign up at [convertkit.com](https://convertkit.com)
2. Create a form
3. Copy embed code
4. Paste into `index.qmd` (replace placeholder at line ~53)

### Google Analytics
1. Create GA4 property at [analytics.google.com](https://analytics.google.com)
2. Copy measurement ID (`G-XXXXXXXXXX`)
3. Add to `_quarto.yml` line ~47

### Affiliate Links
Add to relevant posts:
- Sports betting posts → DraftKings/FanDuel signup links
- Python tutorials → Course affiliate links
- Data tools → Software referral links

---

## 🆘 Troubleshooting

### "Quarto not found"
```bash
# Check installation
quarto --version

# If not installed, download from:
# https://quarto.org/docs/get-started/
```

### "Python module not found"
```bash
# Install dependencies
pip install -r requirements.txt
```

### "Site not deploying"
1. Check Actions tab for errors
2. Verify `gh-pages` branch exists
3. Confirm GitHub Pages is enabled in Settings

### "Custom domain not working"
1. Verify DNS records are correct
2. Check DNS propagation: [dnschecker.org](https://dnschecker.org)
3. Wait 15-30 minutes (sometimes up to 48 hours)

### "HTTPS not available"
- Wait 10-15 minutes after DNS check passes
- GitHub auto-provisions SSL via Let's Encrypt
- If stuck, remove custom domain and re-add

---

## 📚 Resources

- **Quarto Documentation:** https://quarto.org/docs/websites/
- **GitHub Pages:** https://docs.github.com/pages
- **Your Workflow:** `~/.claude/memory/workflow.md`
- **Setup Guide:** `SETUP.md`
- **Migration Guide:** `MIGRATION.md`

---

## ✅ Checklist: Launch Day

- [ ] Purchase domain `modeledworld.com`
- [ ] Create private GitHub repo `the-modeled-world`
- [ ] Update placeholders in `_quarto.yml`, `README.md`, `index.qmd`
- [ ] Initialize git and push to GitHub
- [ ] Enable GitHub Pages in repo settings
- [ ] Wait for first deploy (~2-3 minutes)
- [ ] Configure DNS records at domain registrar
- [ ] Add custom domain in GitHub Pages settings
- [ ] Wait for DNS propagation + enable HTTPS
- [ ] Test: Visit `https://modeledworld.com`
- [ ] Publish first post (Oklahoma example is ready!)
- [ ] Share on LinkedIn/Twitter with YOUR domain

**Time estimate:** ~45 minutes for complete setup

---

## 🎯 What You've Built

**Before:** Medium-only strategy earning ~$85/year from 43K views

**After:**
- Your own blog (SEO credit, email list, full control)
- Auto-deployment (git push → live in 2 minutes)
- Cross-posting to Medium (keep the distribution + earnings)
- Email capture ready (future sponsorship opportunities)
- Affiliate link infrastructure
- 3 organized content buckets
- Professional, fast, searchable site

**Potential revenue by end of 2026:** $8K-25K vs. $85/year

---

## 🚀 Ready to Launch?

1. Start with the "3 Manual Tasks" above
2. Follow "First Deployment" steps
3. Watch your site go live
4. Publish the Oklahoma example post
5. Start migrating your top 5 Medium articles

**You've got this.** The infrastructure is built. Time to publish.

Questions? Check `SETUP.md` or open an issue on the repo.
