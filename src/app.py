"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""

import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
import json

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)


jackson_family = FamilyStructure("Jackson")


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def handle_hello():
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }
    return jsonify(members), 200


@app.route('/member/<int:id>', methods=['GET'])
def list_single_member(id):
    member = jackson_family.get_member(id)
    return jsonify(member), 200


@app.route('/member', methods=['POST'])
def add_jackson():
    data = request.json
    members = jackson_family.add_member(data)
    if members == "added":
        return jsonify('The new Jackson is here!'), 200
    else:
        return jsonify("That guy is not a Jackson's family member"), 400


@app.route('/member/<int:id>', methods=['DELETE'])
def delete_jackson(id):
    members = jackson_family.delete_member(id)
    if members == "not found":
        return jsonify('This Jackson probably is not here anymore'), 400
    else:
        return jsonify(members), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
