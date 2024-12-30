from config import F1_NEWS_URLS
from scraper import scrape_news
from summarizer import categorize_article, summarize_article


def main():
    all_articles = []

    for url in F1_NEWS_URLS:
        articles = scrape_news(url)
        all_articles.extend(articles)

    processed_articles = []
    for article in all_articles:
        try:
            summary = summarize_article(article["title"], article.get("summary", ""))
            category = categorize_article(summary)
            processed_articles.append(
                {
                    "title": article["title"],
                    "link": article["link"],
                    "summary": summary,
                    "category": category,
                }
            )
        except Exception as e:
            print(f"Error processing article: {article['title']}. Error: {e}")

    for article in processed_articles:
        print(f"Title: {article['title']}")
        print(f"Category: {article['category']}")
        print(f"Summary: {article['summary']}")
        print(f"Link: {article['link']}\n")


if __name__ == "__main__":
    main()
