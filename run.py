import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"
    

app.run(host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', 8080), debug=True)