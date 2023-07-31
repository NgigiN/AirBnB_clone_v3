#!/usr/bin/python3
# Path: api/v1/views/index.py
# Compare this snippet from models/engine/file_storage.py:


from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage_t


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """" Returns a JSON: "status": "OK" """
    return jsonify({"status": "OK"})
