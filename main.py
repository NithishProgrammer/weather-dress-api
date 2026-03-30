from fastapi import FastAPI
import requests

app = FastAPI()

@app.get('/city')
def getcity(city : str):
    api_id = ""     #Replace it with your API KEY
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_id
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        weather = data['weather'][0]['main'].lower()
        if weather == "rain" :
            return {"Suggesting" : "Take an unmbrella or wear a Rain coat"}
        
        elif weather == "thunderstorm":
            return {"Suggesting" : "Stay indoor if possible" }
        
        elif weather == "clear":
            return {"Suggesting" : "Nothing.. Just light sunscreen" }
        
        elif weather == "drizzle":
            return {"Suggesting" : "A light hoodie or windbreaker." }
        
        elif weather == "clouds":
        
            return {"Suggesting" : "Good for a walk, maybe a light sweater." }
        
        elif weather == "haze":
            return {"Suggesting" : "Normal outdoor clothing, but keep your eyes protected from grit/dust." , "Precation" : "Visibility is reduced. Drive carefully and wear a mask if you have respiratory sensitivities" }