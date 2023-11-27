from flask import Flask, render_template, request, flash
import string
import secrets


# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a secret key
app.secret_key = 'a_random_secret_key'  # Replace with a secure secret key

@app.route('/')
def index():
    '''Render the home page.'''
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    '''Generate a random password.'''
    try:
        length = int(request.form['length'])
        use_symbols = 'use_symbols' in request.form
        use_digits = 'use_digits' in request.form
        use_uppercase = 'use_uppercase' in request.form

        characters = string.ascii_lowercase

        if use_symbols:
            characters += "!@#$%^&*()_-+=<>?"
        if use_digits:
            characters += string.digits
        if use_uppercase:
            characters += string.ascii_uppercase

        if not characters:
            flash('Please select at least one character type (letters, numbers, or symbols).', 'danger')
            return render_template('index.html')

        password = ''.join(secrets.choice(characters) for _ in range(length))
        flash('Password generated successfully.', 'success')
        return render_template('index.html', password=password)
    except ValueError:
        flash('Invalid input. Please enter a valid length (a positive integer).', 'danger')
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
