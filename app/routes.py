# main app code
# By Mahima Arya

# things to do
# 1. make form template nicer ✅
#     - use bootstrap
#     - explain what the page is for
#     - add a title
# 2. make results page ✅
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
#     - explain future work (db)
#     - desc of actual vision(chrome extension)

from app import app
from flask import Flask, request, render_template
import json
import requests
import re
import csv

@app.route('/')
def form():
    # initial screen should have a form for a YT URL submission
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    # when the URL is submitted, allow the user to review the comments
    URL = request.form['text']
    try:
        # except is triggered when there isn't a valid URL
        html = requests.get(URL).text
        # except is triggered when the URL isn't for a YT video
        vidTitle = getVidTitle(html)
        channelName = getChannel(html)
        comments = getComments()
    except:
        # change to in-line check that it's a valid YouTube link
        return render_template('error.html')
    return render_template('review.html', vidTitle = vidTitle, 
                            channelName = channelName, comments = comments)

def getVidTitle(html):
    # uses regex to find the video title
    result = re.search("""<span id="eow-title" class="watch-title" dir="ltr" title="(.*)">""", html)
    return(result.group(1))

def getChannel(html):
    # uses regex to find the channel name
    result = re.search("""<span class="stat attribution"><span class="" >(.*)</span></span>""", html)
    return(result.group(1))

def make2DListFromCSV(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data[1:] # skip the header row

def getComments():
    # comments are not included in the HTML request
    # using the YouTube API to get comment data requires approval in advance
    # YT API info: https://developers.google.com/youtube/v3/quickstart/python
    # for the purposes of an mvp, a csv from kaggle is being hardcoded in
    # (https://www.kaggle.com/datasnaek/youtube#UScomments.csv)
    comments = make2DListFromCSV('UScomments.csv')[:10] # cutting off at 10 for demo
    return comments







