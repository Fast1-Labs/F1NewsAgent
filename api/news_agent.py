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
                    "content": "You are a sports news reporter specializing in Formula 1.",
                },
                {
                    "role": "user",
                    "content": "Provide the latest Formula 1 news highlights for today.",
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
    return """
    1. Max Verstappen clinches another victory at the Abu Dhabi GP.
    2. Ferrari shows promise with Charles Leclerc leading the charge.
    3. Mercedes prepares major upgrades for the next F1 season.
    4. Aston Martin's Fernando Alonso reflects on his remarkable season.
    """


def get_f1_news():
    news = fetch_f1_news()
    return news


if __name__ == "__main__":
    print("Fetching F1 news...")
    news = get_f1_news()
    print("\n=== F1 News Highlights ===\n")
    print(news)
