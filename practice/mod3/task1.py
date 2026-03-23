import requests
import json

URL_API = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

API_KEY = "a572c450317e4915202bd4dcb71b2998"

def weather(city):
    URL = URL_API.format(city=city, api_key=API_KEY)
    r: requests.Response = requests.get(URL)
    return r.status_code

def main():
    print("Введите назввание города:")
    city = input()
    code = weather(city)
    print(code)
    

if __name__ == "__main__":
    main()
