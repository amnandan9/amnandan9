import os

color = "#68b587"
bg_color = "#0a0f0b"
title_color = "#abd200"

# 1. Left to Right scrolling text, runs once
run_right = f"""<svg width="800" height="40" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="40" fill="{bg_color}" />
  <text y="25" fill="{title_color}" font-family="monospace" font-size="20" font-weight="bold">
    <animate attributeName="x" from="-300" to="800" dur="5s" repeatCount="1" fill="freeze" />
    System Initialized...
  </text>
</svg>"""

# 2. Right to Left scrolling text, runs once
run_left = f"""<svg width="800" height="40" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="40" fill="{bg_color}" />
  <text y="25" fill="{title_color}" font-family="monospace" font-size="20" font-weight="bold">
    <animate attributeName="x" from="800" to="-300" dur="5s" repeatCount="1" fill="freeze" />
    Hi, I'm Nandan A M
  </text>
</svg>"""

# 3. Bio text in SVG to force color matching
bio = f"""<svg width="800" height="280" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="280" fill="{bg_color}" />
  <text x="20" y="30" fill="{title_color}" font-family="monospace" font-size="18" font-weight="bold">// BIO_DATA</text>
  <text x="20" y="70" fill="{color}" font-family="monospace" font-size="14">I am a passionate developer who loves turning ideas into impactful digital</text>
  <text x="20" y="90" fill="{color}" font-family="monospace" font-size="14">solutions. I work across web, mobile, and AI-driven systems, focusing on</text>
  <text x="20" y="110" fill="{color}" font-family="monospace" font-size="14">building secure, efficient, and scalable applications.</text>
  
  <text x="20" y="150" fill="{color}" font-family="monospace" font-size="14">- I've hands-on experience with Django, React, Laravel, MySQL, Git, Docker.</text>
  <text x="20" y="170" fill="{color}" font-family="monospace" font-size="14">- Currently exploring AI-based projects like handwriting recognition.</text>
  <text x="20" y="190" fill="{color}" font-family="monospace" font-size="14">- Actively building full-stack &amp; security-focused projects.</text>
  <text x="20" y="210" fill="{color}" font-family="monospace" font-size="14">- Outside coding, I enjoy tech challenges, hackathons, logic puzzles.</text>
  
  <text x="20" y="250" fill="{title_color}" font-family="monospace" font-size="14" font-style="italic">Always learning, always building, always curious.</text>
</svg>"""

os.makedirs("assets", exist_ok=True)
with open("assets/run_right.svg", "w") as f: f.write(run_right)
with open("assets/run_left.svg", "w") as f: f.write(run_left)
with open("assets/bio.svg", "w") as f: f.write(bio)
