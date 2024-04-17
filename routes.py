from flask import Blueprint, jsonify, request
from models import Bonsai, User, db

api = Blueprint('api', __name__)

@api.route('/bonsai')
def get_all_bonsai():
    bonsai_list = Bonsai.query.all()
    bonsai_json = [bonsai.to_dict() for bonsai in bonsai_list]
    return jsonify(bonsai_json)

# HTTP GET - Read Record

# HTTP POST - Create Record

@api.route('/bonsai', methods=['POST'])
def add_bonsai():
    data = request.get_json()
    new_bonsai = Bonsai(name=data['name'], species=data['species'])
    db.session.add(new_bonsai)
    db.session.commit()
    return jsonify({'message': 'Bonsai added successfully!'}), 201


# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record