from flask import Blueprint, jsonify, request
from models import Bonsai, User, db

api = Blueprint('api', __name__)


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
    
    bonsai_list = Bonsai.query.filter((Bonsai.name.ilike(f'%{search_query}%')) | (Bonsai.species.ilike(f'%{search_query}%'))).all()
    bonsai_json = [bonsai.to_dict() for bonsai in bonsai_list]
    if bonsai_list:
        return jsonify(bonsai_json), 200
    else:
        return jsonify({'message': 'Bonsai not found'}), 404


# HTTP POST - Create Record

@api.route('/add_bonsai', methods=['POST'])  
def add_bonsai():
    name = request.form['name']
    test = Bonsai.query.filter_by(name=name).first()
    if test:
        return jsonify({'message': 'There is already a bonsai with this name.'}), 409
    else:
        species=request.form['species']
        tree_type=request.form['tree_type']
        origin=request.form['origin']

        new_bonsai = Bonsai(name=name, 
                            species=species, 
                            tree_type=tree_type, 
                            origin=origin
                            )
        db.session.add(new_bonsai)
        db.session.commit()
        return jsonify({'message': 'You added new bonsai tree.'}), 201


# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record