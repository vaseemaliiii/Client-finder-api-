from flask import Flask, request, jsonify
import os
from serpapi import GoogleSearch

app = Flask(__name__)

@app.route('/')
def home():
    return "Client Finder API is running!"

@app.route('/find-clients')
def find_clients():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    api_key = os.getenv("SERP_API_KEY")  # Key is read from environment variable

    if not api_key:
        return jsonify({"error": "SERP_API_KEY is not set"}), 500

    search = GoogleSearch({
        "q": query,
        "location": "India",
        "hl": "en",
        "gl": "in",
        "api_key": api_key
    })

    results = search.get_dict()

    # Only return organic search results
    return jsonify(results.get("organic_results", []))

if __name__ == '__main__':
    app.run(debug=True)
