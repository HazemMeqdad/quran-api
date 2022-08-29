from flask import Blueprint, jsonify, send_from_directory, current_app
from utlits.checks import is_allow
import os


moshaf = Blueprint('moshaf', __name__, url_prefix="/moshaf")

@moshaf.route('/')
@is_allow
def index():
    files = os.listdir("cdn/moshaf/")
    domain = current_app.config['DOMAIN']
    data = [f"{domain}/moshaf/{file}" for file in files]
    data.sort()
    return jsonify(data)

@moshaf.route('/<path:path>')
@is_allow
def moshaf_from_file(path):
    if not path.endswith(".png"):
        data = [f"{current_app.config['DOMAIN']}/moshaf/{file}" for file in os.listdir("cdn/moshaf/")]
        data.sort()
        return jsonify({"available_files": data})
    if not os.path.exists("cdn/moshaf/" + path):
        return jsonify({"error": "file not found"}), 404
    return send_from_directory('cdn/moshaf', path)
