from flask import Flask, render_template, request
import requests
import datetime
import sys

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/userlogin")
def userlogin():
    return render_template('userlogin.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
