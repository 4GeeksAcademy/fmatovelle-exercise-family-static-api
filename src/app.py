"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Verificar que los miembros se agregaron correctamente
print(jackson_family)
# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members')
def get_all_members():
    members =  jackson_family.get_all_members()
    return jsonify(members), 200
@app.route('/members', methods=['POST'])

def add_member():
    added_member = jackson_family.add_member()
    return jsonify(added_member)
@app.route('/member/<int:id>', methods=['GET'])

def get_member(id):
    member = jackson_family.get_member(id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"msg": "Member not found"}), 404
@app.route('/member/<int:id>', methods=['DELETE'])

def delete_member(id):
    result = jackson_family.delete_member(id)
    return jsonify(result)

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
