from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'juste pour voir comment ça marche'
