# Movie Application

The Movie App is a simple Flask web application that allows users to explore top movies and search for specific movies. It utilizes The Movie Database (TMDb) API to fetch movie data and present it in an organized manner.

The movie poster images used in this application are sourced from [The Movie Database (TMDb)](https://www.themoviedb.org/).

## How it Works

- **Constants**
    - `API_KEY`: The API key required for accessing TMDb API.
    - `API_URL`: The base URL for TMDb API.
    - `IMG_PATH`: The base URL for retrieving movie poster images.
    - `DISCOVER_API`: The API endpoint for discovering top movies.
    - `SEARCH_API`: The API endpoint for searching movies based on user input.

- **Routes**
    - `/`: Renders the index page displaying top movies.
    - `/search` (POST): Handles the movie search functionality and renders the index page with search results.

- **Functions**
    - `get_movies(url)`: Fetches movie data from the provided URL using the `requests` library. Returns a list of movies.
    - `rate_class(vote)`: Determines the CSS class for the movie rating based on the provided vote.

- **Filters**
    - `rate_class`: A template filter that uses the `rate_class` function to determine the CSS class for movie ratings.

### How to Run the Application

- Make sure you have a valid TMDb API key.
- Run the Flask application using `python app.py`.
- Open a web browser and navigate to `http://127.0.0.1:5000/` to view the top movies.
- Use the search bar to look for specific movies.

The output of the program will look like this:

![Movie App Output](output/movies-output.png)
![Movie App Output 2](output/movies-2-output.png)