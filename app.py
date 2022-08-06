from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Starting Machine Learning Project. Ci/CD pipeline has been established"

if __name__ == "__main__":
    app.run(debug=True)