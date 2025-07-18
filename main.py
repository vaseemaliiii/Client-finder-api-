from flask import Flask, request, jsonify
from serpapi import GoogleSearch
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Client Finder API is running"

@app.route('/search')
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Query required"}), 400

    params = {
        "engine": "google",
        "q": query,
        "api_key": os.environ.get("SERPAPI_KEY")
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    return jsonify(results)

if __name__ == '__main__':
    app.run()
