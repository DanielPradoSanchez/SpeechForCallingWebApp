import os
from flask import Flask
import twilio.twiml

app = Flask(__name__)

@app.route('/')
def hello():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("Hello Monkey")
 
    return str(resp)