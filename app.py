from flask import Flask,render_template,request

app = Flask(__name__,template_folder='templates')

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/search")
def login1():
    return render_template("search.html")