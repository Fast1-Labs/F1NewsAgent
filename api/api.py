from fastapi import FastAPI

from api.news_agent import get_f1_news

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the F1 News API"}


@app.get("/news")
def fetch_news():
    news = get_f1_news()
    return {"news": news}
