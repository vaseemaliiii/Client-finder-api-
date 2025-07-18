from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from serpapi import GoogleSearch
import os

app = FastAPI()

# Allow all origins (frontend ke liye CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search/")
def search_clients(query: str):
    params = {
        "q": query,
        "engine": "google",
        "api_key": os.getenv("SERPAPI_KEY")
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results
