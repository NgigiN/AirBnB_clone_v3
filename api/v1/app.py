#!/usr/bin/python3
# import storage from models

from models import storage
from api.v1.views import app_views
from flask import jsonify, Blueprint, Flask
import os
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.register_blueprint(app_views)

CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontest(self):
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """404 page not found"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')),
            debug=True, threaded=True)
