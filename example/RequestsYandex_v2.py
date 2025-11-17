import requests

params={"custname":"alexey",
        "custtel":"838950302"}


headers={
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6",
    "Host": "httpbin.org",
    "Priority": "u=1, i",
    "Referer": "https://httpbin.org/",
    "Sec-Ch-Ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-691a2744-10d79c695a4c452255b5d51d"
  }

response=requests.post("https://httpbin.org/post",headers=headers,data=params)
print(response.status_code)
print(response.json())