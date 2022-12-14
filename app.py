from flask import Flask, render_template, flash, redirect, request
from models import db, connect_db, Pet, get_pet
from forms import PetForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adoption_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# debug = DebugToolbarExtension(app)

app.app_context().push()
connect_db(app)

@app.route('/')
def home():
    """Shows all pets and a a link to add new pets"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route('/pets/<int:pet_id>/detail')
def show_pet_detail(pet_id):
    """Get's the pet from the database as well as shows information for editing a pet"""
    pet = get_pet(pet_id)
    return render_template("detail.html", pet=pet)

    

@app.route('/pets/new', methods=["GET","Post"])
def handle_new_pet():
    """Creates a new pet and submits it to the database"""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        species = form.species.data
        photo_url = form.photo_url.data
        is_available = form.is_available.data
   
        pet = Pet(name=name, age=age, species=species, photo_url=photo_url, is_available=is_available)
        db.session.add(pet)
        db.session.commit()
        print(pet)
        
        return redirect('/')
    else:
        return render_template("new.html", form=form)
    
@app.route('/pets/<int:pet_id>/edit', methods=["GET","Post"])
def show_pet_edit_page(pet_id):
    """Shows the pet edit page form and pet by the id

    Args:
        pet_id (int): pet_id from the database

    Returns:
        html: Shows the html page
    """
    pet = get_pet(pet_id)
    form = PetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.age = form.age.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.is_available = form.is_available.data
        pet.notes = form.notes.data
        
        db.session.commit()
        
        return redirect('/')
    
    else:
        return render_template("edit.html", form=form)