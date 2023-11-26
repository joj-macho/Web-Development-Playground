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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object to interact with the database
db = SQLAlchemy(app)

# Item class to represent the database model for inventory
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=True)
    price = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"<Item {self.name}>"

# Create the database
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    '''Display all expenses.'''
    items = Item.query.all()
    return render_template('index.html', items=items)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    '''Add an item.'''
    # Get form data
    if request.method == 'POST':
        name = request.form['name']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])

        # Basic input validation
        if not name or not quantity:
            flash('Item Name and Quantity are required.', 'danger')
            return redirect(url_for('add_item'))

        # Create a new item object and add it to the database
        item = Item(name=name, quantity=quantity, price=price)
        db.session.add(item)
        db.session.commit()
        flash('Item added successfully!', 'success')

        return redirect(url_for('index'))
    return render_template('add_item.html')


@app.route('/edit_item/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    '''Edit an existing item.'''
    item = Item.query.get_or_404(item_id)
    if request.method == 'POST':
        # Get form data
        item.name = request.form['name']
        item.quantity = int(request.form['quantity'])
        item.price = float(request.form['price'])

        # Basic input validation
        if not item.name or not item.quantity:
            flash('Item Name and Quantity are required.', 'danger')
            return redirect(url_for('edit_item', item_id=item.id))

        # Update the inventory in the database
        db.session.commit()
        flash('Item updated successfully!', 'info')

        return redirect(url_for('index'))
    return render_template('edit_item.html', item=item)


@app.route('/delete_item/<int:item_id>')
def delete_item(item_id):
    '''Delete an expense.'''
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted successfully!', 'danger')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
