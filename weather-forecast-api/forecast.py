import os #import os variable
import requests

def get_forecast(city_name, units = 'metric'):
    api_key = os.environ.get('OPENWEATHER_API_KEY') #get the api key from the environment variable
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units={units}'
    r = requests.get(url)
    content = r.json()
    forecasts = content['list']
    city_name = content['city']['name']
    results = []
    with open('forecast.txt', 'a') as file: #create the txt file and append the results to it. with 'a' it will append the results to the file instead of overwriting it
        for forecast in forecasts:
            outcome = f"City: {city_name} \nTime: {forecast['dt_txt']} \nTemperature: {forecast['main']['temp']} \nCondition: {forecast['weather'][0]['description']}\n"
            results.append(outcome) 
            file.write(outcome) #write the outcome to the txt file
    return results #to be able to print the results in the console as well
print('\n'.join(get_forecast('London')))