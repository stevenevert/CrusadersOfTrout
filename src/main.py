from flask import Flask, request
from processing.predict import Pitcher, Hitter

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        result = bar(something)
        return 'This is a super basic flask api'


if __name__ == "__main__":
    app.run()