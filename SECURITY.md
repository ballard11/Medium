# Security Guide: Public Repo, Private Logic

**Strategy:** Air-gap sensitive code from your public blog while building social proof.

---

## The "Air-Gap" Layers

### Layer 1: .gitignore Shield (MUST HAVE)

Your `.gitignore` file is your first line of defense. It tells GitHub: "Do not upload these folders."

**Protected folders/files:**
- `data/`, `raw_data/`, `datasets/` - Raw CSVs, scraped data, proprietary datasets
- `.env`, `.env.*` - API keys, database passwords, tokens
- `notebooks/scratch/` - Messy exploratory notebooks
- `models/`, `*.pkl`, `*.h5` - Trained ML models with proprietary weights
- `proprietary/`, `private/` - Anything explicitly marked as sensitive

**What gets published:**
- Clean analysis notebooks (`.qmd` files in `sports/`, `economics/`, `code/`)
- Polished visualizations
- Example code with placeholders (`YOUR_API_KEY`)
- Frozen outputs (charts, tables, results)

---

## Layer 2: Code Hiding Strategies

Quarto gives you fine-grained control over what code is visible.

### Strategy A: Hide ALL Code (Show Results Only)

**Use case:** Your entire analysis uses proprietary methods

**YAML header:**
```yaml
execute:
  freeze: true
  echo: false  # Hides all code blocks
```

**Result:** Readers see charts, insights, and results. No code visible.

---

### Strategy B: Selective Hiding (Best for Most Posts)

**Use case:** Show setup/simple code, hide proprietary algorithms

**Example:**
```python
# PUBLIC: Show setup (readers can follow along)
import pandas as pd
import matplotlib.pyplot as plt

api_key = "YOUR_API_KEY"  # Placeholder
df = pd.read_csv("public_dataset.csv")
```

```python
#| echo: false

# HIDDEN: Proprietary betting algorithm
from my_proprietary_models import BettingModel  # Not in repo
model = BettingModel(secret_params=load_from_env())
predictions = model.predict(df, alpha=PROPRIETARY_ALPHA)
```

```python
# PUBLIC: Show results
plt.plot(predictions)
plt.title("Betting Model Predictions")
plt.show()
```

**What readers see:**
- Setup code (can reproduce)
- Results/charts
- **Not visible:** Your secret algorithm

---

### Strategy C: Collapsible Code

**Use case:** Code is okay to show, but you want clean reading experience

```python
#| code-fold: true
#| code-summary: "Click to see the full code"

# This code is hidden behind a collapsible button
def complex_data_processing(df):
    # 50 lines of data munging...
    return cleaned_df
```

**Result:** Readers can expand to see code if they want, but it's not cluttering the post.

---

## Layer 3: Freeze Strategy (Nuclear Option)

**Use case:** Heavy proprietary models that can't run in GitHub Actions

**How it works:**
1. Run your analysis **locally** with your real API keys and proprietary code
2. Quarto saves the outputs (charts, tables) in `_freeze/` folder
3. Push to GitHub
4. GitHub Actions deploys the frozen results **without re-running your code**

**Setup:**
```yaml
execute:
  freeze: true  # Already in your template
```

**Workflow:**
```bash
# On your laptop (private)
quarto render  # Runs your proprietary code, saves outputs

# Push to GitHub (public)
git add .
git commit -m "Add new post"
git push  # GitHub deploys frozen outputs, never sees your code
```

**Critical:** Your proprietary Python scripts (`.py` files) stay in folders blocked by `.gitignore`.

---

## What to Publish vs. Hide

### ✅ SAFE TO PUBLISH (Build Authority)

**Setup code:**
```python
import pandas as pd
import cfbd

configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'  # Placeholder
```

**Data fetching (public APIs):**
```python
games = api_instance.get_games(year=2025)
df = pd.DataFrame.from_records([g.to_dict() for g in games])
```

**Basic analysis:**
```python
# Calculate points per game
avg_ppg = df['points'].mean()
print(f"Average: {avg_ppg:.1f} PPG")
```

