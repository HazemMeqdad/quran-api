import json
from flask import Blueprint, jsonify
import random

pray = Blueprint('pray', __name__, url_prefix="/pray")


@pray.route('/')
def index():
    with open("pray.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

@pray.route('/random')
def random_pray():
    with open("pray.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data[random.randint(0, len(data) - 1)])
