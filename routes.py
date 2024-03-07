from flask import Blueprint, jsonify
from models import Bonsai, BonsaiOwner

api = Blueprint('api', __name__)

@api.route('/bonsai')
def get_all_bonsai():
    bonsai_list = Bonsai.query.all()
    bonsai_json = [bonsai.to_dict() for bonsai in bonsai_list]
    return jsonify(bonsai_json)

# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record