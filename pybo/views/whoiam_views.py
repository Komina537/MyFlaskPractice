from flask import Flask
from flask import jsonify
import json

from flask import Blueprint, render_template, request, url_for, g, flash
from pybo.views.auth_views import login_required

app = Flask(__name__)
bp = Blueprint('whoiam', __name__, url_prefix='/whoiam')

@bp.route('/whoiam/')
def _whoiam():
    return render_template('mini/index1.html')