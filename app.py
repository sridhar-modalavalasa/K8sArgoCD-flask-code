from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Thank you for staying till end</h1>'
