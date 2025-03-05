from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Securely load API Key from environment variables
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

@app.route('/claude-api', methods=['POST'])
def proxy_request():
    if not CLAUDE_API_KEY:
        return jsonify({"error": "API key missing"}), 500

    data = request.json
    headers = {
        "Content-Type": "application/json",
        "x-api-key": CLAUDE_API_KEY,
        "anthropic-version": "2023-06-01"
    }

    response = requests.post("https://api.anthropic.com/v1/messages", json=data, headers=headers)
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
