from flask import Blueprint, send_from_directory
from utlits.checks import is_allow


reciters = Blueprint('reciters', __name__, url_prefix="/reciters")


@reciters.route("/<path:path>")
@is_allow
def reader(path):
    return send_from_directory("cdn/reciters", path)
