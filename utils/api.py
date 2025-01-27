import datetime
import requests
from utils.debug import info


def get_weather() -> float:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 55.737026,
        "longitude": 37.611577,
        "hourly": "temperature_2m"
    }
    response = requests.get(url, params=params)
    info(response.json())
    data = response.json()['hourly']

    dtime = datetime.datetime.now().strftime("%Y-%m-%dT%H:00")
    index = data['time'].index(dtime)
    temp = data['temperature_2m'][index]
    print(temp, index)
    return float(temp)