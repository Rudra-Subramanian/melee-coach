from flask import Flask
from flask_cors import CORS
from comboparser import ACombo as cp
from comboparser import main_specific

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return {"data": "hello flask"}

@app.route('/<stage>/<characterPicked>/<charactersAgainst>/<minHits>/<slippiSource>')
def getCombos(stage, characterPicked, charactersAgainst, minHits, slippiSource):
    charactersAgainst = charactersAgainst.strip().split(',')
    allcombos, newComboList = main_specific(characterPicked, stage, int(minHits), charactersAgainst, slippiSource)
    return {"allcombos": [combo.__dict__ for combo in allcombos], "newComboList": [combo.__dict__ for combo in newComboList]}