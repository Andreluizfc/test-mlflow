from flask import Flask, request, jsonify
import predict_model

application = Flask(__name__)

@application.route("/health", methods=["POST"])
def health():
    return jsonify({"response": "I'm alive"})

@application.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()
    result = predict_model.predict(data['data'])

    return jsonify({"response": result.tolist()})


if __name__ == "__main__":
    application.run(threaded=True, host="0.0.0.0", port=8080)
