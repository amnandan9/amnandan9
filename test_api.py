import urllib.request
import urllib.error

url = "https://github-readme-stats.vercel.app/api?username=amnandan9&theme=merko"

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    data = response.read().decode('utf-8')
    print("SUCCESS, size:", len(data))
    with open("assets/debug.svg", "w", encoding="utf-8") as f:
        f.write(data)
except urllib.error.URLError as e:
    print(f"FAILED: {e}")
except Exception as e:
    print(f"ERROR: {e}")
