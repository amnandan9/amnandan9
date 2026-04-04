import os

bg_color = "#0a0f0b"
title_color = "#abd200"
text_color = "#68b587"

def create_sliding_svg(filename, text, direction="right", color=title_color, font_size=20):
    # direction "right" means it moves from left to right, ending in center
    # direction "left" means it moves from right to left, ending in center
    
    start_x = "-200" if direction == "right" else "1000"
    
    svg = f"""<svg width="800" height="40" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="40" fill="{bg_color}" />
  <text y="25" fill="{color}" font-family="monospace" font-size="{font_size}" font-weight="bold" text-anchor="middle">
    <animate attributeName="x" from="{start_x}" to="400" dur="2s" repeatCount="1" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1" />
    {text}
  </text>
</svg>"""
    
    with open(f"assets/{filename}", "w") as f:
        f.write(svg)

os.makedirs("assets", exist_ok=True)

# 1. Main Headers
create_sliding_svg("header_left.svg", "System Initialized...", "right")
create_sliding_svg("header_right.svg", "Hi, I'm Nandan A M", "left")

# 2. Tech Header
create_sliding_svg("tech_header.svg", "// SYSTEM_ASSETS: TECHNOLOGIES", "right")

# 3. Connection Header
create_sliding_svg("conn_header.svg", "// ESTABLISH_CONNECTION", "left")

# 4. Footer Headers
create_sliding_svg("footer_left.svg", "[ STATUS: ALWAYS LEARNING. ALWAYS BUILDING. ]", "right", color=text_color, font_size=16)
create_sliding_svg("footer_right.svg", "I love connecting with new people, feel free to say hi!", "left", color=text_color, font_size=16)

print("Generated all sliding headers in assets/!")
