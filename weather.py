# weather.py
#from typing import List, Dict

def get_weather(city):
    # Simulating weather data (Contains type issues)
    print("Getting weather data for " + city)
    return {'city': city, 'temperature': 25, 'condition': "Sunny"}

#run this one first and it will return an error
def format_weather(weather_data):
    return "The weather in " + weather_data['city'] + " is " + weather_data['temperature'] + "°C with " + weather_data['condition'] + " conditions."

#Run this next with the temperature converted to string for output
#def format_weather(weather_data):
    #return "The weather in " + weather_data['city'] + " is " + str(weather_data['temperature']) + "°C with " + weather_data['condition'] + " conditions."

# Example usage (contains deliberate issues)
weather_data = get_weather("Sydney") 
print(format_weather(weather_data))