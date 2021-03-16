from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route("/")
def home():     
    return"<h1><center>Hello, From ME! <img src='https://media.heartlandtv.com/images/Pool1.PNG' width='100' height='200'></h1></center>"

    