from flask import Flask, request, render_template, jsonify
import requests
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
API_KEY = os.getenv("API_KEY")
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        if not city:
            return render_template('index.html', error="Please enter a city name.")
        # Fetch weather data from API
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        try:
            response = requests.get(url)
            data = response.json()
            if response.status_code != 200:
                return render_template('index.html', error=data.get("message", "City not found."))

            weather_info = {
                "city": data["name"],
                "temperature": round(data["main"]["temp"]),  # Rounded for cleaner output
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"] }

            return render_template('index.html', weather=weather_info)

        except Exception:
            return render_template('index.html', error="Error fetching weather data.")

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
