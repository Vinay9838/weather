from django.shortcuts import render
from django.views.generic import View
from .forms import CityForm
import requests
from weatherapp import formatting,measurables
from datetime import datetime
from weather.settings import WEATHER_API_KEY

WEATHER_BASE = "http://api.openweathermap.org/"
WEATHER_END_POINT = "{}data/2.5/forecast".format(WEATHER_BASE)


WEATHER_GIF = {
"Snow":"https://mdbgo.io/ascensus/mdb-advanced/img/snow.gif",
"Clouds":"https://mdbgo.io/ascensus/mdb-advanced/img/clouds.gif",
"Fog":"https://mdbgo.io/ascensus/mdb-advanced/img/fog.gif",
"Rain":"https://mdbgo.io/ascensus/mdb-advanced/img/rain.gif",
"Clear":"https://mdbgo.io/ascensus/mdb-advanced/img/clear.gif",
"Thunderstorm":"https://mdbgo.io/ascensus/mdb-advanced/img/thunderstorm.gif",
"default":"https://mdbgo.io/ascensus/mdb-advanced/img/clear.gif"
}


class TemperatureView(View):
    context = {}

    def time_from_timezone(self,value,timezone):
        return datetime.fromtimestamp(value+timezone)

    def get_date_obj(self,date_value):
        return datetime.strptime(date_value, '%Y-%m-%d %H:%M:%S')

    def get(self,request):
        self.context = {}
        self.context['form'] = CityForm()
        return render(request,'weather/home.html',self.context)

    def post(self,request):
        form = CityForm(request.POST)
        weather_list = []
        if form.is_valid():
            if form.cleaned_data and form.cleaned_data.get('name',None):
                city_obj = form.cleaned_data.get('name',None)
                print(city_obj)
                city_name = city_obj.name
                api = "{}?q={}&APPID={}".format(WEATHER_END_POINT,city_name,WEATHER_API_KEY)
                try:
                    result = requests.get(api).json()
                    self.context['city'] = result.get('city')
                    self.context['city']['sunrise'] = self.time_from_timezone(result.get('city').get('sunrise'),result.get('city').get('timezone'))
                    self.context['city']['sunset'] = self.time_from_timezone(result.get('city').get('sunset'),result.get('city').get('timezone'))

                    for weather in result.get('list'):
                        data_dict = {}
                        data_dict['temp_min'] = measurables.kelvin_to_celsius(weather.get('main').get('temp_min'))
                        data_dict['temp_max'] = measurables.kelvin_to_celsius(weather.get('main').get('temp_max'))
                        data_dict['humidity'] = measurables.kelvin_to_celsius(weather.get('main').get('humidity'))
                        data_dict['pressure'] = weather.get('main').get('pressure')
                        data_dict['main'] = weather.get('weather')[0].get('main')
                        data_dict['description'] = weather.get('weather')[0].get('description')
                        data_dict['wind'] = measurables.metric_wind_dict_to_km_h(weather.get('wind'))
                        data_dict['link'] = WEATHER_GIF.get(data_dict.get('main'))
                        data_dict['datetime'] = self.get_date_obj(weather.get('dt_txt'))
                        data_dict['font'] = 'text-dark' if data_dict['main'] == 'Clear' else 'text-white'
                        data_dict['visibility'] = weather.get('visibility',None)
                        data_dict['rain'] = weather.get('rain',None).get('3h',None) if weather.get('rain',None) else None
                        weather_list.append(data_dict)

                    self.context['forecast'] = weather_list

                except Exception as e:
                    print(e)
        self.context['form'] = form
        return render(request,'weather/home.html',self.context)


