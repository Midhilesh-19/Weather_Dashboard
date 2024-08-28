from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your own Weatherbit API key
API_KEY = '0dd5674345434d089a2a9d636feaa5d5'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        url = f'https://api.weatherbit.io/v2.0/current?city={city}&key={API_KEY}'
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200 and data.get('data'):
            weather_data = data['data'][0]
            weather = {
                'city': city,
                'temperature': weather_data['temp'],
                'description': weather_data['weather']['description'],
                'icon': weather_data['weather']['icon'],
            }
        else:
            weather = {'error': 'City not found'}
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
