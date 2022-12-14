from unittest import TestCase

from forms import PetForm
from app import app
from models import db, connect_db, Pet

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_wtforms_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

# Don't req CSRF for testing
app.config['WTF_CSRF_ENABLED'] = False

db.drop_all()
db.create_all()

class PetViewsTestCase(TestCase):
    """Tests for views for Pets."""
    def setUp(self):
        """Add sample pet."""
        
        Pet.query.delete()
        
        pet = Pet(name="Test Pet", species="cat", photo_url="https://www.google.com", age=5, notes="Test Notes")
        db.session.add(pet)
        db.session.commit()
        self.pet_id = pet.id
        
    def tearDown(self):
        """Clean up any fouled transaction."""
        
        db.session.rollback()
        
    
    def test_pet_add_form(self):
        with app.test_client() as client:
            resp = client.get("/pets/new")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<title> New </title>', html)
    
    def test_home_view(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<title> HOME </title>', html)
            
    def test_pet_edit_form(self):
        with app.test_client() as client:
            resp = client.get(f"/pets/{self.pet_id}/edit")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<title> Edit </title>', html)
    
    def test_pet_edit(self):
        with app.test_client() as client:
            resp = client.post(
                f"/pets/{self.pet_id}/edit",
                data={"name": "Test Pet", "species": "cat", "photo_url": "https://www.google.com", "age": 5, "notes": "Test Notes"},
                follow_redirects=True
            )
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<title> HOME </title>', html)
            
            pet = Pet.query.get(self.pet_id)
            self.assertEquals(pet.name, "Test Pet")
            self.assertEquals(pet.species, "cat")