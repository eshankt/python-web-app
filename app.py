from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1><center>Hello, from AZURE WEB APP </h1></center>"
