from flask import Flask, render_template, request, url_for
import requests

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a secret key
app.secret_key = 'a_random_secret_key'  # Replace with a secure secret key

# OpenWeatherMap API key and base URL to fetch weather information
WEATHER_API_KEY = "your_api_key"
WEATHER_API_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.route('/')
def index():
    '''Renders the home page.'''
    return render_template('index.html', weather_image_url=url_for('static', filename='images/weather-background.jpg'))

@app.route('/weather', methods=['POST'])
def get_weather():
    '''Retrieves weather information based on the submitted city.'''
    city = request.form['city']
    if city:
        weather_data = fetch_weather(city)
        if weather_data:
            weather_image_url = get_weather_image_url(weather_data['weather'][0]['main'])
            return render_template('index.html', weather=weather_data, weather_image_url=weather_image_url)
    return render_template('index.html', error="City not found.")

def fetch_weather(city):
    '''Fetches weather data for the specified city from the OpenWeatherMap API.'''
    try:
        response = requests.get(f"{WEATHER_API_BASE_URL}?q={city}&appid={WEATHER_API_KEY}&units=metric")
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def get_weather_image_url(weather_type):
    '''Returns the URL of an image corresponding to the given weather type.'''
    # Define a mapping of weather types to image URLs
    weather_images = {
        'Clear': url_for('static', filename='images/clear.jpg'),
        'Clouds': url_for('static', filename='images/cloudy.jpg'),
        'Rain': url_for('static', filename='images/rainy.jpg'),
        'Thunderstorm': url_for('static', filename='images/thunderstorm.jpg'),
        'Haze': url_for('static', filename='images/haze.jpg'),
    }

    # Get the image URL for the given weather type
    return weather_images.get(weather_type, url_for('static', filename='images/weather-background.jpg'))


if __name__ == '__main__':
    app.run(debug=True)
