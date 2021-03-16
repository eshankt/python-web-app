from flask import Flask
from flask import render_template
app = Flask(__name__)
#@app.route("/")
def home():
    #return "Hello, Flask!"
    #<img src="https://ih1.redbubble.net/image.1220724104.4638/farp,small,wall_texture,product,750x1000.u10.jpg" align="middle" />
    return render_template(
        "hello_there.html"
    )