import openai

from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def summarize_article(title, content):
    prompt = f"Summarize the following F1 news article:\n\nTitle: {title}\nContent: {content}\n\nSummary:"
    response = openai.completions.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.5,
    )
    return response.choices[0].text.strip()


def categorize_article(summary):
    prompt = f"Categorize the following F1 news summary into one of these categories: Race Results, Driver News, Team Updates, Technology Updates.\n\nSummary: {summary}\n\nCategory:"
    response = openai.completions.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=20,
        temperature=0.3,
    )
    return response.choices[0].text.strip()
