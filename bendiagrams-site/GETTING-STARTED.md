# Getting Started: BenDiagrams Site

**Status:** Live at [ballard11.github.io/Medium](https://ballard11.github.io/Medium/) via GitHub Pages

---

## How It Works

- **Framework:** Quarto static site
- **Hosting:** GitHub Pages, auto-deployed via GitHub Actions on push to `main`
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

### 1. Copy the template

```bash
# Sports post
cp _templates/post-template.qmd sports/my-new-post.qmd

# Economics post
cp _templates/post-template.qmd economics/my-new-post.qmd

# Code post
cp _templates/post-template.qmd code/my-new-post.qmd
```

### 2. Update the YAML frontmatter

- `title:` - Post title
- `description:` - 1-2 sentence summary
- `date:` - Use `today` or `"2026-02-15"`
- `categories:` - e.g., `[sports, nba, python]`
- `image:` - Featured image path
- `draft:` - Set to `false` when ready to publish

### 3. Write the post

Follow the style: code → output → explain in plain English. Conversational tone.

### 4. Preview locally

```bash
quarto preview
```

### 5. Publish

```bash
git add .
git commit -m "Add post title"
git push origin main
```

Live in ~2-3 minutes.

---

## Creating a Toolbox Card

```bash
cp _templates/tool-template.qmd toolbox/my-tool.qmd
```

Fill in the YAML fields (tool name, category, links, etc.) and it auto-populates the Toolbox listing.

---

## Cross-Posting to Medium

1. Wait 2-3 days after publishing (let Google index your post first)
2. Go to [medium.com/p/import](https://medium.com/p/import)
3. Enter the post URL
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

## Future Additions (When Ready)

- **Newsletter:** Email capture via ConvertKit (placeholder removed for now)
- **Custom domain:** Purchase domain → configure DNS → update `_quarto.yml` site-url
- **Google Analytics:** Uncomment and add GA4 measurement ID in `_quarto.yml`
- **Migration:** Top Medium articles can be cross-posted with canonical URLs

---

## Key Files

| File | Purpose |
|------|---------|
| `_quarto.yml` | Site config (nav, theme, footer, SEO) |
| `index.qmd` | Homepage with auto-listing of posts |
| `about.qmd` | About page |
| `styles.css` + `custom.scss` | Styling and dark mode |
| `_templates/post-template.qmd` | New post template |
| `_templates/tool-template.qmd` | New toolbox card template |
| `.github/workflows/publish.yml` | GitHub Actions deployment |
