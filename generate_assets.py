import os

bg_color = "#0a0f0b"
title_color = "#abd200"
text_color = "#68b587"
icon_color = "#b7d364" # Brighter green for the footer

# Helper for sliding headers
def create_sliding_svg(filename, text, direction="right", color=title_color, font_size=20):
    start_x = "-200" if direction == "right" else "1000"
    svg = f"""<svg width="800" height="40" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="40" fill="{bg_color}" />
  <text y="25" fill="{color}" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="{font_size}" font-weight="bold" text-anchor="middle">
    <animate attributeName="x" from="{start_x}" to="400" dur="2s" repeatCount="1" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1" />
    {text}
  </text>
</svg>"""
    with open(f"assets/{filename}", "w", encoding="utf-8") as f:
        f.write(svg)

# Detailed Bio SVG mapping to github specific typography metrics
def create_bio_svg(filename):
    svg = f"""<svg width="800" height="240" xmlns="http://www.w3.org/2000/svg">
  <style>
    @keyframes slideIn {{
      0% {{ transform: translateY(20px); opacity: 0; }}
      100% {{ transform: translateY(0); opacity: 1; }}
    }}
    .line {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 14px; opacity: 0; animation: slideIn 1s ease-out forwards; }}
  </style>
  <rect width="800" height="240" fill="{bg_color}" />
  <text x="20" y="30" fill="{text_color}" class="line" style="animation-delay: 0.1s;">Hi, I'm Nandan A M, a passionate developer who loves turning ideas into impactful</text>
  <text x="20" y="50" fill="{text_color}" class="line" style="animation-delay: 0.2s;">digital solutions. I work across web, mobile, and AI-driven systems, focusing</text>
  <text x="20" y="70" fill="{text_color}" class="line" style="animation-delay: 0.3s;">on building secure, efficient, and scalable applications.</text>
  
  <text x="20" y="110" fill="{title_color}" class="line" font-weight="bold" style="animation-delay: 0.5s;">⚙️ I've hands-on experience with Django, React, Laravel, MySQL, Android Studio, Git, Docker.</text>
  <text x="20" y="130" fill="{title_color}" class="line" font-weight="bold" style="animation-delay: 0.7s;">🌱 Currently exploring AI-based projects like handwriting recognition.</text>
  <text x="20" y="150" fill="{title_color}" class="line" font-weight="bold" style="animation-delay: 0.9s;">🔭 Actively building full-stack &amp; security-focused projects.</text>
  <text x="20" y="170" fill="{title_color}" class="line" font-weight="bold" style="animation-delay: 1.1s;">🎮 Outside coding, I enjoy tech challenges, hackathons, logic puzzles.</text>
</svg>"""
    with open(f"assets/{filename}", "w", encoding="utf-8") as f:
        f.write(svg)

os.makedirs("assets", exist_ok=True)

print("Building Text Assets...")

create_sliding_svg("header_left.svg", "System Initialized...", "right")
create_sliding_svg("header_right.svg", "Hi, I'm Nandan A M", "left")
create_sliding_svg("tech_header.svg", "TECHNOLOGIES", "right")
create_sliding_svg("conn_header.svg", "CONNECTION", "left")
create_sliding_svg("footer_left.svg", "[ STATUS: ALWAYS LEARNING. ALWAYS BUILDING. ]", "right", color=icon_color, font_size=14)
create_sliding_svg("footer_right.svg", "I love connecting with new people, feel free to say hi!", "left", color=icon_color, font_size=14)
create_bio_svg("bio.svg")

print("Finished! All files saved to assets/ directory.")
