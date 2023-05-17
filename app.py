from flask import Flask, render_template, flash, redirect, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import PetForm, EditPetForm

app = Flask(__name__)
app.app_context().push()
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_pet_list():
    """Show list of all pets."""
    pets = Pet.query.all()
    return render_template('home.html', pets = pets)

@app.route('/add', methods=["GET", "POST"])
def add_new_pet():
    """Show form to add a new pet to the database."""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_new_pet.html', form = form)
    
@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_pet_details(pet_id):
    """Show pet information and a form to edit pet information."""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()


    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit_pet.html', form=form, pet=pet)


