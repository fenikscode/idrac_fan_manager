import threading as th
import time

from flask import Flask, redirect, url_for
from flask.templating import render_template

from redfish_request import make_query

CURRENT_FANS_SPEED = None

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def update_fans():
    while True:
        CURRENT_FANS_SPEED = make_query()
        print(CURRENT_FANS_SPEED)
        time.sleep(5)

if __name__ == "__main__":
    t1 = th.Thread(target=update_fans).start()
    app.run('0.0.0.0', 8080, debug=True)