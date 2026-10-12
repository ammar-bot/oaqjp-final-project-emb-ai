from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/emotion_detector", methods=["POST"])
def detect_emotion():
    data = request.get_json()
    text = data.get("text", "")

    # Example response; replace with your emotion detector
    return jsonify({
        "text": text,
        "message": "Text received successfully"
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5005, debug=True)