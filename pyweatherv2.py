import os
import sys
import argparse
import requests
import json

api_secret = os.environ.get('WEATHER_STACK_SECRET')

if api_secret == None: #checking to see if WEATHER_STACK_SECRET is nill 
    print("You do not yet have a token set for a 'WEATHER_STACK_SECRET' enviornment variable, please set one up now")

parser = argparse.ArgumentParser(description="Return the current weather and condition of a specified area")

parser.add_argument('Location', metavar='location',
type=str, help = 'add a location(ex: Grand Rapids)')

parser.add_argument('--unit', metavar='unit', #optional unit argument 
type =str, help = 'choose a unit, f(fahrenheit), s(scientific) or leave the default metric')

args = parser.parse_args()

location = args.Location #setting location to the argument location

if args.unit != None:
    unit = args.unit
    r = requests.get('http://api.weatherstack.com/current?access_key='+api_secret+'& query='+location+ '& units=' +unit)

else:
    r = requests.get('http://api.weatherstack.com/current?access_key='+api_secret+'& query='+location)

data = r.content
weather_json = json.loads(data)
current = weather_json['current']



print("In "+location+" it is: " + str(current['temperature'])+" degrees Celsius and")

def displayWeatherTable(parsedJson): # function to print weather table to prevent clutter
    print("""
=========================
| Feels Like: {} |   
| Wind Speed: {} |
| Wind Direction: {} | 
| Humidity:  {} |
| Percipitation: {} |
| Cloud Cover: {} |
| Visibility: {} | 
=========================
    """.format(parsedJson['feelslike'], parsedJson['wind_speed'], parsedJson['wind_dir'],
    parsedJson['humidity'], parsedJson['precip'], parsedJson['cloudcover'], parsedJson['visibility']))       

if str(current['weather_descriptions'][0]) == "Partly cloudy":#checking weather description(Ex: clear, sunny, cloudy)

    print("""\033[1;37m CLOUDY
                            .-~~~-.
                    .- ~ ~-(       )_ _ _.
                  /                       ~ -.
                 |                          \\
                 \                          .'
                   \ ~- . _____________ . -~ 
                    """)
    displayWeatherTable(current)
elif str(current['weather_descriptions'][0]) == "Sunny":

    print("""033[1;33m SUNNY
      ;   :   ;
   .   \_,!,_/   ,
    `.,'     `.,'
     /         \\
~ -- :         : -- ~
     \         /
    ,'`._   _.'`.
   '   / `!` \   `
      ;   :   ; 
                    """)
    displayWeatherTable(current)
elif str(current['weather_descriptions'][0]) == "Clear":
    
 #in the next line I am changing the output color with the escape code "\033" setting the style to 1(normal) and setting the color to 34 which is blue
    print("""\033[1;34m 
      _                 
     | |                
  ___| | ___  __ _ _ __ 
 / __| |/ _ \/ _` | '__|
| (__| |  __/ (_| | |   
 \___|_|\___|\__,_|_|   
 """)
    displayWeatherTable(current)


