from functools import wraps
from flask import request, current_app as app, jsonify


def is_allow(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ip = request.remote_addr
        if app.config['ALLOW_HOSTS'] != ['*'] and ip not in app.config['ALLOW_HOSTS']:
            return jsonify({"error": "You are not allowed to access this API."}), 403
        return func(*args, **kwargs)
    return wrapper