**Visualizations:**
```python
plt.plot(df['game_number'], df['cumulative_points'])
plt.show()
```

### ❌ NEVER PUBLISH (Proprietary)

**Real API keys:**
```python
api_key = "sk_live_abc123xyz..."  # NEVER in code
```

**Proprietary algorithms:**
```python
# Your secret betting edge
def calculate_betting_edge(odds, historical_data):
    secret_factor = PROPRIETARY_CONSTANT * math.log(...)
    return adjusted_line
```

**Trained model weights:**
```python
model = load_model('models/my_betting_model.pkl')  # File is gitignored
```

**Raw scraped data:**
```python
df = pd.read_csv('data/scraped_odds_2020_2025.csv')  # Folder is gitignored
```

---

## The "Black Box with Glass Windows" Approach

**What you show:**
- "I built a model to predict NBA player props"
- "Here's the data I collected" (aggregated, not raw)
- "Here are the results" (charts, accuracy metrics)
- "Here's how to build your own version" (general approach)

**What you hide:**
- Exact feature engineering steps
- Hyperparameters and model architecture
- Training data specifics
- The actual prediction logic

**Result:** People see you're an expert (authority) but can't clone your exact system (protection).

---

## Repo Structure Example

```
Medium/  (PUBLIC REPO)
├── sports/
│   └── nba-prop-predictions.qmd  # Polished post, selective code
├── economics/
│   └── inflation-analysis.qmd
├── code/
│   └── api-tutorial.qmd
├── _templates/
│   └── post-template.qmd  # Includes hiding strategies
│
├── data/  # ❌ GITIGNORED
│   └── scraped_odds.csv  # Never uploaded
│
├── models/  # ❌ GITIGNORED
│   └── betting_model.pkl  # Never uploaded
│
├── notebooks/scratch/  # ❌ GITIGNORED
│   └── messy_exploration.ipynb  # Never uploaded
│
├── proprietary/  # ❌ GITIGNORED
│   └── betting_algorithm.py  # Never uploaded
│
└── .env  # ❌ GITIGNORED
    API_KEY=sk_live_abc123...
```

---

## Security Checklist

Before pushing ANY commit:

- [ ] Check `.gitignore` is up to date
- [ ] No real API keys in code (use placeholders: `YOUR_API_KEY`)
- [ ] No proprietary algorithms visible (use `#| echo: false`)
- [ ] No raw data files committed (check `git status`)
- [ ] Run `git diff` to verify what's being pushed
- [ ] If using freeze, run `quarto render` locally first

---

## Emergency: "I Accidentally Committed a Secret"

If you push an API key or secret by accident:

**Step 1: REVOKE THE KEY IMMEDIATELY**
- Go to the service (CFBD, Medium, etc.)
- Revoke the leaked API key
- Generate a new one

**Step 2: Remove from Git History**
```bash
# DO NOT just delete the file - it's still in git history!
# Use BFG Repo-Cleaner or git-filter-repo to purge

# Simple case: if it's the most recent commit
git reset HEAD~1  # Undo commit
# Fix .gitignore, remove sensitive file
git add .
git commit -m "Add security fixes"
git push --force  # ⚠️ Only if no one else is using the repo
```

**Step 3: Update all keys**
- Change any secrets that were exposed
- Update `.env` locally with new keys

---

## Why This Works

**You get:**
- Public portfolio (networking, social proof, authority)
- Free GitHub Pages hosting
- Full control over what's visible
- Protection for proprietary methods

**You don't give away:**
- Your competitive edge (betting algorithms)
- Your data sources (scraped/purchased data)
- Your API keys (security)
- Your messy exploration process (professionalism)

**The balance:** Transparent enough to build trust, opaque enough to protect value.

---

## Resources

- [GitHub: Remove Sensitive Data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- [Quarto: Code Display Options](https://quarto.org/docs/computations/execution-options.html#code-output)
- [Quarto: Freeze Feature](https://quarto.org/docs/projects/code-execution.html#freeze)

---

**Bottom line:** Public repo for authority, `.gitignore` + code hiding for protection.
