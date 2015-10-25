import os
from flask import Flask
import twilio.twiml
import praw

name = 'Daniel Prado'
myTest = praw.Reddit('myTest1')
topContent = myTest.get_front_page(limit = 1)
listOfTopContentTitles = [x.title for x in theContent]
topContentTitle = listOfTopContentTitles[0]

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say('My name is Daniel Prado')
    #resp.say('The top content on Reddit today is: ' + topContentTitle)
    return str(resp)