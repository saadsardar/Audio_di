from flask import Flask, jsonify, request
from speaker import getAudio


app = Flask(__name__)

@app.route("/audio", methods=["POST"])
def predict():
    predictions = getAudio(request)

    return jsonify(predictions)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)