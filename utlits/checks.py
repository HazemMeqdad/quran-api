from functools import wraps, current_app as app, jsonify

from flask import request


def is_allow(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ip = request.remote_addr
        if app.config['ALLOW_HOSTS'] != '*' and ip not in app.config['ALLOW_HOSTS']:
            return jsonify({"error": "You are not allowed to access this API."}), 403
        return func(*args, **kwargs)
    return wrapper

