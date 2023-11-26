from flask import Flask, render_template, request, flash, redirect, url_for
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object to interact with the database
db = SQLAlchemy(app)

# Task class to represent the database model for books
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<Task {self.title}>"

# Create the database
with app.app_context():
    db.create_all()

    # Add demo tasks
    demo_tasks = [
        Task(title="Task 1", description="Description for Task 1", completed=False),
        Task(title="Task 2", description="Description for Task 2", completed=False),
        Task(title="Task 3", description="Description for Task 3", completed=True),
    ]

    db.session.bulk_save_objects(demo_tasks)
    db.session.commit()


@app.route('/')
def index():
    '''Render the home page with a list of all tasks'''
    tasks = Task.query.order_by(Task.completed, Task.due_date).all()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    '''Render the page for creating a new tasks or handle form submission.'''
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date_str = request.form['due_date']
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d') if due_date_str else None
        task = Task(title=title, description=description, due_date=due_date)
        db.session.add(task)
        db.session.commit()
        flash('Task added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/toggle_complete/<int:task_id>')
def toggle_complete(task_id):
    '''Render the page for toggling task completion status.'''
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    '''Delete a task based on the provided ID.'''
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
