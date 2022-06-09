from flask import jsonify



def page_not_found(e):
    return jsonify({"error": "This route does not exist."}), 404
