document.getElementById('weatherForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    fetch('/weather', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const temperatureCelsius = data.temperature;
        const temperatureFahrenheit = (temperatureCelsius * 9/5) + 32;
        const humidity = data.humidity;
        const waterIntake = data.water_intake_ml;
        document.getElementById('result').innerHTML = `Temperature: ${temperatureCelsius.toFixed(2)}°C (${temperatureFahrenheit.toFixed(2)}°F)<br>Humidity: ${humidity}%<br>Recommended Water Intake: ${waterIntake} ml`;
    });
});
