from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# SerpAPI key from Render's Environment Variables
SERP_API_KEY = os.environ.get("SERP_API_KEY")

@app.route("/")
def home():
    return "Client Finder API is running!"

@app.route("/find-clients", methods=["GET"])
def find_clients():
    query = request.args.get("query")

    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    search_url = f"https://serpapi.com/search.json?q={query}&api_key={SERP_API_KEY}&engine=google"

    try:
        response = requests.get(search_url)
        data = response.json()
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
