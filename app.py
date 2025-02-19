from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# OpenWeatherMap API Key (Replace with your API key)
API_KEY = "5c71b6c6c2bb329b9a7ce59cf353ea36"

# Function to fetch weather data
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].capitalize(),
            "icon": data["weather"][0]["icon"]
        }
        return weather
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        weather = get_weather(city)
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
