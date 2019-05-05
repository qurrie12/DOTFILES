import requests

class Weather:
    def __init__(self):
        self.weather = None
        self.temperature = None
        self.humidity = None
        self.sunrise = None
        self.sunset = None

    def __str__(self):
        return str(int(self.temperature - 273.15)).upper() + "°C" + " - " + self.weather.upper()

city = "Lubliniec"
url = "http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=b0465a23b8ab35929574a5e83f7cc4a5" % city
response = requests.get(url)
data = response.json()

weather = Weather()
weather.weather = data['weather'][0]['description']
weather.temperature = data['main']['temp']
weather.humidity = data['main']['humidity']
weather.sunrise = data['sys']['sunrise']
weather.sunset = data['sys']['sunset']

print(weather)
