from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def hello():
    outFile = {'Tittle' : "Simon Game", 'msg' : "Hello World!"}
    outFile = json.dumps(outFile)
    return json.loads(outFile)