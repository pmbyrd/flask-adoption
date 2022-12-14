from flask_sqlalchemy import SQLAlchemy

Default_Url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0jQ8wyxDdRDNZdu-LCU95MYnotwaUuRJ8_A&usqp=CAU"
db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
    
class Pet(db.Model):
    """Creates a table model pets for the database"""
    __tablename__ = "pets"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=False, default=Default_Url)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    is_available = db.Column(db.Boolean, unique=False, default=True)
    
    def __repr__(self):
        return f"<Pet name={self.name}, species={self.species}, age={self.age}>"
    

def get_pet(pet_id):
    """Queries the pet from the database"""
    
    pet = Pet.query.get_or_404(pet_id)
    return pet