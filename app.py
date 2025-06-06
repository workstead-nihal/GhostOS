from flask import Flask

app = Flask(__name__)

from flask import render_template

@app.route('/')
def home(name=None):
    return render_template('home.html', person=name)