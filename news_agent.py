import json

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()


def fetch_f1_news():
    try:
        print("Fetching F1 news...")
        url = "https://www.autosport.com/f1/news/"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        articles = []
        news_items = soup.select("article")

        for item in news_items[:10]:
            title = (
                item.find("h2").get_text(strip=True) if item.find("h2") else "No Title"
            )
            description = (
                item.find("p").get_text(strip=True)
                if item.find("p")
                else "No Description"
            )
            image_url = item.find("img")["src"] if item.find("img") else "No Image URL"

            articles.append(
                {
                    "title": title,
                    "description": description,
                    "image_url": image_url,
                }
            )

        print("F1 news fetched successfully!")
        return articles

    except Exception as e:
        print(f"Error fetching F1 news: {e}")
        return default_f1_news()


def default_f1_news():
    return [
        {
            "title": "Max Verstappen Wins Abu Dhabi GP",
            "description": "Max Verstappen clinches another victory, dominating the 2023 season.",
            "image_url": "https://example.com/verstappen.jpg",
        },
        {
            "title": "Ferrari Prepares Major Upgrades",
            "description": "Ferrari plans to bring significant updates for the next season.",
            "image_url": "https://example.com/ferrari.jpg",
        },
        {
            "title": "Lewis Hamilton Extends Mercedes Contract",
            "description": "Lewis Hamilton signs a new multi-year deal with Mercedes.",
            "image_url": "https://example.com/hamilton.jpg",
        },
    ]


def get_f1_news():
    news = fetch_f1_news()
    return json.dumps(news, indent=2)


if __name__ == "__main__":
    print("Fetching F1 news...")
    news = get_f1_news()
    print("\n=== F1 News Highlights ===\n")
    print(news)
