from flask import Blueprint, jsonify, send_from_directory, request, current_app
from utlits.checks import is_allow
import os


moshaf = Blueprint('moshaf', __name__, url_prefix="/moshaf")

@moshaf.route('/')
@is_allow
def index():
    files = os.listdir("cdn/moshaf/")
    domain = current_app.config['DOMAIN']
    return jsonify([f"{domain}/moshaf/{file}" for file in files])

@moshaf.route('/<path:path>')
@is_allow
def moshaf_from_file(path):
    return send_from_directory('cdn/moshaf', path)
