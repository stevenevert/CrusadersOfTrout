from flask import Flask, request, jsonify
from processing.predict import predict

app = Flask(__name__)


@app.route('/api', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        json = request.get_json()
        results = predict(json)
        return jsonify(results)

    return 'This is a super basic flask api'


if __name__ == "__main__":
    app.run()