import openai
from dotenv import load_dotenv

load_dotenv()


def fetch_f1_news():
    try:
        print("Attempting to fetching F1 news...")
        response = openai.chat.completions.create(
            model="chatgpt-4o-latest",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert Formula 1 news reporter. "
                        "Your task is to provide up-to-date F1 news."
                        "Each news item should include a title, description, and an image URL "
                        "relevant to the news. The description should summarize the news in 1-2 sentences."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        "Provide 3-10 Formula 1 news highlights. "
                        "Each item should have a title, description, and image URL."
                    ),
                },
            ],
            max_tokens=300,
        )
        news = response.choices[0].message.content
        print("News fetched successfully!")
        return news
    except Exception as e:
        print(f"Error fetching f1 news {e}")
        return default_f1_news()


def default_f1_news():
    return [
        {
            "title": "Max Verstappen Wins Abu Dhabi GP",
            "description": "Max Verstappen clinches another victory, dominating the 2023 season.",
            "image": "https://example.com/verstappen.jpg",
        },
        {
            "title": "Ferrari Prepares Major Upgrades",
            "description": "Ferrari plans to bring significant updates for the next season.",
            "image": "https://example.com/ferrari.jpg",
        },
        {
            "title": "Lewis Hamilton Extends Mercedes Contract",
            "description": "Lewis Hamilton signs a new multi-year deal with Mercedes.",
            "image": "https://example.com/hamilton.jpg",
        },
    ]


def get_f1_news():
    news = fetch_f1_news()
    return news


if __name__ == "__main__":
    print("Fetching F1 news...")
    news = get_f1_news()
    print("\n=== F1 News Highlights ===\n")
    print(news)
