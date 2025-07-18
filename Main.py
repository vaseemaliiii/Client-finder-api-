from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Client Finder API is Running!"

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get("query")

    if not query:
        return jsonify({"error": "❌ Query not provided"}), 400

    serpapi_key = "ca85c7d5812eec558fb3efda3df5b7601045f22c897f0297a28900b1e5fc72f1"
    params = {
        "engine": "bing",
        "q": query,
        "api_key": serpapi_key
    }

    response = requests.get("https://serpapi.com/search.json", params=params)

    if response.status_code != 200:
        return jsonify({"error": "❌ Failed to fetch data from SerpAPI"}), 500

    results = response.json().get("organic_results", [])

    return jsonify([
        {
            "title": r.get("title"),
            "link": r.get("link"),
            "snippet": r.get("snippet")
        } for r in results
    ])

if __name__ == '__main__':
    app.run()
