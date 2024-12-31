from fastapi import FastAPI

from news_agent import get_f1_news

app = FastAPI()


@app.get("/f1-news")
def fetch_news():
    news = get_f1_news()
    return {"news": news}
