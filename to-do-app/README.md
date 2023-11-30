# To-Do Application

## Description

The To-Do Application is a simple web application built with Flask and SQLAlchemy that allows users to manage their tasks efficiently. Users can add new tasks, mark tasks as complete, delete tasks, and view tasks in a sorted order. The application uses SQLAlchemy for database interactions.

## How it Works

- The Flask application is initialized and configured with a secret key and a SQLite database.

- The `Task` class is defined to represent the database model for tasks.

- Routes are established for rendering the home page, adding tasks, toggling task completion status, and deleting tasks.

- The `index` route renders the home page with a list of tasks, showing their titles, descriptions, due dates, and completion status.

## How to Run the Program

- To run this application, first you must ensure that you have Python installed on your system.
- Ensure that you have `Flask` and `SQLAlchemy` installed on your system. If not, you can install them using pip: `pip install flask flask_sqlalchemy`
- Go to the project directory.
- Run the application on the terminal: `python3 app.py`
- Open a web browser and go to http://localhost:5000 to access the access the To-Do application.
- Navigate to the main page to view, add, and manage tasks.
- Use the provided buttons to mark tasks as complete or incomplete and delete tasks.
- Click the "Add Task" button to add new tasks with details.

The output will look like this:

![Task Output](output/task-output.gif)