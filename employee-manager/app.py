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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object to interact with the database
db = SQLAlchemy(app)

# Employee class to represent the database model for employees
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=True)
    department = db.Column(db.String(100), nullable=True)
    salary = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"<Employee {self.name}>"

# Create the database
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    '''Display all contacts.'''
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)


@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    '''Add a new employee.'''
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        position = request.form['position']
        department = request.form['department']
        salary = float(request.form['salary'])

        # Basic input validation
        if not name or not position:
            flash('Name and Position are required.', 'danger')
            return redirect(url_for('add_employee'))

        # Create a new Employee object and add it to the database
        employee = Employee(name=name, position=position, department=department, salary=salary)
        db.session.add(employee)
        db.session.commit()
        flash('Employee added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_employee.html')


@app.route('/edit_employee/<int:employee_id>', methods=['GET', 'POST'])
def edit_employee(employee_id):
    '''Edit an existing employee.'''
    employee = Employee.query.get_or_404(employee_id)
    if request.method == 'POST':
        # Get form data
        employee.name = request.form['name']
        employee.position = request.form['position']
        employee.department = request.form['department']
        employee.salary = float(request.form['salary'])

        # Basic input validation
        if not employee.name or not employee.position:
            flash('Name and Position are required.', 'danger')
            return redirect(url_for('edit_employee', employee_id=employee.id))

        # Update the employee in the database
        db.session.commit()
        flash('Employee updated successfully!', 'info')
        return redirect(url_for('index'))
    return render_template('edit_employee.html', employee=employee)


@app.route('/delete_employee/<int:employee_id>')
def delete_employee(employee_id):
    '''Delete an employee.'''
    employee = Employee.query.get_or_404(employee_id)
    db.session.delete(employee)
    db.session.commit()
    flash('Employee deleted successfully!', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
