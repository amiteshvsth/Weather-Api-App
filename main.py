import requests
import json
import win32com.client as wincom

city = input("Enter the name of city")
url = f"https://api.weatherapi.com/v1/current.json?key=30209a51404d48f296a75300232603&q={city}&aqi=no"

r = requests.get(url)
print(r.text)
print(type(r.text))
dic = json.loads(r.text)
w = dic["current"]["temp_c"]
speak = wincom.Dispatch("SAPI.SpVoice")
speak.Speak(f"the current weather in {city} is {w}")
