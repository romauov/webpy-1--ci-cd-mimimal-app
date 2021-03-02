from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    time = datetime.now()
    return f'Hello, Netology! It\'s {time}'