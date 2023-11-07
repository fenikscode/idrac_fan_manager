from flask import Flask, redirect, url_for
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run('0.0.0.0', 8080, debug=1)