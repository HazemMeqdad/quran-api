from flask import Blueprint, jsonify
from utlits.checks import is_allow


index = Blueprint('inedx', __name__)


@index.route("/")
@is_allow
def welcome():
    return jsonify({"message": "Welcome to the API for Quran cdn."})
