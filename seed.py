from models import Pet, db
from app import app 

# Create all tables
db.drop_all()
db.create_all()

# TODO commit seeds to the database

p1 = Pet(name="Whiskers", age=4, species="Tiger", photo_url="https://images.pexels.com/photos/2541239/pexels-photo-2541239.jpeg?cs=srgb&dl=pexels-waldemar-brandt-2541239.jpg&fm=jpg")
p2 = Pet(name="Mr. Pickles", age="8", species="Lion", photo_url="https://images.pexels.com/photos/247502/pexels-photo-247502.jpeg?auto=compress&cs=tinysrgb&w=400")
p3 = Pet(name="Bobo", age="6", species="Chimpanzee", photo_url="https://images.pexels.com/photos/1238352/pexels-photo-1238352.jpeg?auto=compress&cs=tinysrgb&w=400")
p4 = Pet(name="Nemo", age="5", species="Parrot", photo_url="https://images.pexels.com/photos/1004517/pexels-photo-1004517.jpeg?auto=compress&cs=tinysrgb&w=400")
p5 = Pet(name="Suga and Spyce", age="1", species="Dog", photo_url="https://images.pexels.com/photos/14555653/pexels-photo-14555653.jpeg?auto=compress&cs=tinysrgb&w=400")


db.session.add_all([p1, p2, p3, p4, p5])
db.session.commit()