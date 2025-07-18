from fastapi import FastAPI
from serpapi.google_search import GoogleSearch
import os

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Client Finder API is running ✅"}

@app.get("/search/")
def search(query: str):
    search = GoogleSearch({
        "q": query,
        "engine": "google",
        "api_key": os.getenv("SERPAPI_KEY")
    })
    result = search.get_dict()
    return result
