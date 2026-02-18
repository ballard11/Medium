# Setup Guide: BenDiagrams Site

**Current state:** Site is live at [bendiagrams.com](https://bendiagrams.com) via GitHub Pages.

---

## How Deployment Works

1. Push to `main` branch
2. GitHub Actions (`.github/workflows/publish.yml`) runs:
   - Installs Quarto and Python dependencies
   - Renders the site from `bendiagrams-site/`
   - Deploys to `gh-pages` branch
3. Site updates in ~2-3 minutes

Check deployment status: [GitHub Actions](https://github.com/ballard11/Medium/actions)

---

## Custom Domain (Done)

Domain `bendiagrams.com` is configured and live.

- **`_quarto.yml`:** `site-url: "https://bendiagrams.com"`
- **`CNAME` file:** `bendiagrams.com`
- **GitHub Pages:** Custom domain set in Settings → Pages, HTTPS enforced

### DNS Records (for reference)

| Type | Name | Value | TTL |
|------|------|-------|-----|
| A | @ | 185.199.108.153 | 3600 |
| A | @ | 185.199.109.153 | 3600 |
| A | @ | 185.199.110.153 | 3600 |
| A | @ | 185.199.111.153 | 3600 |
| CNAME | www | ballard11.github.io | 3600 |

---

## Google Analytics (Done)

GA4 is active in `_quarto.yml`:
```yaml
google-analytics: "G-7SD1391XRV"
```

View data at [analytics.google.com](https://analytics.google.com).

---

## Troubleshooting

### Site Not Deploying
- Check [GitHub Actions](https://github.com/ballard11/Medium/actions) for errors
- Verify `gh-pages` branch exists
- Confirm GitHub Pages is enabled in Settings → Pages

### Custom Domain Not Working
- Verify DNS records are correct
- Check propagation: [dnschecker.org](https://dnschecker.org)
- Wait 15-30 minutes, sometimes up to 48 hours

### HTTPS Not Available
- Wait 10-15 minutes after DNS check passes
- GitHub auto-provisions SSL via Let's Encrypt
- If stuck, remove custom domain and re-add

### Preview Not Working Locally
```bash
quarto --version        # Check Quarto is installed
pip install -r requirements.txt  # Install dependencies
quarto preview          # Start local dev server
```
