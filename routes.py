from flask import Blueprint, jsonify, request
from models import Bonsai, User, db

api = Blueprint('api', __name__)


# User authentication routes

@api.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email-email).first():
        return jsonify({'message': 'User already exist'}), 409
    
    new_user = User(name=name, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered sucessfully'}), 201


#TODO: Add login route with access token
@api.route('/login', methods=['POST'])
def login():
    pass



# HTTP GET - Read Record

@api.route('/bonsai', methods=['GET'])
def get_all_bonsai():
    bonsai_list = Bonsai.query.all()
    bonsai_json = [bonsai.to_dict() for bonsai in bonsai_list]
    return jsonify(bonsai_json)


@api.route('/bonsai/<int:bonsai_id>', methods=['GET'])
def get_bonsai(bonsai_id):
    bonsai = Bonsai.query.get(bonsai_id)
    if bonsai:
        return jsonify(bonsai.to_dict()), 200
    else:
        return jsonify({'message': 'Bonsai not found'}), 404


@api.route('/bonsai', methods=['POST'])
def search_bonsai():
    search_query = request.args.get('query')
    if not search_query:
        return jsonify({'message': 'Query parameter "query" is required'}), 400

    bonsai_list = Bonsai.query.filter(
        (Bonsai.name.ilike(f'%{search_query}%')) | 
        (Bonsai.species.ilike(f'%{search_query}%'))
    ).all()
    bonsai_json = [bonsai.to_dict() for bonsai in bonsai_list]
    if bonsai_list:
        return jsonify(bonsai_json), 200
    else:
        return jsonify({'message': 'Bonsai not found'}), 404


# HTTP POST - Create Record

@api.route('/add_bonsai', methods=['POST'])  
def add_bonsai():
    data = request.get_json()  # Parse JSON from the request body

    name = data.get('name')
    if not name:
        return jsonify({'message': 'Name is required'}), 400

    test = Bonsai.query.filter_by(name=name).first()
    if test:
        return jsonify({'message': 'There is already a bonsai with this name.'}), 409

    species = data.get('species')
    tree_type = data.get('tree_type')
    origin = data.get('origin')

    # Ensure essential fields are provided
    if not species or not tree_type or not origin:
        return jsonify({'message': 'Species, tree type, and origin are required'}), 400

    new_bonsai = Bonsai(
        name=name,
        species=species,
        tree_type=tree_type,
        origin=origin
    )
    db.session.add(new_bonsai)
    db.session.commit()
    return jsonify({'message': 'You added a new bonsai tree.'}), 201


# HTTP PUT - Update Record

@api.route('/update_bonsai/<int:id>', methods=['PUT'])
def update_bonsai(id):
    bonsai = Bonsai.query.get_or_404(id)
    data = request.get_json()

    if 'name' in data:
        existing_bonsai = Bonsai.query.filter_by(name=data['name']).first()
        if existing_bonsai and existing_bonsai.id != id:
            return jsonify({'message': 'There is already a bonsai with this name.'}), 409
        bonsai.name = data['name']

    if 'species' in data:
        bonsai.species = data['species']
    if 'tree_type' in data:
        bonsai.tree_type = data['tree_type']
    if 'origin' in data:
        bonsai.origin = data['origin']

    db.session.commit()
    return jsonify({'message': 'Bonsai record updated successfully.'}), 200


# HTTP DELETE - Delete Record

@api.route('/delete_bonsai/<int:id>', methods=['DELETE'])
def delete_bonsai(id):
    bonsai = Bonsai.query.get_or_404(id)
    db.session.delete(bonsai)
    db.session.commit()
    return jsonify({'message': 'Bonsai record deleted successfully.'}), 200
