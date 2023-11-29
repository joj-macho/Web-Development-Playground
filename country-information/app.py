from flask import Flask, render_template, request, flash
import requests

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a secret key and database URI
app.config['SECRET_KEY'] = 'a_random_secret_key'  # Replace 'a_random_secret_key' with a secure secret key

REST_COUNTRIES_API_URL = 'https://restcountries.com/v3.1/all'

@app.route('/')
def index():
    '''Get country data from the REST Countries API and renders
    the home page template'''
    countries_data = get_countries()
    return render_template('index.html', countries=countries_data)

def get_countries():
    '''Get information about all countries from the REST Countries API.'''
    try:
        response = requests.get(REST_COUNTRIES_API_URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        countries_data = response.json()

        if isinstance(countries_data, list):
            return countries_data
        else:
            flash('Error retrieving country data.', 'danger')
            return []

    except requests.exceptions.RequestException as e:
        print(f'Error fetching country data: {e}')
        flash('Error fetching country data.', 'danger')
        return []


if __name__ == '__main__':
    app.run(debug=True)
