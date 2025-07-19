from fastapi import FastAPI, Query
from serpapi import GoogleSearch
import os

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Client Finder API is running!"}

@app.get("/search/")
def search(query: str = Query(...)):
    params = {
        "engine": "google",
        "q": query,
        "api_key": os.getenv("SERPAPI_KEY")
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results
