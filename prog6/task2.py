import json
import requests
import klvn_cls

api_key = "f4cca8a7997c1a94a5a76022e3b2409a"
location = str(input("Enter location:"))

try:
    with open("UK.json", "r") as file:
        UKdata = json.load(file)

except KeyError:
    print("Location not found")

for place in UKdata["places"]:
    if place["name"] == location:
        lon = place["x"]
        lat = place["y"]

URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

response = requests.get(URL)
data = json.loads(response.text)

tempc = klvn_cls.convert_to_c(data["main"]["temp"])
summ = data["weather"][0]["description"]


print(f"The weather in {location} is:\n {summ}, temp: {tempc} degrees celcius")
