# GitHub User Information Viewer

## Description

The GitHub Profile Viewer is a Flask web application that allows users to search for GitHub profiles using a username. The app fetches data from the GitHub API to display the user's information, including their name, bio, followers, following, and top repositories.

This app is a web-based alternative to the [GitHub Profile Viewer CLI program](https://github.com/joj-macho/Pythological-Playground/tree/main/github-profile-viewer). While the CLI program allows direct interaction through the command line, the Flask app provides a user-friendly interface for exploring GitHub profiles.

## How it Works

- The Flask application is initialized and configured with a secret key.

- The main route (`/`) renders the home page where users can input a GitHub username.

- The `/user` route handles the form submission, fetches GitHub user data using the GitHub API, and renders the home page with the user's information. If the user is found, it displays the user's profile information, including their name, bio, followers, following, and avatar.

- The `get_user_data` function sends HTTP requests to the GitHub API to retrieve user data and the user's top repositories. It handles errors and flashes messages for user feedback.

## How to Run the Application

- To run this application, make sure you have Python installed on your system.
- Ensure that Flask is installed. If not, you can install it using pip: `pip install flask`
- Navigate to the project directory.
- Run the application in the terminal: `python3 app.py`
- Open a web browser and go to http://localhost:5000 to access GitHub User Information Viewer.
- Enter a GitHub username in the form, and the app will display the user's information.

The output will look like this:

![Github Profile Output](output/github-output.png)