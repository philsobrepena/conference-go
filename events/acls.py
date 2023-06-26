import requests
import json
from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY

def get_location_photo(city, state):
    try:
        url = "https://api.pexels.com/v1/search"
        params = {
            "query": city + " " + state,
            "per_page": 1
        }
        headers = {
            "Authorization": PEXELS_API_KEY
        }

        res = requests.get(url, params=params, headers=headers)
        unencoded = json.loads(res.content)

        url = unencoded["photos"][0]["url"]

        return {"picture_url" : url}
    except (KeyError, IndexError):
        return {"picture_url": None}

# def get_weather_data(city_name, state_code):
#     url = "http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country code}&limit={limit}&appid={OPEN_WEATHER_API_KEY}"
#     response = requests.get(url)


#     try:
#         lat = json.loads(response.content)[0]["lat"]
#         lon = json.loads(response.content)[0]["lon"]
#     except IndexError:
#         return None

#     url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}"
#     response = requests.get(url)
#     try:
#         description = json.loads(response.content)["weather"][0]["description"]
#         temp = json.loads(response.content)["main"]["temp"]
#         weather = {"temp": temp, "description": description}

#     except IndexError:
#         return None

#     return weather
