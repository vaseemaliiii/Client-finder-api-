from flask import Flask, request, jsonify
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

    # ✅ Your SerpAPI Key (safe only for personal use)
    api_key = "09e036563bdb7e5f1959c16b51230c1e0933090d69cbd337b24f65189111df34"

    # 🔍 SerpAPI Search
    search = GoogleSearch({
        "q": query,
        "location": "India",
        "hl": "en",
        "gl": "in",
        "api_key": api_key
    })

    results = search.get_dict()

    # ✅ Return only organic search results
    return jsonify(results.get("organic_results", []))

if __name__ == '__main__':
    app.run(debug=True)
