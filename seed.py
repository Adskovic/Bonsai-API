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
            origin="Japan",
            skill_level="Intermediate"
        )

        chinese_sweet_plum = Bonsai(
            name="Chinese sweet plum",
            species="Sageretia theezans",
            tree_type="Evergreen",
            origin="China",
            skill_level="Beginner"
        )

        chinese_elm = Bonsai(
            name="Chinese elm",
            species="Ulmus parviflora",
            tree_type="Evergreen",
            origin="China",
            skill_level="Beginner"
        )

        japanese_elm = Bonsai(
            name="Japanese elm",
            species="Zelkova",
            tree_type="Evergreen",
            origin="Japan",
            skill_level="Intermediate"
        )

        european_oak = Bonsai(
            name="European Oak",
            species="Quercus robur",
            tree_type="Deciduous",
            origin="Europe",
            skill_level="Intermediate"
        )

        american_white_oak = Bonsai(
            name="American White Oak",
            species="Quercus alba",
            tree_type="Deciduous",
            origin="North America",
            skill_level="Intermediate"
        )

        ficus = Bonsai(
            name="Ficus retusa",
            species="Ficus retusa",
            tree_type="Evergreen",
            origin="Indonesia",
            skill_level="Beginner"
        )

        chinese_juniper = Bonsai(
            name="Chinese Juniper",
            species="Juniperus Chinensis",
            tree_type="Coniferous",
            origin="China",
            skill_level="Intermediate"
        )

        japanese_shimpaku = Bonsai(
            name="Japanese Shimpaku Juniper",
            species="Juniperus sargentii",
            tree_type="Coniferous",
            origin="Japan",
            skill_level="Intermediate"
        )

        rocky_mountain_juniper = Bonsai(
            name="Rocky Mountain Juniper",
            species="Juniperus scopulorum",
            tree_type="Coniferous",
            origin="America",
            skill_level="Intermediate"
        )

        common_juniper = Bonsai(
            name="Common Juniper",
            species="Juniperus communis",
            tree_type="Coniferous",
            origin="Europe",
            skill_level="Beginner"
        )

        fukien_tea = Bonsai(
            name="Fukien Tea",
            species="Carmona Retusa",
            tree_type="Evergreen",
            origin="China",
            skill_level="Advanced"
        )

        japanese_black_pine = Bonsai(
            name="Japanese Black Pine",
            species="Pinus thunbergii",
            tree_type="Coniferous",
            origin="Japan",
            skill_level="Advanced"
        )

        trident_maple = Bonsai(
            name="Trident Maple",
            species="Acer buergerianum",
            tree_type="Deciduous",
            origin="China",
            skill_level="Intermediate"
        )

        bougainvillea = Bonsai(
            name="Bougainvillea",
            species="Bougainvillea glabra",
            tree_type="Flowering",
            origin="South America",
            skill_level="Beginner"
        )

        willow_leaf_ficus = Bonsai(
            name="Willow Leaf Ficus",
            species="Ficus nerifolia",
            tree_type="Evergreen",
            origin="Southeast Asia",
            skill_level="Beginner"
        )

        desert_rose = Bonsai(
            name="Desert Rose",
            species="Adenium obesum",
            tree_type="Succulent",
            origin="Africa",
            skill_level="Intermediate"
        )

        cedar = Bonsai(
            name="Cedar of Lebanon",
            species="Cedrus libani",
            tree_type="Coniferous",
            origin="Mediterranean",
            skill_level="Advanced"
        )

        # Additional Bonsai Entries
        olive = Bonsai(
            name="Olive",
            species="Olea europaea",
            tree_type="Evergreen",
            origin="Mediterranean",
            skill_level="Intermediate"
        )

        sago_palm = Bonsai(
            name="Sago Palm",
            species="Cycas revoluta",
            tree_type="Evergreen",
            origin="Japan",
            skill_level="Intermediate"
        )

        boxwood = Bonsai(
            name="Boxwood",
            species="Buxus sempervirens",
            tree_type="Evergreen",
            origin="Europe",
            skill_level="Beginner"
        )

        redwood = Bonsai(
            name="Dawn Redwood",
            species="Metasequoia glyptostroboides",
            tree_type="Coniferous",
            origin="China",
            skill_level="Intermediate"
        )

        pomegranate = Bonsai(
            name="Pomegranate",
            species="Punica granatum",
            tree_type="Flowering",
            origin="Middle East",
            skill_level="Advanced"
        )

        jade = Bonsai(
            name="Jade",
            species="Crassula ovata",
            tree_type="Succulent",
            origin="South Africa",
            skill_level="Beginner"
        )
        
        dwarf_jade = Bonsai(
            name="Dwarf Jade",
            species="Portulacaria Afra",
            tree_type="Succulent",
            origin="South Africa",
            skill_level="Beginner"
        )

        
        
        bonsai_list = [japanese_maple,
            chinese_sweet_plum,
            chinese_elm,
            japanese_elm,
            european_oak,
            american_white_oak,
            ficus,
            chinese_juniper,
            japanese_shimpaku,
            rocky_mountain_juniper,
            common_juniper,
            fukien_tea,
            japanese_black_pine,
            trident_maple,
            bougainvillea,
            willow_leaf_ficus,
            desert_rose,
            cedar,
            olive,
            sago_palm,
            boxwood,
            redwood,
            pomegranate,
            jade,
            dwarf_jade
            ]


    for bonsai in bonsai_list:
        db.session.add(bonsai)
    db.session.commit()
print("Trees have been successfully seeded.")

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