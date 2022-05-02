from flask import Blueprint, send_from_directory
from utlits.checks import is_allow


moshaf = Blueprint('moshaf', __name__)

@moshaf.route('/<path:path>')
@is_allow
def index(path):
    return send_from_directory('cdn', path)

