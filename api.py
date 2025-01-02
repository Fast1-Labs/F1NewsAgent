from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from news_agent import get_f1_news

app = FastAPI(
    title="F1 News API", description="Fetches the latest F1 news.", version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the F1 News API"}


@app.get("/news", response_class=JSONResponse)
def fetch_news():
    try:
        news = get_f1_news()
        if not news:
            raise HTTPException(status_code=404, detail="No news found.")
        return {"status": "success", "news": news}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
