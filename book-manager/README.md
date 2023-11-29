# Book Management System Application

## Description

The Book Management System is a web-based application that allows users to manage their collection of books. Users can add new books, edit existing ones, and delete books they no longer need. The application uses Flask for the backend and SQLite for the database to store book records.

## How it Works

- Start by setting up the Flask application including importing required modules, configuration for the database, and creating an instance of the SQLAlchemy database.

- The `Book` class is created to represent the model for books in the database, including attributes like `title`, `author`, `description`, and `rating`.

- The SQLite database is created and the necessary table for books is defined.

- Various routes are established to handle different functionalities:
    - **Index Route** (`/`): Displays the list of book.
    - **Add Book Route** (`/add_book`): Allows the user to add a new book.
    - **Edit Book Route** (`/edit_book/int:book_id`): Allows the user to edit an existing book.
    - **Delete Book Route** (`/delete_book/int:book_id`): Allows the user to delete an existing book.

- The routes render HTML templates that serve as the views, providing the user interface for the corresponding functionality. Users can interact with the application by filling out forms to add or edit book details.

## How to Run the Application

- To run this application, first you must ensure that you have Python installed on your system.
- Ensure that you have `Flask` and `SQLAlchemy` installed on your system. If not, you can install them using pip: `pip install flask flask_sqlalchemy`
- Navigate to the project directory.
- Run the application on the terminal: `python3 app.py`
- Open a web browser and go to http://localhost:5000 to access the Book Management System. The output will look like this:

![Books Output](output/book-output.gif)

