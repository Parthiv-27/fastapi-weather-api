# FastAPI Weather API 🌤️

A simple FastAPI-based Weather API that fetches real-time weather data from OpenWeatherMap and provides JSON responses.

## 🔧 Requirements
- Python 3.x
- FastAPI
- Uvicorn
- Requests

## 🚀 How to Run
1. Clone the repository
git clone https://github.com/yourusername/weather-api.git
cd weather-api

2. Install dependencies:
pip install -r requirements.txt

3. Run the FastAPI server
python -m uvicorn main:app --reload

4. Open in browser:
http://127.0.0.1:8000/docs


## 🌍 Example API Call
http://127.0.0.1:8000/weather/Toronto
Expected JSON response:
```json
{
  "city": "Toronto",
  "country": "CA",
  "temperature": -6.42,
  "feels_like": -13.42,
  "humidity": 69,
  "weather": "clear sky",
  "wind_speed": 9.26
}

🛠️ Features
✅ Fetches real-time weather data
✅ Provides structured JSON response (City, Country, Temperature, Humidity, Weather, Wind Speed)
✅ Error handling for incorrect city names
✅ Interactive API docs using Swagger UI

📝 Notes
Ensure you have an OpenWeatherMap API Key before running the API.
If you encounter a 401 Unauthorized error, verify your API Key and replace it in main.py.
For more details, check out the OpenWeatherMap API Documentation.

📜 License
This project is open-source and available under the MIT License.

🌟 Contributions & Feedback
💡 Found a bug? Want to contribute? Feel free to open an issue or submit a pull request!
If you find this project helpful, give it a ⭐ on GitHub!