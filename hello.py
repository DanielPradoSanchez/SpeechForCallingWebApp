import os
from flask import Flask
import twilio.twiml
import praw


app = Flask(__name__)

@app.route('/')
def hello():
    """Respond to incoming requests."""
    #myTest = praw.Reddit('myTest1')
	#theContent = myTest.get_front_page(limit = 2)
	#theList = [str(x) for x in theContent]
	theList = ['hello']
    resp = twilio.twiml.Response()
    resp.say("Hello Monkey")
    #resp.say(theList[0])
 
    return str(resp)