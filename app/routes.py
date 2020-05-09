from app import app
from flask import Flask, request, render_template

@app.route('/')
@app.route('/index')
def form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    print(request.form)
    text = request.form['text']
    processed_text = text.upper()
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + processed_text + '''!</h1>
    </body>
</html>'''