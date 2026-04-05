import os
import urllib.request

def download(url, filename):
    print(f"Downloading {filename}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response, open(filename, 'wb') as out_file:
            out_file.write(response.read())
    except Exception as e:
        print(f"Failed to fetch {filename}: {e}")

os.makedirs("assets", exist_ok=True)

download("https://github-readme-stats.anuraghazra1.vercel.app/api?username=amnandan9&show_icons=true&title_color=abd200&text_color=68b587&icon_color=b7d364&bg_color=0a0f0b&hide_border=true&cache_seconds=86400", "assets/github_stats.svg")
download("https://streak-stats.demolab.com?user=amnandan9&background=0a0f0b&stroke=b7d364&ring=abd200&fire=abd200&currStreakNum=68b587&sideNums=68b587&currStreakLabel=68b587&sideLabels=68b587&dates=68b587&hide_border=true&cache_seconds=86400", "assets/streak_stats.svg")
download("https://github-profile-trophy.vercel.app/?username=amnandan9&theme=merko&no-frame=true&no-bg=true&margin-w=15", "assets/trophies.svg")
download("https://github-readme-activity-graph.vercel.app/graph?username=amnandan9&bg_color=0a0f0b&color=68b587&line=abd200&point=b7d364&area=true&hide_border=true&cache_seconds=86400", "assets/activity.svg")
download("https://github-readme-stats.anuraghazra1.vercel.app/api/top-langs/?username=amnandan9&layout=compact&title_color=abd200&text_color=68b587&icon_color=b7d364&bg_color=0a0f0b&hide_border=true&cache_seconds=86400", "assets/top_langs.svg")

print("Done proxying SVGs.")
