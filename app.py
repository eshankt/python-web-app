from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route("/")
def home():     
    return"<h1><center>Hello, From ME!<img src='https://media.heartlandtv.com/images/Pool1.PNG' align='middle'></h1></center>"

    