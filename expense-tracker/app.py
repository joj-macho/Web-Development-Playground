from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
from pathlib import Path
from datetime import datetime

# Set Working Directory
BASE_DIRECTORY = Path(__file__).resolve().parent
os.chdir(BASE_DIRECTORY)

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a secret key and database URI
app.config['SECRET_KEY'] = 'a_random_secret_key'  # Replace 'a_random_secret_key' with a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object to interact with the database
db = SQLAlchemy(app)

# Expense class to represent the database model for employees
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Expense {self.description}>'

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    '''Display all expenses.'''
    expenses = Expense.query.all()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    '''Add a new expense.'''
    if request.method == 'POST':
        # Get form data
        description = request.form['description']
        amount = float(request.form['amount'])
        category = request.form['category']
        date_str = request.form['date']
        # Convert the date string to a Python date object
        date = datetime.strptime(date_str, '%Y-%m-%d').date()

        # Basic input validation
        if not description or not amount or not date:
            flash('Expense Description, Amount, and Date are required.', 'danger')
            return redirect(url_for('add_expense'))

        # Create a new Expense object and add it to the database
        expense = Expense(description=description, amount=amount, category=category, date=date)
        db.session.add(expense)
        db.session.commit()
        flash('Expense added successfully!', 'success')

        return redirect(url_for('index'))
    return render_template('add_expense.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    '''Edit an existing expense.'''
    expense = Expense.query.get_or_404(id)

    if request.method == 'POST':
        # Get form data
        expense.description = request.form['description']
        expense.amount = float(request.form['amount'])
        expense.category = request.form['category']
        date_str = request.form['date']
        # Convert the date string to a Python date object
        expense.date = datetime.strptime(date_str, '%Y-%m-%d').date()

        # Basic input validation
        if not expense.description or not expense.amount or not expense.date:
            flash('Expense Description, Amount, and Date are required.', 'danger')
            return redirect(url_for('edit_expense', id=expense.id))

        # Update the expense in the database
        db.session.commit()
        flash('Expense updated successfully!', 'info')

        return redirect(url_for('index'))
    return render_template('edit_expense.html', expense=expense)

@app.route('/delete/<int:id>')
def delete_expense(id):
    '''Delete an expense.'''
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted successfully!', 'danger')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
