# Flask getting started documentation: https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask
from markupsafe import escape
from flask import render_template
app = Flask(__name__)

# using decorators to define routes
# decorators are a way to add additional functionality to functions
@app.route('/') # / means root of the website mywebsite.com/ etc
def hello_world():
    return '<h1>Hello, World!</h1><p>Congrats Python course students!</p>'

# let's add another route at base level
@app.route('/<anything>')
def anything(anything):
    return f'Aha!, {escape(anything)}!'

# let's add greet route
@app.route('/greet/<name>')
def greet(name):
    # here we could get data from some database or other source
    return f'Hello, {escape(name)}!' # remember we do not trust users :)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f"Hello User <strong>{escape(username)}</strong>" # remember we do not trust users :)
    # return 'User %s' % escape(username)

# let's use some templates

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    # so the incoming name will be passed to the template as person
    return render_template('hello.html', person=name)


app.run(host='0.0.0.0', port=8080)

    

