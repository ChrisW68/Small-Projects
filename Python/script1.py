# Import Flask class object from flask library
from flask import Flask, render_template


app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

if __name__=="main":
    app.run(host='0.0.0.0')
