from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bonsai(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    species = db.Column(db.String(100))
    age = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('bonsai_owner.id'))


class BonsaiOwner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))