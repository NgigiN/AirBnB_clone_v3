#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage_t


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """" Returns a JSON: "status": "OK" """
    return jsonify({"status": "OK"})
