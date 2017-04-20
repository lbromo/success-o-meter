from flask import Flask, jsonify, request
from threading import Timer
import json

app = Flask(__name__)

success = 0

def dec_lort():
    global success
    success = success - 1
    if success < 0: success = 0
    Timer(60, dec_lort).start()

@app.route('/sink', methods=['POST'])
def on_push():
    global success
    try:
        payload = json.loads(request.data)
        for commit in payload['commits']:
            success = success + 5
            print(
                "AUTHOR: {0} | MSG: {1}".format(
                    commit['author'], commit['message']
                )
            )
    except:
        pass
    return "FUCK"

@app.route('/out')
def on_poll():
    global success
    return str(success)

if __name__ == '__main__':
    Timer(60, dec_lort).start()
    app.run(host='0.0.0.0', port=8000)