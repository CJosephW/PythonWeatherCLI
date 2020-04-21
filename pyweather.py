import click
import requests
import os
import json
import argparse

api_secret = os.getenv("WeatherStackApiKey")


@click.command()
@click.option('--when', default="now", help='set time of day')
@click.option('--where', prompt = "set location", help = "Set your location")
@click.option('--auth', default = api_secret, prompt = "set WeatherStackAPI key", help = 'set api access key from stackweatherAPI')
def getWeather(when, where, auth):

    r = requests.get('http://api.weatherstack.com/current?access_key='+auth+'& query='+where)
    data = r.content
    weather_json = json.loads(data)
    temp = weather_json['current']
    
    click.echo("In "+where+" it is: " + str(temp['temperature'])+" degrees Celsius")
    
    if str(temp['weather_descriptions'][0]) == "Partly cloudy":
        click.echo("and Partly Cloudy")
        click.echo("""\  
                            .-~~~-.
                    .- ~ ~-(       )_ _ _.
                  /                       ~ -.
                 |                          \\
                 \                          .'
                   \ ~- . _____________ . -~ 
                    """)
    elif str(temp['weather_descriptions'][0]) == "Sunny":
        click.echo("And Sunny!!!")
        click.echo("""\
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
if __name__ == '__main__':
    getWeather()