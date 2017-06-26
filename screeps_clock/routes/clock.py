from datetime import datetime
from screeps_clock import app
from screeps_clock.services import ticks
import json
from flask_cors import cross_origin
from screeps_clock.routes.decorators import httpresponse
from flask import render_template


# @httpresponse(expires=3, content_type='application/json')
@app.route('/time.js')
@cross_origin(origins="*", send_wildcard=True, methods="GET")
@httpresponse(expires=3, content_type='application/json')
def json_time():
    return json.dumps({
        'time': ticks.getCurrentTime(),
        'tick': ticks.getCurrentTick(),
    })


# @httpresponse(expires=3, content_type='application/json')
@app.route('/time.html')
@cross_origin(origins="*", send_wildcard=True, methods="GET")
def html_time():
    return render_template('clock.html')
