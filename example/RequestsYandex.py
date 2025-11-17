import requests

params = {
    "ll": "37.677751,55.757718",
    "spn": "0.016457,0.00619",
    "l": "map"
}
response=requests.get("https://static-maps.yandex.ru/1.x/", params=params)
print(response.status_code)
with open("map.png", "wb") as file:
    file.write(response.content)

