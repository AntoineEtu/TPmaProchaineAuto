from flask import Flask, render_template, request, redirect
import requests
import datetime
import sys

app = Flask(__name__)

username = ""

@app.route("/")
def index():
    return render_template('index.html', username = username)

@app.route("/userlogin", methods=["GET","POST"])
def userlogin():
    if request.method == "POST":
        req = request.form
        username = req['username']
        print(username)
        redirect(request.url)
        if username == "client":
            return render_template('vehiculeslist.html', username = username)
        if username == "vendeur":
            return render_template('dashboard.html', username = username)
        if (username != 'vendeur' and username != "client"):
            return render_template('authenticationfailed')
    return render_template('userlogin.html')

@app.route("/vehicules")
def vehicules():
    return render_template('vehiculeslist.html', username = username)

@app.route("/visiteVirtuelle")
def visiteVirtuelle():
    return render_template('visiteVirtuelle.html', username = username)

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html', username = username)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
