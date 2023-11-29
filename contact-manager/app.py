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
app.config['SECRET_KEY'] = 'a_random_secret_key'  # Replace 'a_random_secret_key' with a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object to interact with the database
db = SQLAlchemy(app)

# Contact class to represent the database model for contacts
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<Contact {self.name}>"

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    '''Display all contacts.'''
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@app.route('/add_contact', methods=['GET', 'POST'])
def add_contact():
    '''Add a new contact.'''
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        # Basic input validation
        if not name or not email:
            flash('Name and Email are required.', 'danger')
            return redirect(url_for('add_contact'))

        # Create a new Contact object and add it to the database
        contact = Contact(name=name, phone=phone, email=email)
        db.session.add(contact)
        db.session.commit()
        flash('Contact added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_contact.html')

@app.route('/edit_contact/<int:contact_id>', methods=['GET', 'POST'])
def edit_contact(contact_id):
    '''Edit an existing contact.'''
    contact = Contact.query.get_or_404(contact_id)
    if request.method == 'POST':
        # Get form data
        contact.name = request.form['name']
        contact.phone = request.form['phone']
        contact.email = request.form['email']

        # Basic input validation
        if not contact.name or not contact.email:
            flash('Name and Email are required.', 'danger')
            return redirect(url_for('edit_contact', contact_id=contact.id))

        # Update the contact in the database
        db.session.commit()
        flash('Contact updated successfully!', 'info')
        return redirect(url_for('index'))
    return render_template('edit_contact.html', contact=contact)

@app.route('/delete_contact/<int:contact_id>')
def delete_contact(contact_id):
    '''Delete a contact.'''
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact deleted successfully!', 'danger')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
