from flask import Flask
from flask import jsonify
import json

from flask import Blueprint, render_template, request, url_for, g, flash
from pybo.views.auth_views import login_required

app = Flask(__name__)
bp = Blueprint('MovieDL', __name__, url_prefix='/MovieDL')

@bp.route('/MovieDL/')
def _MovieDL():
    return render_template('MovieDL_final/5_Web Implementation/index.html')

@bp.route('/5rings/')
def _5rings():
    return render_template('MovieDL_final/5_Web Implementation/5rings.html')

@bp.route('/ML_model/')
def _ML_model():
    return render_template('MovieDL_final/5_Web Implementation/ml_model.html')

@bp.route('/report/')
def _report():
    return render_template('MovieDL_final/5_Web Implementation/report.html')