import requests
from bs4 import BeautifulSoup


def scrape_news(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch news from {url}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    articles = []

    for article in soup.select("article"):
        title = (
            article.select_one("h3").get_text(strip=True)
            if article.select_one("h3")
            else None
        )
        link = article.select_one("a")["href"] if article.select_one("a") else None
        summary = (
            article.select_one("p").get_text(strip=True)
            if article.select_one("p")
            else None
        )

        if title and link:
            articles.append({"title": title, "link": link, "summary": summary})

    return articles
