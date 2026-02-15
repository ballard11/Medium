# Setup Guide: BenDiagrams Site

**Current state:** Site is live at [ballard11.github.io/Medium](https://ballard11.github.io/Medium/) via GitHub Pages.

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

## Future: Custom Domain Setup

When you're ready to use a custom domain (e.g., `bendiagrams.com`):

### 1. Purchase Domain

Go to [Namecheap](https://namecheap.com) or your preferred registrar and purchase the domain (~$10-15/year).

### 2. Configure DNS Records

Add these records at your domain registrar:

| Type | Name | Value | TTL |
|------|------|-------|-----|
| A | @ | 185.199.108.153 | 3600 |
| A | @ | 185.199.109.153 | 3600 |
| A | @ | 185.199.110.153 | 3600 |
| A | @ | 185.199.111.153 | 3600 |
| CNAME | www | ballard11.github.io | 3600 |

DNS propagation: 15 minutes to 48 hours (usually 30 minutes).

### 3. Configure GitHub Pages

1. Go to repository **Settings** → **Pages**
2. Under "Custom domain", enter your domain
3. Click **Save**
4. Wait for DNS check (green checkmark)
5. Enable **Enforce HTTPS** when available

### 4. Update Site Config

In `_quarto.yml`, update:
```yaml
site-url: "https://yourdomain.com"
```

Create/update `CNAME` file in `bendiagrams-site/`:
```
yourdomain.com
```

---

## Future: Google Analytics

1. Create a GA4 property at [analytics.google.com](https://analytics.google.com)
2. Get your Measurement ID (`G-XXXXXXXXXX`)
3. In `_quarto.yml`, uncomment and update:
   ```yaml
   google-analytics: "G-XXXXXXXXXX"
   ```

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
