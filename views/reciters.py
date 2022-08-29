import json
import os
from flask import Blueprint, jsonify, send_from_directory, current_app as app
from utlits.checks import is_allow


reciters = Blueprint('reciters', __name__, url_prefix="/reciters")


@reciters.route('/')
@is_allow
def index():
    domain = app.config["DOMAIN"]
    available_reciters = os.listdir("cdn/reciters")
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)["reciters"]
    response = [{"reciter": data.get(i, None) or i, "url": domain + f"/reciters/{i}"} for i in available_reciters]
    return jsonify(response)


@reciters.route("/<path:path>")
@is_allow
def reader(path):
    file = os.path.exists("cdn/reciters/" + path)
    domain = app.config["DOMAIN"]
    folder_name = path.split("/")[-1]
    if not file:
        return jsonify({"error": "reciter not found"}), 404
    if not path.endswith(".mp3"):
        files = [domain + f"/reciters/{folder_name}/{i}" for i in os.listdir("cdn/reciters/" + path)]
        files.sort()
        with open("data.json", "r", encoding="utf-8") as f:
            reciters = json.load(f)["reciters"]
        return jsonify({"available_files": files, "name": reciters.get(folder_name, None) or folder_name})
    return send_from_directory("cdn/reciters", path, as_attachment=True)
