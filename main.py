from flask import *
import json, time

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home_page():
    dataset = {'Page': 'Home', 'Message': 'Successfully loaded home page', 'Timestamp': time.time()}
    json_dump = json.dumps(dataset)

    return json_dump


@app.route('/user', methods = ['GET'])
def request_page():
    user = str(request.args.get('usr'))  # /user?usr=USER_NAME
    
    dataset = {'Page': 'Request', 'Message': 'Your username is ' + user, 'Timestamp': time.time()}
    json_dump = json.dumps(dataset)

    return json_dump


if __name__ == '__main__':
    app.run()