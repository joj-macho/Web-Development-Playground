# app.py
from flask import Flask, render_template, request
import requests

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a secret key
app.secret_key = 'a_random_secret_key'  # Replace with a secure secret key

# Constants for The Movie Database (TMDb) API
API_KEY = "your_api_key"
API_URL = "https://api.themoviedb.org/3"
IMG_PATH = "https://image.tmdb.org/t/p/w1280"

# API endpoints for movie discovery and search
DISCOVER_API = f"{API_URL}/discover/movie?sort_by=popularity.desc&api_key={API_KEY}&page=1"
SEARCH_API = f"{API_URL}/search/movie?api_key={API_KEY}&query="

@app.route('/')
def index():
    '''Renders the index page displaying the top movies.'''
    movies = get_movies(DISCOVER_API)
    return render_template('index.html', movies=movies)

@app.route('/search', methods=['POST'])
def search():
    '''Handles the movie search functionality and renders the index page with search results.'''
    search_term = request.form['search']
    if search_term:
        search_url = SEARCH_API + search_term
        movies = get_movies(search_url)
        return render_template('index.html', movies=movies, search_term=search_term)
    return render_template('index.html', error="Please enter a search term.")

def get_movies(url):
    '''Fetches movie data from the provided URL.'''
    try:
        response = requests.get(url)
        response.raise_for_status()
        movies_data = response.json()
        return movies_data.get('results', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movie data: {e}")
        return []


@app.template_filter('rate_class')
def rate_class(vote):
    '''Determines the CSS class for the movie rating based on the provided vote.'''
    if vote >= 8:
        return "green"
    elif vote >= 5:
        return "orange"
    else:
        return "red"
        

if __name__ == '__main__':
    app.run(debug=True)
