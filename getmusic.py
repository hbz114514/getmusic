import requests as reqs
import re
import flask
import json
import flask_cors
from gevent import pywsgi
import random


app = flask.Flask(__name__)
flask_cors.CORS(app)
ids = [502455381,524152942,558390968]

'''outer link:http://music.163.com/song/media/outer/url?id={musicid}.mp3'''

@app.route('/geturl')
def geturlbyid():
    i = random.randint(0, len(ids) - 1)
    params = {'url': f'http://music.163.com/song/media/outer/url?id={ids[i]}.mp3','id': ids[i]}
    return json.dumps(params, indent=1)

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('127.0.0.1', 9600), app)
    server.serve_forever()