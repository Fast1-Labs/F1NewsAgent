import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

F1_NEWS_URLS = [
    "https://www.formula1.com/en/latest/all.html",
    "https://www.motorsport.com/f1/news/",
]
