# Real Estate Listings Application

## Description

The Real Estate Listings Application is a web-based tool that allows users to view, add, edit, and delete property listings. It uses Flask for the backend and SQLite for the database to store property records.

## How it Works

- Start by setting up the Flask application including importing required modules, configuration for the database and creating an instance of the SQLAlchemy database.

- A `Property` class is defined to represent the model of a property with attributes such as `title`, `description`, `price`, and `image_url`.

- The SQLite database is created and the necessary table for property listings is defined.

- Various routes are defined to handle different functionalities:
    - **Index Route** (`/`): Displays all property listings.
    - **Propery Route** (`/property/int:property_id`): Displays a specific property listing.
    - **Add Listing Route** (`/add_property`): Allows the user to add a new property.
    - **Edit Listing Route** (`/edit_property/int:property_id`): Allows the user to edit an existing property.
    - **Delete Listing Route** (`/delete_property/int:property_id`): Allows the user to delete an existing property.

- The routes render HTML templates that serve as the views, providing the user interface for the corresponding functionality. Users can interact with the application by filling out forms to add or edit real estate listings.

## How to Run the Program

- To run this application, first you must ensure that you have Python installed on your system.
- Ensure that you have `Flask` and `SQLAlchemy` installed on your system. If not, you can install them using pip: `pip install flask flask_sqlalchemy`
- Go to the project directory.
- Run the application on the terminal: `python3 app.py`
- Open a web browser and go to http://localhost:5000 to access the Real Estate Listings Application.

The output will look like this:

![Property Output](output/property-output.gif)