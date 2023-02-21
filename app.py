from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'juste pour voir comment ça marche-20-02-2023-1618'
