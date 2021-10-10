from os import environ
from flask import Flask, render_template, request
import datetime
import json

from you_are_real.data import HerokuDatabase

app = Flask(__name__)

@app.route("/")
def main_page(): 
    return render_template("index.html")

ALWAYS_OPEN = True

db = HerokuDatabase(environ["DATABASE_URL"])

def is_open(t_open, t_close, t_check):
    is_open_day = (t_check >= t_open and t_check <= t_close)
    # Open hours might straddle midnight
    is_open_night = (t_close < t_open and (t_check < t_close or t_check > t_open))
    return is_open_day or is_open_night


@app.route("/content", methods=["POST"])
def get_content():
    request_data = request.get_json()
    hour = datetime.timedelta(hours=int(request_data["hour"]))
    open_time = datetime.timedelta(hours=8)
    closed_time = datetime.timedelta(hours=16)
    if is_open(open_time, closed_time, hour):
        result = {
            "css_file": "static/open.css",
            "body" : render_template("open.html", question="do you think you are real"),
            "title": "first prise"
        }
    else:
        result = {
            "css_file": "static/closed.css",
            "body" : render_template("closed.html"),
            "title": "closed"
        }
    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response


    
@app.route("/update", methods=["POST"])
def get_response():
    answer = request.form["answer"]
    db.add_answer(answer)
    return ""
