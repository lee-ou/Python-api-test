from flask import Flask

app = Flask(__name__)


@app.route(methods=["GET"])
def mock_api():
    pass


if __name__ == '__main__':
    app.run(debug=True)
