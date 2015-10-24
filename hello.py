import os
from flask import Flask
import twilio.twiml
import praw

myTest = praw.Reddit('myTest1')
theContent = myTest.get_front_page(limit = 2)
theList = [str(x) for x in theContent]
print(theList[0])

app = Flask(__name__)

@app.route('/')
def hello():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("Hello Monkey") 
    return str(resp)