# Employee Manager

## Description

The Employee Manager is a web application that allows users to manage employee information. Users can view a list of employees, add new employees, edit existing employee details, and delete employees. The application uses Flask for the backend and SQLite for the database to store employee information.


## How it Works

- The program starts by importing the necessary modules and libraries (<code>Flask</code>, <code>SQLAlchemy</code>, <code>os</code>).

- Then the Flask application is set up, including configuration for the database and creating an instance of the SQLAlchemy database.

- The <code>Employee</code> class is defined, representing the model of an employee with attributes like <code>name</code>, <code>position</code>, <code>department</code>, and <code>salary</code>.

- The program then creates the SQLite database and the necessary table for employees.

- The program then creates various routes for different functionalities, these routes act as the controller, handling the interactions between the user and the model:
    - <strong>Index Route</strong> (<code>/</code>): Displays the list of employees.
    - <strong>Add Employee Route</strong> (<code>/add_employee</code>): Allows the user to add a new employees.
    - <strong>Edit Employee Route</strong> (<code>/edit_employee/int:employee_id</code>): Allows the user to edit an existing employees.
    - <strong>Delete Employee Route</strong> (<code>/delete_employee/int:employee_id</code>): Allows the user to delete an existing employees.

- The routes above render HTML templates that serve as the views, providing the user interface for the corresponding functionality. Users can interact with the application by filling out forms to add or edit employee details.


## How to Run the Program

- To run this application, first you must ensure that you have Python installed on your system.

- Ensure that you have <code>Flask</code> and <code>SQLAlchemy</code> installed on your system. If not, you can install them using pip:

<pre>pip install flask flask_sqlalchemy</pre>

- Go to the project directory.
- Run the application on the terminal:
<pre>python3 app.py</pre>

- Open a web browser and go to http://localhost:5000 to access the Employee Manager. The output will look like this:

<p align="center">
  <img src="output/employee-output.gif" alt='Employee Output'>
</p>
