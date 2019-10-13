from flask import Flask, request
import json
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    outFile = {'Tittle' : "Simon Game", 'msg' : "Hello World!"}
    return json.dumps(outFile)

@app.route('/Simon/generateGame')
def generateRandomSimonGame():
    colors = np.random.randint(4,size=10)
    outFile = {"round" : 1, "sequence" : colors.tolist()}
    return json.dumps(outFile)


