# Unit Converter

The Unit Converter is a web application built using Flask that allows users to convert values between different units of length and mass. Users can input a value, select the category (length or mass), and choose the units for conversion. The application provides instant results and maintains a history of recent conversions.

This web application is an implementation of this [Unit Converter CLI](https://github.com/joj-macho/Pythological-Playground/tree/main/converter), providing a more user-friendly interface for unit conversions.

## How It Works

- The Flask application is initialized and configured with a secret key.

- Conversion options are defined for length and mass, including various units such as millimeters, centimeters, meters, kilometers, inches, feet, yards, miles for length, and grams, kilograms, milligrams, pounds, ounces, tons for mass.

- A history of recent conversions is maintained to display the latest conversions.

- Two routes are defined:
   - The index route (`/`) renders the home page where users can input conversion details.
   - The convert route (`/convert`) handles the form submission, performs the conversion, and renders the result along with the conversion history.

- The `perform_conversion` function calculates the result based on the selected category, unit from, and unit to, using predefined conversion factors.

## How to Run the Program

- To run this application, first you must ensure that you have Python installed on your system.
- Ensure that you have `Flask` installed on your system. If not, you can install them using pip: `pip install flask`
- Go to the project directory.
- Run the application on the terminal: `python3 app.py`
- Open a web browser and go to http://localhost:5000 to access the access the Unit Converter Application.

The output will look like this:

![Converter Output](output/converter-output.gif)