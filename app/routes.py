# main app code

# things to do
# 1. make form template nicer
#     - use bootstrap
#     - explain what the page is for
#     - add a title
# 2. make results page
#     - show the vid title and channel name at the top
#     - show comments and have a button to submit to trust lab
#     - make comments that are chosen disappear
# 3. set up a trust lab db
#     - use pymongo?
#     - add comments that are chosen to the db
# 4. update readme
#     - explain the subtask i chose
#     - explain what installs need to be done
#     - explain how to run the code
#     - explain future work

from app import app
from flask import Flask, request, render_template
import json
import requests
import re
import csv
import pandas as pd

@app.route('/')
@app.route('/index')
def form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    URL = request.form['text']
    html = requests.get(URL).text
    try:
        vidTitle = getVidTitle(html)
    except:
        return '''
            <html>
                <head>
                    <title>Home Page - Microblog</title>
                </head>
                <body>
                    <h1>Please hit the back button and input a valid YouTube URL.</h1>
                </body>
            </html>''' # change to in-line check that it's a valid YouTube link
    channelName = getChannel(html)
    comments = getComments()
    # turn this into a template
    return render_template('analysis.html') # pass in the comments DF

def getVidTitle(html):
    # uses regex to find the video title
    result = re.search("""<span id="eow-title" class="watch-title" dir="ltr" title="(.*)">""", html)
    return(result.group(1))

def getChannel(html):
    # uses regex to find the channel name
    result = re.search("""<span class="stat attribution"><span class="" >(.*)</span></span>""", html)
    return(result.group(1))

def makeDataFrame(filename):
    data = pd.read_csv(filename)
    df = pd.DataFrame(data)
    return df

def getComments():
    # comments are not included in the HTML request
    # using the YouTube API to get comment data requires approval in advance
    # for the purposes of an mvp, a csv from kaggle is being hardcoded in
    # (https://www.kaggle.com/datasnaek/youtube#UScomments.csv)
    commentsDf = makeDataFrame('UScomments.csv')
    return commentsDf







