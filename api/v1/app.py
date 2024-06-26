#!/usr/bin/python3
""" Module for the API """

from flask import Flask
from flask import jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """ Closes the current session """
    storage.close()


@app.errorhandler(404)
def not_found(e):
    """ Returns a JSON-formatted 404 status code response """
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
