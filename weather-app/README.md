# Weather App

## Description

The Weather App is a simple Flask web application that allows users to check the current weather in a city. It leverages the OpenWeatherMap API to fetch weather data and displays it alongside a background image that reflects the current weather condition. The application provides a visually appealing and informative way to stay updated on weather conditions.

## How It Works

- **Homepage**: The user is initially presented with a search box on the homepage. They can enter the name of a city and submit the form.

- **Weather Information**: Upon submitting the form, the application fetches the weather information for the entered city using the OpenWeatherMap API. The weather details, including temperature, weather type, and min/max temperature, are displayed.

- **Background Image**: The background image of the page changes dynamically based on the weather type. For instance, a clear sky will have a different background image compared to a rainy or cloudy sky.

### How to Run the Application

```bash
python app.py
```

Visit `http://localhost:5000` in your web browser to access the Weather Application.

The output of the program will look like this:

<p>
  <img src="output/london.png" alt='London Output'>
  <img src="output/mahikeng.png" alt='Mahikeng Output'>
</p>

<p>
  <img src="output/singapore.png" alt='Singapore Output'>
  <img src="output/newyork.png" alt='New-York Output'>
</p>

#### Credits for Images

- **weather-background.jpg**: Photo by [Tom Barrett](https://unsplash.com/@wistomsin?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/clouds-during-golden-hour-hgGplX3PFBg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
  
- **cloudy.jpg**: Photo by [Daoudi Aissa](https://unsplash.com/@dannyeve?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/cumulus-clouds-Pe1Ol9oLc4o?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
  
- **thunderstorm.jpg**: Photo by [Michelle McEwen](https://unsplash.com/@michellem18?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/black-and-white-abstract-painting-sCrqMG2f6qo?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

- **haze.jpg**: Photo by [Tobias Tullius](https://unsplash.com/@tobiastu?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/trees-covered-with-fog-RhjVGxILcqE?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

- **rainy.jpg**: Photo by [Valentin Müller](https://unsplash.com/@wackeltin_meem?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/dew-drops-on-glass-panel-bWtd1ZyEy6w?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

- **clear.jpg**: Photo by [Dave Hoefler](https://unsplash.com/@iamthedave?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/blue-ocean-photography-ELXbHhzVFO0?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)