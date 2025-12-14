import requests

def get_weather(location):
    api_key = "7a025f9c5cf60ca36e1933575caad706"  
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        city = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description']
        
        print(f"\nWeather in {city}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition.capitalize()}")
    else:
        print("Location not found. Please enter a valid city or ZIP code.")

def main():
    location = input("Enter city name or ZIP code: ").strip()
    if location:
        get_weather(location)
    else:
        print("Invalid input. Please enter a city name or ZIP code.")

if __name__ == "__main__":
    main()