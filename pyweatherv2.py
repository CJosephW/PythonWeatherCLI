import os
import sys
import argparse
import requests
import json

api_secret = os.environ.get('WEATHER_STACK_SECTRET')

parser = argparse.ArgumentParser(description="Return the current weather and condition of a specified area")

parser.add_argument('Location', metavar='location',
type=str, help = 'add a location(ex: Grand Rapids)')

args = parser.parse_args()

location = args.Location #setting location to the argument location

r = requests.get('http://api.weatherstack.com/current?access_key='+api_secret+'& query='+location)
data = r.content
weather_json = json.loads(data)
current = weather_json['current']

print("In "+location+" it is: " + str(current['temperature'])+" degrees Celsius and")

if str(current['weather_descriptions'][0]) == "Partly cloudy":#checking weather description(Ex: clear, sunny, cloudy)

    print("""\033[1;37m CLOUDY
                            .-~~~-.
                    .- ~ ~-(       )_ _ _.
                  /                       ~ -.
                 |                          \\
                 \                          .'
                   \ ~- . _____________ . -~ 
                    """)
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
elif str(current['weather_descriptions'][0]) == "Clear":
 #in the next line I am changing the output color with the escape code "\033" setting the style to 1(normal) and setting the color to 34 which is blue
    print("""\033[1;34m CLEAR
      _                 
     | |                
  ___| | ___  __ _ _ __ 
 / __| |/ _ \/ _` | '__|
| (__| |  __/ (_| | |   
 \___|_|\___|\__,_|_|   
 """)
