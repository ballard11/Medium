# Getting Started: BenDiagrams Site

**Status:** Live at [bendiagrams.com](https://bendiagrams.com) via GitHub Pages

---

## How It Works

- **Framework:** Quarto static site
- **Hosting:** GitHub Pages, auto-deployed via GitHub Actions on push to `main`
- **Domain:** `bendiagrams.com` (custom domain, HTTPS enforced)
- **Analytics:** Google Analytics (`G-7SD1391XRV`)
- **Repo:** [github.com/ballard11/Medium](https://github.com/ballard11/Medium) (the `bendiagrams-site/` directory)

Push to `main` → GitHub Actions builds → site updates in ~2-3 minutes.

---

## Content Buckets

| Section | Path | Description |
|---------|------|-------------|
| Sports & Odds | `sports/` | Betting models, player props, performance predictions |
| Economics | `economics/` | Inflation tracking, CPI analysis, macro indicators |
| Code & Labs | `code/` | API integrations, Python tutorials, experiments |
| The Toolbox | `toolbox/` | Quick-reference tool cards (Pandas, Plotly, CFBD API, etc.) |

---

## Creating a New Post

Each post lives in its own folder: `bucket/post-slug/index.qmd`

### 1. Create the post folder and copy the template

```bash
# Sports post
mkdir -p sports/my-post-slug
cp _templates/post-template.qmd sports/my-post-slug/index.qmd

# Economics post
mkdir -p economics/my-post-slug
cp _templates/post-template.qmd economics/my-post-slug/index.qmd

# Code post
mkdir -p code/my-post-slug
cp _templates/post-template.qmd code/my-post-slug/index.qmd
```

### 2. Update the YAML frontmatter

- `title:` - Post title
- `description:` - 1-2 sentence summary
- `date:` - Use `today` or `"2026-02-15"`
- `categories:` - e.g., `[sports, nba, python]`
- `image:` - Featured image path (relative to post folder, e.g., `images/chart.png`)
- `draft:` - Set to `false` when ready to publish

### 3. Add images

Create an `images/` subfolder inside the post folder:

```bash
mkdir sports/my-post-slug/images
```

Reference images relative to the post: `![Alt text](images/chart.png)`

### 4. Write the post

Follow the style: code → output → explain in plain English. Conversational tone.

### 5. Preview locally

```bash
quarto preview
```

### 6. Publish

```bash
git add .
git commit -m "Add post title"
git push origin main
```

Live in ~2-3 minutes.

---

## Creating a Toolbox Card

```bash
mkdir -p toolbox/my-tool
cp _templates/tool-template.qmd toolbox/my-tool/index.qmd
```

Fill in the YAML fields (tool name, category, links, etc.) and it auto-populates the Toolbox listing.

---

## Cross-Posting to Medium

1. Wait 2-3 days after publishing (let Google index your post first)
2. Go to [medium.com/p/import](https://medium.com/p/import)
3. Enter the post URL from `bendiagrams.com`
4. Verify canonical URL in Medium editor settings
5. Publish

---

## Common Commands

```bash
quarto preview          # Local dev server with auto-refresh
quarto render           # Build to _site/ without serving
git push origin main    # Deploy (triggers GitHub Actions)
```

---

## Key Files

| File | Purpose |
|------|---------|
| `_quarto.yml` | Site config (nav, theme, footer, SEO, GA) |
| `index.qmd` | Homepage with auto-listing of posts |
| `about.qmd` | About page |
| `styles.css` + `custom.scss` | Styling and dark mode |
| `_templates/post-template.qmd` | New post template |
| `_templates/tool-template.qmd` | New toolbox card template |
| `.github/workflows/publish.yml` | GitHub Actions deployment |
| `CNAME` | Custom domain file (`bendiagrams.com`) |
