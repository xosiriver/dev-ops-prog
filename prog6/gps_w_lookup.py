import requests
import json
import klvn_cls

api_key = "f4cca8a7997c1a94a5a76022e3b2409a"

print("Enter coords to get Weather")
lat = str(input("lat> "))
lon = str(input("lon> "))

URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"


response = requests.get(URL)
data = json.loads(response.text)

location = data["name"]
tempc = klvn_cls.convert_to_c(data["main"]["temp"])
summ = data["weather"][0]["description"]


if location == "":
    print(
        f"The weather at this place in the middle of nowhere is:\n {tempc} degrees celcius"
    )

else:
    print(f"The weather in {location} is:\n {summ}, temp: {tempc} degrees celcius")
