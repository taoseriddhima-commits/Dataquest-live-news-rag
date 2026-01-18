import os
import json
import time
import requests
from dotenv import load_dotenv

print("Starting news writer...")

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
print("API KEY loaded:", "YES" if NEWS_API_KEY else "NO")

def fetch_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "language": "en",
        "pageSize": 3,
        "apiKey": NEWS_API_KEY
    }

    print("Fetching news from API...")
    response = requests.get(url, params=params, timeout=10)

    print("Status code:", response.status_code)

    if response.status_code != 200:
        print("API response:", response.text)
        return []

    return response.json().get("articles", [])

while True:
    try:
        articles = fetch_news()
        print("Articles received:", len(articles))

        for i, article in enumerate(articles):
            data = {
                "title": article.get("title"),
                "content": article.get("description") or "",
                "source": article["source"]["name"]
            }

            filename = f"data/news_{int(time.time())}_{i}.json"
            with open(filename, "w") as f:
                json.dump(data, f)

            print(f"Wrote {filename}")
            time.sleep(2)

        time.sleep(10)

    except Exception as e:
        print("ERROR:", e)
        time.sleep(5)

