from flask import Blueprint, jsonify


azkar = Blueprint('azkar', __name__)


@azkar.route('/')
def index():
    return jsonify()

