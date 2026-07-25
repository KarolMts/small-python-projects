import requests
import argparse
import sys


def fetch(url, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
        

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('city')
    args = parser.parse_args()
    
    try:
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        geo_data = fetch(geo_url, {'name':args.city, 'count':1})
        
        # .get() -> None, if key 'results' doesn't exist, or if it exists but as an empty list
        # the .get() method wan't throw an errror like []-access
        if not geo_data.get('results'):
            sys.exit(f"There is no city named: {args.city}")
            
        city = geo_data['results'][0]['name']
        lat = geo_data['results'][0]['latitude']
        lon = geo_data['results'][0]['longitude']

        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_data = fetch(weather_url)
        
    except requests.exceptions.HTTPError as err:
            sys.exit(f"Sorry, the response status code is: {err.response.status_code} ")
    except requests.exceptions.RequestException:
            sys.exit("The server doesn't respond.")
            
    temp =  weather_data['current_weather']['temperature']
    units = weather_data['current_weather_units']['temperature']
    
    print(f"The temperature in {city} is {temp} {units}.")
    

if __name__ == "__main__":
    main()