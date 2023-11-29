from flask import Flask, render_template, request, flash
import requests

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a secret key
app.config['SECRET_KEY'] = 'a_random_secret_key'  # Replace with a secure secret key

# API URL
API_URL = "https://api.github.com/users/"

@app.route('/')
def index():
    '''Renders the main page where users can input a GitHub username.'''
    return render_template('index.html')

@app.route('/user', methods=['POST'])
def get_user():
    '''Handles the form submission and fetches GitHub user data.'''
    username = request.form['username']
    
    if username:
        user_data = get_user_data(username)
        
        if user_data:
            return render_template('index.html', user=user_data)
        else:
            flash("User not found.", 'danger')
    else:
        flash("Please enter a username.", 'warning')

    return render_template('index.html')

def get_user_data(username):
    '''Fetches GitHub user data and the user's top repositories.'''
    try:
        user_response = requests.get(API_URL + username)
        user_response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        user_data = user_response.json()

        repos_response = requests.get(API_URL + username + "/repos")
        repos_response.raise_for_status()

        repos_data = repos_response.json()

        return {'user': user_data, 'repos': repos_data[:10]}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:  # User not found
            print(f"User not found: {username}")
            return {'user': None, 'repos': []}
        else:
            print(f"HTTPError: {e}")
            return None


if __name__ == '__main__':
    app.run(debug=True)
