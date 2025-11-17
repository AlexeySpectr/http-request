import requests
import json
from API_TOKEN import API_TOKEN


params={"q":"53.1202,45.0016","key":API_TOKEN}

response_weather=requests.get("http://api.weatherapi.com/v1/current.json?",params=params)

response=requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.status_code)
# print(response.json())
x=response.json()
print(f"numder posts-{x[99]["userId"]}\n number id-{x[99]["id"]}\n title-{x[99]["title"]}\n boby-{x[99]["body"]}")
# print(json.dumps(response.json(), indent=4, ensure_ascii=False))
response2=requests.get("https://jsonplaceholder.typicode.com/users")
y=response2.json()
print(json.dumps(response2.json(), indent=4, ensure_ascii=False))
print(f"lat:{y[0]["address"]["geo"]["lat"]}\n lng:{y[0]["address"]["geo"]["lng"]}\n Company-name:{y[0]["company"]["name"]}")
print(response_weather.status_code)
print(response_weather.json())
x=response_weather.json()
print(x["current"]["temp_c"])