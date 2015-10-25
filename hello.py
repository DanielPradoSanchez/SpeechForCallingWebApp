import os
from flask import Flask
import twilio.twiml
import praw

myTest = praw.Reddit('myTest1')
theContent = myTest.get_front_page(limit = 2)
theList = [x.title for x in theContent]

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("Hello Monkey")
    return str(resp)