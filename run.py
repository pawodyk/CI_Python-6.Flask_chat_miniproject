import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "temporaryrandomstring123"
messages = []

def add_messages(username, message):
    """ adds the user and the message to the list """
    timestamp = datetime.now().strftime('%H:%M:%S')
    messages.append("({}) {}: {}".format(timestamp, username, message))
    

def get_all_messages():
    """ return all messages, formated on seperate lines"""
    return "<br>".join(messages)

@app.route("/", methods=["GET", "POST"])
def index():
    """ Main page with instructions """
    if request.method == "POST":
        session["username"] = request.form["username"]
        
    if "username" in session:
        print("User " +  session["username"] + "entered chat")
        return redirect("/" + session["username"])
        
        
    return render_template("index.html")


@app.route("/<username>")
def user(username):
    """ Display chat messages """
    return "<h1>Welcome, {0}</h1><hr> {1}".format(username, get_all_messages())


@app.route("/<username>/<message>")
def send_message(username, message):
    """ Create a new message and redirect back to the chat page """
    add_messages(username, message)
    return redirect("/" + username)
    

app.run(host=os.getenv('IP', '127.0.0.1'), port=os.getenv('PORT', 5500), debug=True)