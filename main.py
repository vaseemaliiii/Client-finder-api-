from fastapi import FastAPI, Query
from serpapi import GoogleSearch
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

@app.get("/search/")
def search_clients(query: str = Query(...)):
    params = {
        "engine": "google",
        "q": query,
        "api_key": os.getenv("SERPAPI_KEY"),
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results
