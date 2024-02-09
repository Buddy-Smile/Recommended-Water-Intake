from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = 'PUT YOUR OWN OPEN WEATHER API IN'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    temperature_celsius = data['main']['temp']
    humidity = data['main']['humidity']

    # Calculate recommended water intake based on temperature and humidity
    recommended_water_intake_ml = 2000  # Default value

    # Adjust water intake based on temperature
    if temperature_celsius > 25:
        recommended_water_intake_ml += (temperature_celsius - 25) * 20  # Increase intake by 20ml for each degree above 25°C

    # Adjust water intake based on humidity
    if humidity > 70:
        recommended_water_intake_ml += (humidity - 70) * 10  # Increase intake by 10ml for each percentage point above 70%

    return jsonify({'temperature': temperature_celsius, 'humidity': humidity, 'water_intake_ml': recommended_water_intake_ml})

if __name__ == '__main__':
    app.run(debug=True)
