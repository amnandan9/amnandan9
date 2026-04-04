import urllib.request

urls = [
    "https://github-readme-stats.anuraghazra1.vercel.app/api?username=amnandan9",
    "https://readme-stats-service-endpoints.vercel.app/api?username=amnandan9",
    "https://github-readme-stats-git-masterrstaa-rickstaa.vercel.app/api?username=amnandan9",
    "https://streak-stats.demolab.com?user=amnandan9&theme=merko"
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        print("SUCCESS:", url)
    except Exception as e:
        print("FAIL:", url, "->", e)
