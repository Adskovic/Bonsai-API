from models import Bonsai, User, db
from routes import api

@api.cli.command('db_seed')
def db_seed():
    japanese_maple = Bonsai(name="Japanese maple",
                            species="Acer palmatum",
                            tree_type="Deciduous",
                            origin="Japan"
                            )
    
    chinese_sweet_plum = Bonsai(name="Chinese sweet plum",
                        species="Sageretia theezans",
                        tree_type="Sub-tropical",
                        origin="China"
                        )
    
    db.session.add(japanese_maple)
    db.session.add(chinese_sweet_plum)
    db.session.commit()
    print("Database seeded.")