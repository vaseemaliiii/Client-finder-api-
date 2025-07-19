from fastapi import FastAPI
from pydantic import BaseModel
from serpapi import GoogleSearch
import os

app = FastAPI()

class Query(BaseModel):
    search_query: str

@app.post("/find_client")
def find_client(data: Query):
    params = {
        "engine": "google",
        "q": data.search_query,
        "api_key": os.getenv("SERPAPI_KEY"),
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    return {"results": results.get("organic_results", [])}
