from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import pyowm
import yaml
import sys
sys.path.insert(0,"../")

# https://pypi.org/project/weather-api/
#from weather import Weather, Unit


class ActionGetWeather(Action):
    def name(self):
        return 'action_get_weather'

    def run(self, dispatcher, tracker, domain):

        cred = yaml.load(open('cred.yml'))
        owm = pyowm.OWM(cred['pywon_key'])  # You MUST provide a valid API key

        #weather = Weather(unit=Unit.CELSIUS)
        gpe = ('Auckland', tracker.get_slot('GPE'))[bool(tracker.get_slot('GPE'))]
        observation = owm.weather_at_place(gpe)
        #result = weather.lookup_by_location(gpe)
        if observation:
            w = observation.get_weather()
            humid = str(w.get_humidity())
            temp_mean = str(w.get_temperature('celsius')['temp'])
            wind_speed = str(w.get_wind()['speed'])
            #condition = result.condition
            #city = result.location.city
            #country = result.location.country
            dispatcher.utter_message('It\'s ' + temp_mean + '°C with humidity ' + humid +
                                     ', and wind speed ' + wind_speed + '.')
        else:
            dispatcher.utter_message('We did not find any weather information for ' + gpe + '. Search by a city name.')
        return