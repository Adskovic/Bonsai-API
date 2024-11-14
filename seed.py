import click
from flask import Blueprint
from models import Bonsai, User, db
from werkzeug.security import generate_password_hash


seed = Blueprint('seed', __name__)


# Bonsai table seed command
# Use command 'flask seed bonsai' to seed database with bonsai trees
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
        
        chinese_elm = Bonsai(
            name="Chinese elm",
            species="Ulmus parviflora",
            tree_type="Sub-tropical",
            origin="China"
                            )
        
        japanese_elm = Bonsai(
            name="Japanese elm",
            species="Zelkova",
            tree_type="Sub-tropical",
            origin="Japan"
                            )
        
        european_oak = Bonsai(
            name="European Oak",
            species="Quercus robur",
            tree_type="Deciduous",
            origin="Europe"
                            )
        
        american_white_oak = Bonsai(
            name="American White Oak",
            species="Quercus alba",
            tree_type="Deciduous",
            origin="North America"
                            )
        
        ficus = Bonsai(
            name="Ficus retusa",
            species="Ficus retusa",
            tree_type="Tropical",
            origin="Indonesia"
                            )
        
        chinese_juniper = Bonsai(
            name="Chinese Juniper",
            species="Juniperus Chinensis",
            tree_type="Coniferous",
            origin="China"
                            )
        
        japanese_shimpaku = Bonsai(
            name="Japanese Shimpaku Juniper",
            species="Juniperus sargentii",
            tree_type="Coniferous",
            origin="Japan"
                            )
        
        rocky_mountain_juniper = Bonsai(
            name="Rocky Mountain Juniper",
            species="Juniperus scopulorum",
            tree_type="Coniferous",
            origin="America"
                            )

        common_juniper = Bonsai(
            name="Common Juniper",
            species="Juniperus communis",
            tree_type="Coniferous",
            origin="Europe"
                            )
        
        fukien_tea = Bonsai(
            name="Fukien Tea",
            species="Carmona Retusa",
            tree_type="Sub-tropical",
            origin="China"
                            )

    #TODO: Add some Pines, Spruce, Redwood, Cherry etc.
        

        db.session.add(japanese_maple)
        db.session.add(chinese_sweet_plum)
        db.session.commit()
        print("Trees has been successfully seeded.")


# User table seed command
# Use command 'flask seed users' to seed database with test user
@seed.cli.command('users')
def db_seed_users():
    """Add user to User table. """
    if User.query.first() is None:

        hashed_pass = generate_password_hash("223344")
        test_user = User(
            name="Test",
            email="test@test.pl",
            password=hashed_pass
                        )
        db.session.add(test_user)

        db.session.commit()
        print("Users has been successfully seeded.")