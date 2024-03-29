#### **Weather virtual assistant**
# Importing modules
# Helps in pattern matching
import re

# nltk in this helps in lowercase the words
import nltk

# strftime helps to convert the date and time in readable format
from time import strftime

# Helps in importing date and time
import datetime

# Helps in ambiguous times at the end of daylight saving time
import pytz

# Library for OpenWeatherMap
import pyowm

import warnings
warnings.filterwarnings('ignore')

# Building a list of Keywords
lookup_Dict={'greet':{'hello' , 'hi' , 'how do you do' , 'hey', 'hej'},
          'search' : {'search', 'define', 'meaning', 'definition', 'what is', 'tell about', 'tell me about'},
          'weather' : {'current weather' , 'temperature' , 'weather' , 'sunny' , 'rainy' , 'wind' , 
                       'windy' , 'snow' , 'conditions' , 'weather condition' , 'atmospheric condition', 
                       'raining', 'snowy', 'snowing'},
          'ok' : {'okay', 'thanks', 'yeah', 'thank you', 'ok', 'answer', 'good' , 'nice'},   
          'time' : {'time','clock'}}

# Welcome the User

def welcome():
    sweden =  pytz.timezone("Europe/Stockholm")

    #Get our local zone time
    se_time = datetime.datetime.now(sweden)

    #Generating the time in hour, using a 24-hour clock
    # 1) 6 - 12 (Morning)
    # 2) 12- 16 (Afternoon)
    # 3) 16 - 19(EVening) 
    time = int(se_time.strftime('%H'))
    if 6<= time < 12:
      print('Good morning!!!')
    elif 12 <= time < 16:
      print('Good afternoon!!!')
    elif 16<= time <19:
      print('Good evening!!!')
    else:
      print('Good night!!!')
    print("This is Weather Virtual Assistant(Communication) using Openweathermaps API. Welcome and nice to meet you!!!")
    return

# Once welcoming the user. Greet and assist the user to the chat box!!
def greetFunc():

    print("Hello!!! I'm your chatbot and I'm here to help you")
    print("I'll try to answer your questions regarding Weather")
    print("Please enter your question below asking about weather details. If you want to quit, please enter 'quit'")
    return

# Generating the weather 
def getWeather():

    # Helps in entering the city name 
    city = input("Please enter the city : ")    

    #  Gerated my own free API key for weather
    APIKEY="8021b029ea5f1780e724706fcf461833"    

    # The API connection is stored in the OWM variable in pyowm library and builtin functions are used to make the code shorter to get the weather of the place
    OpenWMap=pyowm.OWM(APIKEY)
    mgr = OpenWMap.weather_manager() #The manager object is used to query weather data, including observations, forecasts and so on
    observation = mgr.weather_at_place(city) #weather forecast for the specified location

    # Details for weather
    weather = observation.weather 
    # Other details can be searched are
    # observation.detailed_status        
    # observation.wind()               
    # observation.humidity                
    # observation.temperature('celsius')  
    # observation.rain                    
    # observation.heat_index           
    # observation.clouds  

    temp_dict_celsius = weather.temperature('celsius')
    status = weather.detailed_status

    print('\nCurrent weather in %s is %s. The temperature is %0.2f degree celcius and it feels like %0.2f degree celcius.\n' % (city, status, temp_dict_celsius['temp'],temp_dict_celsius['feels_like']))
    
    # Checks if the API key was valid and returns true if we have valid weather data available. If true then we will get other details of weather like wind/conditions
    while (True): 
      choice = input("\nAny other information regarding the weather like the \n   1)minimum and maximum temperature\n   2)wind speed\n   3)humidity\nEnter the number to get approriate answer. If you want to return to the main chat room, enter 'return'\n")
      if(choice == '1'):
          print("\nMaximum temperature is %0.2f degree celcius\n" %(temp_dict_celsius['temp_max']))
          print("\nMinimum temperature is %0.2f degree celcius\n" %(temp_dict_celsius['temp_min']))
      if(choice == '2'):
          print("\nThe speed of the wind is %0.2f meters per sec with %d degrees\n" %(observation.weather.wind()['speed'],observation.weather.wind()['deg']))
      if(choice == '3'):
          print("\nHumidity measured is %d\n" %(observation.weather.humidity))
      if(choice.lower() == 'return' ):
          return

# 1) Welcome the user
welcome()
# Program loop
# Asks the user for the city  
while (True):  
    # changes any input string to lowercase sentence
    user_input = input().lower()
    # If user does'nt want weather they can quit the weather virtual assistant
    if user_input == 'quit': 
        print ("Thank you for visiting.")
        break    
    
    matched_intent = None 
    key='unclear' 
    for intent,pattern in lookup_Dict.items():
        for p in pattern:
            if(p in user_input):
                key = intent  
    # 2) Greeting the user
    if(key == 'greet'):
        greetFunc()
    # 3) Weather forecast
    if(key == 'weather'):
        getWeather()
    if(key == 'ok'):
        print('Thank you.. Anything more to help you?')
    if(key == 'unclear'):
        print('Sorry!! Could you please repeat that?')

