#!/usr/bin/python3
"""Flask app to handle api for AirBnB clone"""


from api.v1.views import app_views
from flask import jsonify
from models import storage_t


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """" Returns a JSON: "status": "OK" """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """" Returns a JSON: "status": "OK" """
    return jsonify({"amenities": storage_t.count("Amenity"),
                    "cities": storage_t.count("City"),
                    "places": storage_t.count("Place"),
                    "reviews": storage_t.count("Review"),
                    "states": storage_t.count("State"),
                    "users": storage_t.count("User")})
