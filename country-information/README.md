# REST Countries Information Viewer

## Description

The REST Countries Information Viewer is a web-based application built with Flask that retrieves information about countries from the REST Countries API. Users can view details about various countries, including their names, capitals, populations, and more. The application is designed to provide a simple and interactive way to explore country data.

## How it Works

- The Flask application is configured, and an instance of the application is created.

- The application uses the REST Countries API (`https://restcountries.com/v3.1/all`) to fetch information about all countries.

- The main route (`/`) is defined to handle requests and retrieve country data from the API. The data is then rendered in the home page template (`index.html`).

- The `get_countries` function sends a GET request to the REST Countries API and retrieves information about all countries. It handles potential errors and flashes a message if there is an issue retrieving the data.

## How to Run the Application

- To run this application, make sure you have Python installed on your system.
- Ensure that Flask is installed. If not, you can install it using pip: `pip install flask`
- Navigate to the project directory.
- Run the application in the terminal: `python3 app.py`
- Open a web browser and go to http://localhost:5000 to access the REST Countries Information Viewer.
- The application will fetch data from the REST Countries API and display it on the home page.

The output will look like this:

![Country Data Output](output/country-output.png)
