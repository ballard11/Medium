# Setup Guide: The Modeled World

Complete setup instructions for deploying your Quarto blog to GitHub Pages with a custom domain.

---

## Phase 0: Pre-Flight Checklist

### 1. Purchase Domain
- [ ] Go to [Namecheap](https://namecheap.com), [Google Domains](https://domains.google), or your preferred registrar
- [ ] Search for `modeledworld.com` (or your preferred domain)
- [ ] Purchase domain (~$10-15/year)
- [ ] Wait for domain registration to complete (usually instant)

### 2. Create GitHub Repository
- [ ] Go to [GitHub](https://github.com) and create a new **private** repository
- [ ] Name it `the-modeled-world` (or your preferred name)
- [ ] Do NOT initialize with README (we already have files)
- [ ] Leave it private since we're skipping comments (no need for public repo)

---

## Phase 1: Initial Repository Setup

### 1. Initialize Git and Push to GitHub

From the `the-modeled-world/` directory:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Quarto blog structure"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/the-modeled-world.git

# Push to main branch
git branch -M main
git push -u origin main
```

### 2. Configure GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages** (in left sidebar)
3. Under "Build and deployment":
   - Source: **Deploy from a branch**
   - Branch: Select `gh-pages` / `(root)` (this will be created by GitHub Actions)
4. Click **Save**

### 3. Enable GitHub Actions

Your `.github/workflows/publish.yml` is already configured. On your first push, GitHub Actions will:
1. Detect the workflow file
2. Install Quarto and Python dependencies
3. Render your site
4. Deploy to `gh-pages` branch
5. Make your site live at `https://YOUR_USERNAME.github.io/the-modeled-world/`

**First deploy takes ~2-3 minutes.** Check progress at:
- Repository → **Actions** tab

---

## Phase 2: Custom Domain Setup

### 1. Configure DNS (At Your Domain Registrar)

Log in to your domain registrar (Namecheap, Google Domains, etc.) and add these DNS records:

#### A Records (for apex domain: modeledworld.com)
Add **four** A records pointing to GitHub's IP addresses:

| Type | Name | Value | TTL |
|------|------|-------|-----|
| A | @ | 185.199.108.153 | 3600 |
| A | @ | 185.199.109.153 | 3600 |
| A | @ | 185.199.110.153 | 3600 |
| A | @ | 185.199.111.153 | 3600 |

#### CNAME Record (for www subdomain)

| Type | Name | Value | TTL |
|------|------|-------|-----|
| CNAME | www | YOUR_USERNAME.github.io | 3600 |

**Replace `YOUR_USERNAME`** with your actual GitHub username.

**DNS propagation takes 5 minutes to 48 hours.** Usually it's 15-30 minutes.

### 2. Configure Custom Domain in GitHub

1. Go to repository **Settings** → **Pages**
2. Under "Custom domain", enter: `modeledworld.com`
3. Click **Save**
4. Wait for DNS check to complete (green checkmark)
5. Check **Enforce HTTPS** (wait until available, usually 5-10 minutes)

### 3. Verify CNAME File

The `CNAME` file in your repository should contain:
```
modeledworld.com
```

This file tells GitHub Pages which domain to serve your site from.

---

## Phase 3: Update Configuration

### 1. Update `_quarto.yml`

Replace placeholder values:

```yaml
website:
  site-url: "https://modeledworld.com"  # ✅ Update this
  repo-url: "https://github.com/YOUR_USERNAME/the-modeled-world"  # ✅ Update this

  navbar:
    right:
      - icon: github
        href: "https://github.com/YOUR_USERNAME"  # ✅ Update this
      - icon: twitter
        href: "https://twitter.com/YOUR_HANDLE"  # ✅ Update this

format:
  html:
    twitter-card:
      creator: "@YOUR_HANDLE"  # ✅ Update this
      site: "@YOUR_HANDLE"

    google-analytics: "G-XXXXXXXXXX"  # ✅ Add your GA4 ID (see below)
```

### 2. Set Up Google Analytics (Optional but Recommended)

1. Go to [Google Analytics](https://analytics.google.com)
2. Create a new property for `modeledworld.com`
3. Get your Measurement ID (format: `G-XXXXXXXXXX`)
4. Add it to `_quarto.yml` under `google-analytics`

### 3. Set Up ConvertKit Email List (Optional but Recommended)

1. Sign up for [ConvertKit](https://convertkit.com) (free up to 1,000 subscribers)
2. Create a form for newsletter signups
3. Copy the embed code
4. Replace the placeholder in `index.qmd` (line ~53):

```html
<div id="newsletter">
  <!-- Paste ConvertKit embed code here -->
</div>
```

---

## Phase 4: First Post & Deploy

### 1. Create Your First Post

Copy the template and customize it:

```bash
# Create a new sports post
cp _templates/post-template.qmd sports/oklahoma-football-analysis.qmd

# Edit the file
code sports/oklahoma-football-analysis.qmd
```

Update the YAML frontmatter:
- Change title, description, categories
- Set `date: "2026-02-15"` (or `today`)
- Add an image if you have one

### 2. Preview Locally

```bash
# From the-modeled-world/ directory
quarto preview
```

This opens a local preview at `http://localhost:XXXX`. Any changes you make will auto-refresh.

### 3. Deploy to Production

```bash
# Stage your changes
git add .

# Commit with a clear message
git commit -m "Add Oklahoma football analysis post"

# Push to GitHub (triggers auto-deploy)
git push origin main
```

**Your site updates in ~2 minutes.** Check the Actions tab to watch progress.

---

## Phase 5: Cross-Post to Medium

### 1. Wait 2-3 Days

Let Google index your original post first. This ensures your domain gets SEO credit.

### 2. Import to Medium

1. Go to [medium.com/p/import](https://medium.com/p/import)
2. Enter your blog post URL: `https://modeledworld.com/sports/oklahoma-football-analysis.html`
3. Medium imports it automatically
4. **Critical**: Verify the canonical URL is set
   - In Medium editor, click "..." → "More settings"
   - Check that "Original article URL" shows your domain
   - If not, manually add it

### 3. Publish on Medium

- Review formatting (sometimes code blocks need adjustment)
- Add Medium-specific tags
- Publish to relevant publications if desired

---

## Ongoing Workflow

Your new workflow is:

1. **Monday**: Create new post from template
   ```bash
   cp _templates/post-template.qmd sports/new-post.qmd
   ```

2. **Tuesday**: Write and preview locally
   ```bash
   quarto preview
   ```

3. **Wednesday**: Push to GitHub (auto-deploys)
   ```bash
   git add .
   git commit -m "Add new post"
   git push
   ```

4. **Friday**: Import to Medium with canonical URL

**Total time**: ~75 minutes per article (your target)

---

## Troubleshooting

### Site Not Deploying
- Check GitHub Actions tab for errors
- Verify `gh-pages` branch exists
- Check that GitHub Pages is enabled in Settings

### Custom Domain Not Working
- Verify DNS records are correct
- Check DNS propagation: [dnschecker.org](https://dnschecker.org)
- Wait 15-30 minutes, sometimes up to 48 hours

### HTTPS Not Available
- Wait 10-15 minutes after DNS check passes
- GitHub auto-provisions SSL certificates via Let's Encrypt
- If stuck, remove custom domain and re-add it

### Preview Not Working Locally
- Ensure Quarto is installed: `quarto --version`
- Check Python dependencies: `pip install -r requirements.txt`
- Try `quarto render` first, then `quarto preview`

---

## Next Steps

- [ ] Migrate your top 5 Medium articles (see MIGRATION.md)
- [ ] Set up Google Search Console
- [ ] Create content calendar
- [ ] Add affiliate links structure
- [ ] Customize theme colors in `custom.scss`

---

## Support

- Quarto Docs: https://quarto.org/docs/websites/
- GitHub Pages Docs: https://docs.github.com/pages
- If stuck: Open an issue on the blog repo
