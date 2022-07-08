from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Main page'

@app.route('/login')
def login():
    return 'Login page'

@app.route('/tracks')
def tracks():
    return 'My tracks'