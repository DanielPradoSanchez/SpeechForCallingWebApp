import os
from flask import Flask
import twilio.twiml
import praw

app = Flask(__name__)

myName = 'Daniel Prado'
reddit = praw.Reddit('danielprado')
theContent = reddit.get_front_page(limit = 1)
listOfContent = [str(x.title) for x in theContent]
topContentTitle = listOfContent[0]

@app.route("/", methods=['GET', 'POST'])
def hello():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say('My name is ' + myName)
    resp.say('The top content on Reddit right now is ' + topContentTitle)
    return str(resp)