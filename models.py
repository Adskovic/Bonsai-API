from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Bonsai(db.Model):
    __tablename__ = "bonsai"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    species = db.Column(db.String(100))
    tree_type = db.Column(db.String(100))
    origin = db.Column(db.String(100))

    def to_dict(self):
        return {
            "name": self.name,
            "species": self.species,
            "tree_type": self.tree_type,
            "origin": self.origin
        }



class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)