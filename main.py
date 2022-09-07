from flask import *
import json, time
from drugDb import DrugDb

app = Flask(__name__)
db = DrugDb()

@app.route('/', methods = ['GET'])
def home_page():
    dataset = {'Page': 'Home', 'Message': 'Successfully loaded home page', 'Timestamp': time.time()}
    json_dump = json.dumps(dataset)
    return json_dump


@app.route('/allnames', methods = ['GET'])
def getAllNames():
    dataset = {'Names': db.getNames()}
    json_dump = json.dumps(dataset)
    return json_dump


@app.route('/drug', methods = ['GET'])
def getDrugInfo():
    drugName = str(request.args.get('name'))  # /drug?name=DRUG_NAME
    dataset = db.getDrug(drugName)
    json_dump = json.dumps(dataset)
    return json_dump


if __name__ == '__main__':
    app.run()