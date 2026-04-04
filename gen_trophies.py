import os
import json
import urllib.request

# ── CONFIG ─────────────────────────────────────────────────────────────────────
USERNAME  = "amnandan9"
TOKEN     = ""          # optional: set your GitHub PAT here for higher rate limits
# ───────────────────────────────────────────────────────────────────────────────

bg       = "#0a0f0b"
border   = "#203a27"
title_c  = "#abd200"
text_c   = "#68b587"
sub_c    = "#b7d364"

def gh_api(path):
    url = f"https://api.github.com{path}"
    headers = {"User-Agent": "trophy-gen"}
    if TOKEN:
        headers["Authorization"] = f"token {TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

def calc_trophies(user, repos):
    commits  = user.get("public_gists", 0)     # rough proxy; real commits need GraphQL
    stars    = sum(r.get("stargazers_count", 0) for r in repos)
    prs      = 0                                # GitHub REST doesn't expose total PRs easily
    issues   = 0
    followers= user.get("followers", 0)
    repo_cnt = user.get("public_repos", 0)
    langs    = len(set(r.get("language") for r in repos if r.get("language")))
    yrs_since_2008 = max(1, 2026 - 2008)       # experience always S for now

    def grade(val, thresholds):
        # thresholds: [(min_val, grade_letter), ...] in descending order
        for mn, g in thresholds:
            if val >= mn:
                return g
        return "?"

    commit_thresholds = [(500,"S"),(300,"A"),(200,"B"),(100,"C"),(1,"?")]
    star_thresholds   = [(200,"S"),(100,"A"),(50,"B"),(10,"C"),(1,"?")]
    follow_thresholds = [(100,"S"),(50,"A"),(20,"B"),(5,"C"),(1,"?")]
    repo_thresholds   = [(50,"S"),(20,"A"),(10,"B"),(5,"C"),(1,"?")]
    lang_thresholds   = [(10,"S"),(7,"A"),(4,"B"),(2,"C"),(1,"?")]

    return [
        ("MultiLanguage",  grade(langs,    lang_thresholds),   f"{langs} Languages",     f"{langs*3}pt"),
        ("Commits",        grade(user.get("total_private_contributions",82), commit_thresholds), "High Committer", "82pt"),
        ("Followers",      grade(followers, follow_thresholds), "Dynamic User",           f"{followers*2}pt"),
        ("Repositories",   grade(repo_cnt,  repo_thresholds),   "High Repo Creator",      f"{repo_cnt*2}pt"),
        ("Experience",     "A",                                 "Intermediate Dev",        "15pt"),
        ("Stars",          grade(stars,    star_thresholds),    f"{stars} Stars",         f"{max(1,stars)}pt"),
        ("Issues",         "C",                                 "First Issue",             "1pt"),
        ("PullRequest",    "C",                                 "First Pull",              "8pt"),
    ]

print("Fetching live GitHub data...")
try:
    user  = gh_api(f"/users/{USERNAME}")
    repos = gh_api(f"/users/{USERNAME}/repos?per_page=100&sort=updated")
    trophies = calc_trophies(user, repos)
    print(f"  Followers: {user['followers']}  Repos: {user['public_repos']}  Stars: {sum(r.get('stargazers_count',0) for r in repos)}")
except Exception as e:
    print(f"Warning: could not fetch live data ({e}). Using last known values.")
    trophies = [
        ("MultiLanguage", "S", "Rainbow Lang User", "13pt"),
        ("Commits",       "A", "High Committer",    "82pt"),
        ("Followers",     "A", "Dynamic User",       "26pt"),
        ("Repositories",  "A", "High Repo Creator",  "28pt"),
        ("Experience",    "A", "Intermediate Dev",   "15pt"),
        ("Stars",         "C", "First Star",          "7pt"),
        ("Issues",        "C", "First Issue",          "1pt"),
        ("PullRequest",   "C", "First Pull",           "8pt"),
    ]

# ── SVG RENDER ─────────────────────────────────────────────────────────────────
TROPHY_W, TROPHY_H = 128, 128
COLS = 4
PAD  = 14
ROWS = (len(trophies) + COLS - 1) // COLS
SVG_W = TROPHY_W * COLS + PAD * (COLS + 1)
SVG_H = TROPHY_H * ROWS + PAD * (ROWS + 1) + 8

GRADE_COLOR = {"S": title_c, "A": sub_c, "B": text_c, "C": text_c, "?": "#555"}

def trophy_block(x, y, category, grade, label, pts):
    cup = GRADE_COLOR.get(grade, text_c)
    return f"""
  <g transform="translate({x},{y})">
    <rect width="{TROPHY_W}" height="{TROPHY_H}" rx="10" fill="{bg}" stroke="{border}" stroke-width="1.5"/>
    <!-- cup body -->
    <path d="M42,22 L86,22 L80,54 Q64,66 64,74 L64,84 L54,84 L54,74 Q54,66 48,54 Z"
          fill="none" stroke="{cup}" stroke-width="2.5" stroke-linejoin="round"/>
    <!-- handles -->
    <path d="M42,28 Q28,28 28,42 Q28,56 42,50" fill="none" stroke="{cup}" stroke-width="2"/>
    <path d="M86,28 Q100,28 100,42 Q100,56 86,50" fill="none" stroke="{cup}" stroke-width="2"/>
    <!-- base platform -->
    <rect x="46" y="84" width="36" height="4"  rx="2" fill="{cup}" opacity="0.85"/>
    <rect x="40" y="88" width="48" height="5"  rx="2" fill="{cup}" opacity="0.85"/>
    <!-- grade -->
    <text x="64" y="56" text-anchor="middle" fill="{cup}"
          font-family="'Courier New',monospace" font-size="20" font-weight="bold">{grade}</text>
    <!-- category -->
    <text x="64" y="107" text-anchor="middle" fill="{title_c}"
          font-family="'Courier New',monospace" font-size="9" font-weight="bold">{category}</text>
    <!-- label -->
    <text x="64" y="117" text-anchor="middle" fill="{text_c}"
          font-family="'Courier New',monospace" font-size="7.5">{label}</text>
    <!-- pts -->
    <text x="64" y="126" text-anchor="middle" fill="{sub_c}"
          font-family="'Courier New',monospace" font-size="7" opacity="0.9">{pts}</text>
  </g>"""

cells = ""
for i, t in enumerate(trophies):
    col = i % COLS
    row = i // COLS
    x = PAD + col * (TROPHY_W + PAD)
    y = PAD + row * (TROPHY_H + PAD)
    cells += trophy_block(x, y, *t)

svg = f"""<svg width="{SVG_W}" height="{SVG_H}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{SVG_W}" height="{SVG_H}" fill="{bg}"/>
  {cells}
</svg>"""

os.makedirs("assets", exist_ok=True)
with open("assets/trophies.svg", "w", encoding="utf-8") as f:
    f.write(svg)
print(f"Saved assets/trophies.svg  ({SVG_W}x{SVG_H})")
