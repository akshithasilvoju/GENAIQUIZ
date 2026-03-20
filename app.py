from flask import Flask, request, jsonify, render_template
import requests
import json
import re
import os

app = Flask(__name__)


API_KEY = "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"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generateQuiz", methods=["POST"])
def generate_quiz():

    data = request.get_json()

    topic = data.get("topic")
    difficulty = data.get("difficulty")
    num = data.get("num")

    prompt = f"""
Generate {num} {difficulty} multiple choice quiz questions about {topic}.

Return ONLY JSON in this format:

[
{{
"question": "question text",
"options": ["option1","option2","option3","option4"],
"answer": "option1"
}}
]
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/llama-3-8b-instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    result = response.json()

    text = result["choices"][0]["message"]["content"]

    # Extract JSON safely
    match = re.search(r"\[.*\]", text, re.DOTALL)

    if match:
        quiz = json.loads(match.group())
        return jsonify(quiz)
    else:
        return jsonify({"error": "AI did not return valid JSON", "raw": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)