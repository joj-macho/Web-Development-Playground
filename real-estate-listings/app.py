from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import os
from pathlib import Path

# Set Working Directory
BASE_DIRECTORY = Path(__file__).resolve().parent
os.chdir(BASE_DIRECTORY)

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a secret key and database URI
app.config['SECRET_KEY'] = 'a_random_secret_key'  # Replace with a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///properties.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object to interact with the database
db = SQLAlchemy(app)

# Property class to represent the database model for property listings
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.String(20), nullable=False)
    image_url = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"<Property {self.title}>"

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    '''Display all propertly listings.'''
    listings = Property.query.all()
    return render_template('index.html', listings=listings)

@app.route('/property/<int:property_id>')
def property_detail(property_id):
    '''Display a specific property listing'''
    property_data = Property.query.get(property_id)
    if property_data:
        return render_template('property.html', property=property_data)

    flash('Property not found', 'danger')
    return redirect(url_for('index'))

@app.route('/add_property', methods=['GET', 'POST'])
def add_property():
    '''Add a new property.'''
    if request.method == 'POST':
        # Get form data
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        image_url = request.form['image_url']

        # Create a new Contact object and add it to the database
        new_property = Property(title=title, description=description, price=price, image_url=image_url)
        db.session.add(new_property)
        db.session.commit()
        flash('Property added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_property.html')

@app.route('/edit_property/<int:property_id>', methods=['GET', 'POST'])
def edit_property(property_id):
    '''Edit an existing existing.'''
    property_data = Property.query.get_or_404(property_id)

    if request.method == 'POST':
        # Get form data
        property_data.title = request.form['title']
        property_data.description = request.form['description']
        property_data.price = request.form['price']
        property_data.image_url = request.form['image_url']

        # Update the property in the database
        db.session.commit()
        flash('Property updated successfully!', 'info')
        return redirect(url_for('index'))

    return render_template('edit_property.html', property=property_data)

@app.route('/delete_property/<int:property_id>', methods=['GET', 'POST'])
def delete_property(property_id):
    '''Delete an existing property.'''
    property_data = Property.query.get_or_404(property_id)
    db.session.delete(property_data)
    db.session.commit()
    flash('Property deleted successfully!', 'danger')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
