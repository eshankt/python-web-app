from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1><center>Hello there, This is  running on Azure</center></h1>"
    
    

