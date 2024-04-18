import click
from flask import Blueprint
from models import Bonsai, User, db


seed = Blueprint('seed', __name__)


# Bonsai table seed command
@seed.cli.command('bonsai')
def db_seed_bonsai():
    """Add trees to Bonsai table. """ 
    if Bonsai.query.first() is None:

        japanese_maple = Bonsai(
            name="Japanese maple",
            species="Acer palmatum",
            tree_type="Deciduous",
            origin="Japan"
                                )
        
        chinese_sweet_plum = Bonsai(
            name="Chinese sweet plum",
            species="Sageretia theezans",
            tree_type="Sub-tropical",
            origin="China"
                            )
        

        db.session.add(japanese_maple)
        db.session.add(chinese_sweet_plum)
        db.session.commit()
        print("Trees has been successfully seeded.")


# User table seed command
@seed.cli.command('users')
def db_seed_users():
    """Add user to User table. """
    if User.query.first() is None:

        test_user = User(
            name="Test",
            email="test@test.pl",
            password="223344"
                        )
        db.session.add(test_user)

        db.session.commit()
        print("Users has been successfully seeded.")