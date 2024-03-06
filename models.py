from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Bonsai(db.Model):
    pass


class BonsaiOwner(db.Model):
    pass