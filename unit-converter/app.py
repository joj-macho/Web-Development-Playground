from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Define conversion options
conversion_options = {
    'length': ['mm', 'cm', 'm', 'km', 'inch', 'foot', 'yard', 'mile'],
    'mass': ['g', 'kg', 'mg', 'lb', 'oz', 'ton'],
}

# Maintain a history of recent conversions
conversion_history = []

# Route to render the index page
@app.route('/')
def index():
    '''Render the home page for the unit converter app.'''
    return render_template('index.html', units_from=[], units_to=[])

# Route to handle the form submission and conversion
@app.route('/convert', methods=['POST'])
def convert():
    '''Convert each category to the specified units and return the result.'''
    category = request.form['category']
    value = float(request.form['value'])
    unit_from = request.form['unit_from']
    unit_to = request.form['unit_to']

    units_from = conversion_options.get(category, [])
    units_to = conversion_options.get(category, [])

    # Perform the conversion
    result = perform_conversion(value, unit_from, unit_to, category)

    # Append the current conversion to the history
    conversion_history.append({'category': category, 'value': value, 'unit_from': unit_from, 'unit_to': unit_to, 'result': result})

    # Keep only the last 5 conversions in the history
    if len(conversion_history) > 5:
        conversion_history.pop(0)

    return render_template('index.html', result=result, history=conversion_history, units_from=units_from, units_to=units_to)

def perform_conversion(value, unit_from, unit_to, category):
    '''Perform the conversion based on the selected category and return the result.'''
    # Define conversion factors for each category
    conversion_factors = {
        'length': {
            'mm': 1000,
            'cm': 100,
            'm': 1,
            'km': 0.001,
            'inch': 39.3701,
            'foot': 3.28084,
            'yard': 1.09361,
            'mile': 0.000621371
        },
        'mass': {
            'g': 1,
            'kg': 0.001,
            'mg': 1000,
            'lb': 0.00220462,
            'oz': 0.035274,
            'ton': 1e-6
        }
    }

    # Perform the conversion based on the selected category
    if category in conversion_factors:
        try:
            factor_from = conversion_factors[category][unit_from]
            factor_to = conversion_factors[category][unit_to]

            result = (value / factor_from) * factor_to
            return f'Result: {value} {unit_from} = {result:.5f} {unit_to}'
        except KeyError:
            return 'Invalid units.'

    return 'Invalid category.'


if __name__ == '__main__':
    app.run(debug=True)
