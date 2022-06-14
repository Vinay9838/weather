# WeatherReport

---

>Please execute following command in sequence for seamless configuration

### Activate virtual environment

````shell
virtualenv -p python3 /home/weather/weather-env
source /home/weather/weather-env/bin/activate
````

### Application dependencies
```shell
pip install -r requirements.txt
```

### Application setup

```shell
./manage.py migrate
```

### initial config

```shell
./manage.py import_city
```

### Openweather api

Visit <a href="https://home.openweathermap.org/">Open Weather</a> page and signup. An API key will be generated copy that api.

In your root project dir create a file `.env` and paste the api key.

```shell
WEATHER_API_KEY=4297c971407f29ca2f
```

---
Once the setup done, run your server  `./manage.py runserver` . You will be able to search the weather forecasting
citywise . Forecasting data will be of next 5 days 3 hours basis.

### Result


![Weather GIF](https://github.com/Vinay9838/weather/blob/master/static/assets/image/weather.gif?raw=true)
