from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
@app.route("/index")
def home():
     return render_template("index.html")


@app.route("/SayHello/YaserAlNajjar")
def YaserAlNajjar():
	
	return "Hello YaserAlNajjar"



app.run()
