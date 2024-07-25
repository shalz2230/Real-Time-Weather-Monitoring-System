import requests

def fetch_weather_data(location):
    # Replace 'your_api_key' with a valid API key from OpenWeatherMap
    api_key = 'your_api_key'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    # Construct the request URL
    request_url = f"{base_url}?q={location}&appid={api_key}&units=metric"

    # Send the request and get the response
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            'temperature': data['main']['temp'],
            'weather_conditions': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather_info
    else:
        return None

def display_weather_data(weather_info):
    if weather_info:
        print(f"\nWeather Information for the entered city:")
        print(f"------------------------------------------")
        print(f"Temperature: {weather_info['temperature']}°C")
        print(f"Weather Conditions: {weather_info['weather_conditions']}")
        print(f"Humidity: {weather_info['humidity']}%")
        print(f"Wind Speed: {weather_info['wind_speed']} m/s")
        print(f"------------------------------------------\n")
    else:
        print("Failed to retrieve weather data. Please check the location and try again.")

def main():
    while True:
        location = input("Enter the city name (or 'exit' to quit): ")
        if location.lower() == 'exit':
            print("Exiting the weather monitoring system. Goodbye!")
            break
        weather_info = fetch_weather_data(location)
        display_weather_data(weather_info)

if __name__ == '__main__':
    main()

