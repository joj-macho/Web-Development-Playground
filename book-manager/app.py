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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object to interact with the database
db = SQLAlchemy(app)

# Book class to represent the database model for books
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"<Book {self.title}>"

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    '''Display all contacts.'''
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    '''Add a new contact.'''
    if request.method == 'POST':
        # Get form data
        title = request.form['title']
        author = request.form['author']
        description = request.form['description']
        rating = int(request.form['rating'])

        # Basic input validation
        if not title or not author:
            flash('Book Title and Author are required.', 'danger')
            return redirect(url_for('add_book'))
        
        # Create a new Contact object and add it to the database
        book = Book(title=title, author=author, description=description, rating=rating)
        db.session.add(book)
        db.session.commit()
        flash('Book added successfully!', 'success')

        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    '''Edit an existing contact.'''
    book = Book.query.get_or_404(book_id)
    if request.method == 'POST':
        # Get form data
        book.title = request.form['title']
        book.author = request.form['author']
        book.description = request.form['description']
        book.rating = int(request.form['rating'])

        # Basic input validation
        if not book.title or not book.author:
            flash('Book Title and Author are required.', 'danger')
            return redirect(url_for('edit_book', book_id=book.id))

        # Update the book in the database
        db.session.commit()
        flash('Book updated successfully!', 'info')

        return redirect(url_for('index'))
    return render_template('edit_book.html', book=book)

@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    '''Delete a contact.'''
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash('Book deleted successfully!', 'danger')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
