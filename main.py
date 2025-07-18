from fastapi import FastAPI
from serpapi import GoogleSearch
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Client Finder API is running"}

@app.get("/search/")
def search_clients(query: str):
    params = {
        "engine": "google",
        "q": query,
        "api_key": os.getenv("SERPAPI_KEY")
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results
