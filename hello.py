#
#   A web app written with Flask and Praw. This web app
#   displays the title of the top content on the front page
#   of Reddit and a name. This web app is used for the calling 
#   web app TwilCall which requires an xml format for the speech
#   of the call
#

import os
from flask import Flask
import twilio.twiml
import praw

app = Flask(__name__)

# Setting up the name to be said and extracting the title
# of the top content on Reddit
myName = 'Daniel Prado'
reddit = praw.Reddit('danielprado')
theContent = reddit.get_front_page(limit = 1)
#listOfContent = [str(x.title) for x in theContent]
#topContentTitle = listOfContent[0]
topContentTitle = 'The title'

@app.route("/", methods=['GET', 'POST'])
def hello():
    # Respond to incoming requests
    resp = twilio.twiml.Response()
    resp.say('My name is ' + myName)
    resp.say('The top content on Reddit right now is ' + topContentTitle)
    return str(resp)