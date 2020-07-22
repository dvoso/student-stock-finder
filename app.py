# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/result',  methods=['GET','POST'])
def result():
    if request.method == "GET":
        return render_template('results.html')
    else:
        return render_template('index.html')