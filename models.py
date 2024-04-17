from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Bonsai(db.Model):
    __tablename__ = "bonsai"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    species = db.Column(db.String(100))
    tree_type = db.Column(db.String(100))
    origin = db.Column(db.String(100))



class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))