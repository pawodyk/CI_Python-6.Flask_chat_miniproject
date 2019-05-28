import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fallbacksecretvalue123")
chat = []


def add_message(username, message):
    """ adds the user, timestamp and the message to the dictonary and then adds it to message list """
    timestamp = datetime.now().strftime('%H:%M:%S')
    
    chat.append({"timestamp": timestamp, "username": username, "message": message})
    

@app.route("/", methods=["GET", "POST"])
def index():
    """ Main page with instructions """
    if request.method == "POST":
        session["username"] = request.form["username"]
        
    if "username" in session:
        print("User " +  session["username"] + " entered chat")
        return redirect(url_for("user", username=session["username"]))
        
    return render_template("index.html")


@app.route("/chat/<username>", methods = ["GET", "POST"])
def user(username):
    """ Allowes user to add and display chat messages """
    
    if request.method == "POST":
        print(session)
        print(request.form)
        
        if "username" in session:
            username = session["username"]
            message = request.form["message"]
            add_message(username, message)
            return redirect(url_for("user", username=username))
        else:    
            return redirect(url_for("index"))
    
    return render_template("chat.html", user=username, messages=chat)


app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', "5000")), debug=False)

#END OF APPLICATION