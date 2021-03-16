from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route("/")
def home():     
    return"<h1><center>Hello, From ME! </h1></center><img src='https://media.heartlandtv.com/images/Pool1.PNG' width='300' height='300'>"

    