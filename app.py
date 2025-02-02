from flask import Flask, request, jsonify, render_template
import json
import random

app = Flask(__name__)

# Load JSON data
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message", "").strip().lower()

    for intent in data["intents"]:
        if user_message in [pattern.lower() for pattern in intent["patterns"]]:
            return jsonify({"response": random.choice(intent["responses"])})  # Return random response

    return jsonify({"response": "I'm here to listen. Tell me more."})  # Default response

if __name__ == "__main__":
    app.run(debug=True)
