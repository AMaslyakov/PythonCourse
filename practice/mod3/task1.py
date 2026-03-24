import requests
import json

URL_API = "https://api.openweathermap.org/data/2.5/weather?"

API_KEY = "a572c450317e4915202bd4dcb71b2998"

OUTPUT = """{city:=^50}
Температура: {temp} °C
Ощущается как: {feels} °C
Ветер: {speed} м/с; Направление ветра {deg};{gust}
Давление: {pressure} гПа (норамльное давление 1013.25 гПа)
Влажность: {humidity} %
На небе: {desc}
Координаты: широта {lat}, долгота {lon} 
"""

def weather(city, params):
    URL = URL_API.format(city=city)
    response: requests.Response = requests.get(URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code}


def main():
    print("Введите название города:")
    city = input()

    params = {
        "lang":"ru",
        "appid": API_KEY,
        "q":city,
        "units":"metric",
        "date":"DD-MM-YYYY",
    }

    data = weather(city, params=params)
    
    temp = data.get("main").get("temp")
    feels = data.get("main").get("feels_like")
    wind_speed = data.get("wind").get("speed")
    wind_deg = data.get("wind").get("deg")
    pressure = data.get("main").get("pressure")
    humidity = data.get("main").get("humidity")
    city_name = data.get("name")
    lat = data.get("coord").get("lat")
    lon = data.get("coord").get("lon")


    # Порывы не всегда присуствуют в выдаче 
    gust = data.get("wind").get("gust", "")
    # Если порывов нет то в шаблон вывода добавится пустая строка
    gust_tmp = f" Порывы {gust} м/c" if gust else ""
    # data["wether"] - список объектов, у каждого нужно взять описание 
    description = ", ".join([d.get("description") for d in data.get("weather")])

    print(OUTPUT.format(
        city=city_name,
        temp=temp,
        feels=feels,
        speed=wind_speed,
        deg =wind_deg,
        gust=gust_tmp,
        pressure=pressure,
        humidity=humidity,
        desc=description,
        lat=lat,
        lon=lon,
    ))


if __name__ == "__main__":
    main()
