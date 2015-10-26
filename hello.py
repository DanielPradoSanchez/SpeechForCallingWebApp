import os
from flask import Flask
import twilio.twiml
import praw

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    #resp.say('My name is ' + myName)
    #resp.say('The top content on Reddit right now is ' + topContentTitle)
    resp.say('What is up duuuuuuuuuude')
    return str(resp)