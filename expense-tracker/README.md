# Expense Tracker Application

## Description

The Expense Tracker Application is a web-based tool that allows users to record and manage their expenses. Users can add new expenses, edit existing ones, and delete expenses they no longer need. The application uses Flask for the backend and SQLite for the database to store expense records.

## How it Works

- Start by setting up the Flask application including importing required modules, configuration for the database and creating an instance of the SQLAlchemy database.

- The `Expense` class is defined, representing the model of an expense with attributes like `description`, `amount`, `date`, and `category`.

- The SQLite database is created and the necessary table for expenses is defined.

- Various routes are established to handle different functionalities:
    - **Index Route** (`/`): Displays the list of employees.
    - **Add Expense Route** (`/add`): Allows the user to add a new expense.
    - **Edit Expense Route** (`/edit/int:id`): Allows the user to edit an existing expense.
    - **Delete Expense Route** (`/delete_employee/int:id`): Allows the user to delete an existing expense.

- The routes above render HTML templates that serve as the views, providing the user interface for the corresponding functionality. Users can interact with the application by filling out forms to add or edit expense details.

## How to Run the Program

- To run this application, first you must ensure that you have Python installed on your system.
- Ensure that you have `Flask` and `SQLAlchemy` installed on your system. If not, you can install them using pip: `pip install flask flask_sqlalchemy`
- Go to the project directory.
- Run the application on the terminal: `python3 app.py`
- Open a web browser and go to http://localhost:5000 to access the Expense Tracker. The output will look like this:

![Expense Output](output/expense-output.gif)