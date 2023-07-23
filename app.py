from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>I hope you enjoyed a lot and Hope you are doing well</h1>'
