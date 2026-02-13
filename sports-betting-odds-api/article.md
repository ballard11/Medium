# Unlocking Sports Betting with Python in 2026: Updated APIs, Player Props & New Charts

*By Ben Ballard*

> **Update:** This is a refreshed version of my original [Unlocking Sports Betting with Python](https://medium.com/@ben.g.ballard/unlocking-sports-betting-with-python-the-odds-api-3bc74eb24153) from December 2023. Updated code, new markets, and better visualizations.

Back in 2023, I wrote a walkthrough on pulling live sports odds with Python and The Odds API. It became my most-read article — over 6,700 views and counting.

Two years later, the API has evolved significantly. New markets like **player props** and **alternate lines** have been added. Libraries have been updated. And the sports betting landscape in the US has exploded — 38 states now have legal online betting.

So let's do this again, from scratch, with everything updated for 2026.

## What You'll Need

- **Python 3.9+** (I'm using 3.12)
- A free API key from [The Odds API](https://the-odds-api.com) (500 requests/month on the free tier)
- `requests`, `pandas`, `numpy`, `matplotlib`

```bash
pip install requests pandas numpy matplotlib python-dotenv
```

Store your API key in a `.env` file:

```
ODDS_API_KEY=your_key_here
```

## Step 1: See What's In Season

The `/sports` endpoint is your starting point. It returns every sport the API currently covers, along with a `key` you'll need for the odds endpoint.

```python
import os
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('ODDS_API_KEY')
BASE_URL = 'https://api.the-odds-api.com/v4'

response = requests.get(
    f'{BASE_URL}/sports',
    params={'apiKey': API_KEY}
)
response.raise_for_status()

sports = response.json()
sports_df = pd.DataFrame(sports)
sports_df = sports_df[sports_df['active'] == True][['key', 'group', 'title']]
sports_df.head(10)
```

You'll see keys like `basketball_nba`, `americanfootball_nfl`, `soccer_epl`, etc. The `active` flag tells you if games are currently available.

**Pro tip:** Check the response headers for your API quota:

```python
print(f"Requests used: {response.headers.get('x-requests-used')}")
print(f"Requests remaining: {response.headers.get('x-requests-remaining')}")
```

The free tier gives you 500 requests/month. The `/sports` endpoint is free — it doesn't count against your quota.

## Step 2: Pull Live Odds

Now the main event. We'll pull **moneyline (h2h)**, **spread**, and **totals** odds for NBA games from US bookmakers in American odds format.

```python
SPORT = 'basketball_nba'

response = requests.get(
    f'{BASE_URL}/sports/{SPORT}/odds',
    params={
        'apiKey': API_KEY,
        'regions': 'us',
        'markets': 'h2h,spreads,totals',
        'oddsFormat': 'american',
        'dateFormat': 'iso',
    }
)
response.raise_for_status()

events = response.json()
print(f"Events returned: {len(events)}")
```

Each event contains a list of `bookmakers`, and each bookmaker has `markets` with `outcomes`. It's deeply nested JSON — which brings us to the most important step.

### Key Parameters

| Parameter | Options | Notes |
|-----------|---------|-------|
| `regions` | `us`, `us2`, `uk`, `eu`, `au` | Each region costs 1 request unit |
| `markets` | `h2h`, `spreads`, `totals`, `outrights` | Each market costs 1 request unit |
| `oddsFormat` | `american`, `decimal` | American = +150/-200 style |
| `dateFormat` | `iso`, `unix` | ISO is easier to work with in pandas |

**Cost formula:** requests used = number of regions × number of markets. So `regions=us&markets=h2h,spreads,totals` costs 3 quota units.

## Step 3: Flatten the Nested JSON

The API response is three levels deep: events → bookmakers → markets → outcomes. We need to flatten this into a tidy DataFrame.

```python
def flatten_odds(events):
    """Flatten the nested API response into a tidy DataFrame."""
    rows = []
    for event in events:
        game = f"{event['away_team']} @ {event['home_team']}"
        for bookmaker in event['bookmakers']:
            for market in bookmaker['markets']:
                for outcome in market['outcomes']:
                    row = {
                        'game': game,
                        'home_team': event['home_team'],
                        'away_team': event['away_team'],
                        'commence_time': event['commence_time'],
                        'bookmaker': bookmaker['title'],
                        'market': market['key'],
                        'outcome': outcome['name'],
                        'price': outcome['price'],
                    }
                    if 'point' in outcome:
                        row['point'] = outcome['point']
                    rows.append(row)
    return pd.DataFrame(rows)

odds_df = flatten_odds(events)
odds_df['commence_time'] = pd.to_datetime(odds_df['commence_time'])
```

Now you have a flat DataFrame where each row is one line from one bookmaker for one team in one game. This is the foundation for everything else.

## Step 4: Compare Moneylines Across Bookmakers

Different bookmakers set different prices for the same outcome. The gap between them is where informed bettors find value.

```python
ml_df = odds_df[odds_df['market'] == 'h2h'].copy()

ml_pivot = ml_df.pivot_table(
    index=['game', 'outcome'],
    columns='bookmaker',
    values='price',
    aggfunc='first'
)

ml_pivot['best_odds'] = ml_pivot.max(axis=1)
ml_pivot['worst_odds'] = ml_pivot.min(axis=1)
ml_pivot['spread_gap'] = ml_pivot['best_odds'] - ml_pivot['worst_odds']

ml_pivot.sort_values('spread_gap', ascending=False)
```

The `spread_gap` column tells you where bookmakers disagree the most — and where line shopping pays off.

Here's what that looks like visualized for a single game:

![Moneyline comparison across bookmakers](https://raw.githubusercontent.com/ballard11/Medium/main/sports-betting-odds-api/images/moneyline_comparison.png)

## Step 5: Convert to Implied Probability

American odds are useful for calculating payouts, but **implied probability** is what you actually need to evaluate bets. Here's the conversion:

```python
def american_to_implied_prob(odds):
    """Convert American odds to implied probability."""
    if odds > 0:
        return 100 / (odds + 100)
    else:
        return abs(odds) / (abs(odds) + 100)

ml_df['implied_prob'] = ml_df['price'].apply(american_to_implied_prob)
```

**How to read it:** If a team's moneyline is -200, the bookmaker believes there's a 66.7% chance they win. If another book has the same team at -180 (64.3%), the second book thinks they're slightly less likely to win — or is offering a better price.

When you average the implied probability across all bookmakers, you get a consensus estimate:

![Implied win probability by game](https://raw.githubusercontent.com/ballard11/Medium/main/sports-betting-odds-api/images/implied_probability.png)

## Step 6: NEW — Player Props

This is the biggest change since 2023. The Odds API now supports **player prop markets** including points, rebounds, assists, threes, and more. These use the event-level endpoint:

```python
# Get event IDs
events_response = requests.get(
    f'{BASE_URL}/sports/{SPORT}/events',
    params={'apiKey': API_KEY, 'dateFormat': 'iso'}
)
event_list = events_response.json()
event_id = event_list[0]['id']

# Fetch player props for one game
props_response = requests.get(
    f'{BASE_URL}/sports/{SPORT}/events/{event_id}/odds',
    params={
        'apiKey': API_KEY,
        'regions': 'us',
        'markets': 'player_points,player_rebounds,player_assists',
        'oddsFormat': 'american',
        'dateFormat': 'iso',
    }
)
props_data = props_response.json()
```

Flatten it the same way:

```python
def flatten_props(event_data):
    """Flatten player props response into a DataFrame."""
    rows = []
    for bookmaker in event_data.get('bookmakers', []):
        for market in bookmaker['markets']:
            for outcome in market['outcomes']:
                rows.append({
                    'bookmaker': bookmaker['title'],
                    'market': market['key'],
                    'player': outcome.get('description', outcome['name']),
                    'side': outcome['name'],
                    'line': outcome.get('point', None),
                    'price': outcome['price'],
                })
    return pd.DataFrame(rows)

props_df = flatten_props(props_data)
```

Now you can compare **player point lines across bookmakers** — where books disagree on a player's total is where you'll find the most interesting bets:

![Player props comparison across bookmakers](https://raw.githubusercontent.com/ballard11/Medium/main/sports-betting-odds-api/images/player_props_comparison.png)

The red delta values show where bookmakers have set different lines for the same player. A 1.5-point gap on a player's total might not sound like much, but it can be the difference between a -110 line and a +120 line at different books.

## What's Changed Since 2023

| Feature | 2023 | 2026 |
|---------|------|------|
| Player props | Not available | Points, rebounds, assists, threes, TDs, and more |
| Alternate lines | Not available | `alternate_spreads`, `alternate_totals` |
| Game period markets | Not available | Quarter/half/period-specific h2h, spreads, totals |
| Both teams to score | Not available | `btts` for soccer |
| Sports coverage | ~30 sports | 40+ sports including esports |
| Free tier | 500 req/month | 500 req/month (unchanged) |

## Full Code

The complete Jupyter notebook with all the code from this article is available on GitHub:

**[GitHub: sports-betting-odds-api/analysis.ipynb](https://github.com/ballard11/Medium/tree/main/sports-betting-odds-api)**

## What's Next

This article gets you from zero to live odds data in Python. In the next installment, we'll build a **Streamlit dashboard** that auto-refreshes these odds and highlights the biggest bookmaker discrepancies in real time.

If you found this useful, follow me on [Medium](https://medium.com/@ben.g.ballard) for the next part of the series.

---

*Originally published on [Medium](https://medium.com/@ben.g.ballard)*
