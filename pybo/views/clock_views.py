from flask import Flask
from flask import jsonify
import json

from flask import Blueprint, render_template, request, url_for, g, flash
from pybo.views.auth_views import login_required

app = Flask(__name__)
bp = Blueprint('clock', __name__, url_prefix='/clock')

@bp.route('/clock/')
def _clock():
    return render_template('clock/clock.html')

@bp.route('/calendar/')
def _calendar():
    return render_template('clock/calendar.html')

@app.route('/data')
def return_data():
    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')
    # You'd normally use the variables above to limit the data returned
    # you don't want to return ALL events like in this code
    # but since no db or any real storage is implemented I'm just
    # returning data from a text file that contains json elements

    with open("./events.json", "r") as input_data:
        # you should use something else here than just plaintext
        # check out jsonfiy method or the built in json module
        # http://flask.pocoo.org/docs/0.10/api/#module-flask.json
        return input_data.read()

if __name__ == '__main__':
    app.debug = True
    app.run()