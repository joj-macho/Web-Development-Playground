# Contact Manager Application

## Description

The Contact Manager is a simple web application that allows users to manage their contacts. Users can view a list of contacts, add new contacts, edit existing contacts, and delete contacts. The application uses Flask for the backend and SQLite for the database to store contact information.

This web application is an implementation of this [Simple Address Book CLI](https://github.com/joj-macho/Pythological-Playground/tree/main/converter), providing a more user-friendly interface for managing contacts.

## How it Works

- Start by setting up the Flask application including importing required modules, configuration for the database and creating an instance of the SQLAlchemy database.

- The `Contact` class is defined, representing the model of a contact with attributes like `name`, `phone`, and `email`.

- The SQLite database is created and the necessary table for contacts is defined.

- Various routes are established to handle different functionalities:
    - **Index Route** (`/`): Displays the list of contacts.
    - **Add Contact Route** (`/add_contact`): Allows the user to add a new contact.
    - **Edit Contact Route** (`/edit_contact/int:contact_id`): Allows the user to edit an existing contact.
    - **Delete Contact Route** (`/delete_contact/int:contact_id`): Allows the user to delete an existing contact.

- The routes above render HTML templates that serve as the views, providing the user interface for the corresponding functionality. Users can interact with the application by filling out forms to add or edit contacts.

## How to Run the Application

- To run this application, first you must ensure that you have Python installed on your system.
- Ensure that you have `Flask` and `SQLAlchemy` installed on your system. If not, you can install them using pip: `pip install flask flask_sqlalchemy`
- Go to the project directory.
- Run the application on the terminal: `python3 app.py`
- Open a web browser and go to `http://localhost:5000` to access the Contact Manager. The output will look like this:

![Contact Output](output/contact-output.gif)