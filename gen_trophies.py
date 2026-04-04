import os

bg = "#0a0f0b"
border = "#203a27"
title_col = "#abd200"
text_col = "#68b587"
sub_col = "#b7d364"

# Trophy data - matches actual amnandan9 GitHub profile
trophies = [
    ("MultiLanguage", "S", "Rainbow Lang User", "13pt"),
    ("Commits",       "A", "High Committer",    "82pt"),
    ("Followers",     "A", "Dynamic User",       "26pt"),
    ("Repositories",  "A", "High Repo Creator",  "28pt"),
    ("Experience",    "A", "Intermediate Dev",   "15pt"),
    ("Stars",         "C", "First Star",         "7pt"),
    ("Issues",        "C", "First Issue",        "1pt"),
    ("PullRequest",   "C", "First Pull",         "8pt"),
]

TROPHY_W = 120
TROPHY_H = 120
COLS = 4
ROWS = (len(trophies) + COLS - 1) // COLS
PAD = 16
SVG_W = TROPHY_W * COLS + PAD * (COLS + 1)
SVG_H = TROPHY_H * ROWS + PAD * (ROWS + 1) + 10

def trophy_svg(x, y, category, grade, label, pts):
    cup_color = title_col if grade == "S" else sub_col if grade in ("A",) else text_col
    return f"""
  <g transform="translate({x},{y})">
    <rect width="{TROPHY_W}" height="{TROPHY_H}" rx="10" fill="{bg}" stroke="{border}" stroke-width="1.5"/>
    
    <!-- Trophy cup body -->
    <path d="M42,22 L78,22 L72,52 Q60,62 60,70 L60,80 L50,80 L50,70 Q50,62 48,52 Z"
          fill="none" stroke="{cup_color}" stroke-width="2.5" stroke-linejoin="round"/>
    <!-- Cup handles -->
    <path d="M42,28 Q30,28 30,40 Q30,52 42,48" fill="none" stroke="{cup_color}" stroke-width="2"/>
    <path d="M78,28 Q90,28 90,40 Q90,52 78,48" fill="none" stroke="{cup_color}" stroke-width="2"/>
    <!-- Cup base -->
    <rect x="44" y="80" width="32" height="4" rx="2" fill="{cup_color}" opacity="0.8"/>
    <rect x="38" y="84" width="44" height="5" rx="2" fill="{cup_color}" opacity="0.8"/>
    
    <!-- Grade letter -->
    <text x="60" y="52" text-anchor="middle" fill="{cup_color}" font-family="monospace" font-size="18" font-weight="bold">{grade}</text>
    
    <!-- Category name -->
    <text x="60" y="103" text-anchor="middle" fill="{title_col}" font-family="monospace" font-size="9" font-weight="bold">{category}</text>
    <!-- Label -->
    <text x="60" y="113" text-anchor="middle" fill="{text_col}" font-family="monospace" font-size="7.5">{label}</text>
    <!-- Points -->
    <text x="60" y="122" text-anchor="middle" fill="{sub_col}" font-family="monospace" font-size="7" opacity="0.8">{pts}</text>
  </g>"""

elements = ""
for i, (cat, grade, label, pts) in enumerate(trophies):
    col = i % COLS
    row = i // COLS
    x = PAD + col * (TROPHY_W + PAD)
    y = PAD + row * (TROPHY_H + PAD)
    elements += trophy_svg(x, y, cat, grade, label, pts)

svg = f"""<svg width="{SVG_W}" height="{SVG_H}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{SVG_W}" height="{SVG_H}" fill="{bg}"/>
  {elements}
</svg>"""

os.makedirs("assets", exist_ok=True)
with open("assets/trophies.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Generated assets/trophies.svg ({SVG_W}x{SVG_H})")
