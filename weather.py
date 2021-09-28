import os
import requests , json
import datetime
from datetime import datetime, timedelta

api_key = '0b2bf94be643dd6af52cce220e8390d4'



#convert unix date in api response to simple date format
def date(unix):
    date = datetime.fromtimestamp(int(unix)).strftime('%m-%d')
    return date

#this block make a list for date in next week
now = datetime.now()
week = []
for x in range(7):
    d = now + timedelta(days=x)
    week.append(d.strftime("%m-%d"))



# return latitide and longitude of place
def coordinates(city):
    r =requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city,api_key))
    data = r.json()

    try:
        lon = data['coord']['lon']
        lat = data['coord']['lat']
        return (lon, lat)
    except Exception as e:
        print( "----Please make sure data is correct---")

    

# prints current weather and condition of place 
def current(lat, lon):
    #r =requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city,api_key))
    r = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&units={}&appid={}'.format(lat,lon,'imperial',api_key))
    data = r.json()
    
    humidity = data['current']['humidity']
    pressure = data['current']['pressure']
    wind_speed = data['current']['wind_speed']
    wind_deg = data['current']['wind_deg']
    avg_temp = data['current']['temp']
    uv = data['current']['uvi']

    os.system('clear')
    print("Hummidity: {}\n Pressure: {} hPa\n Wind Speed: {}\n Wind Degree: {}\n Average Temperature: {}\n UV Index: {} "
                                                            .format( humidity,pressure,wind_speed,wind_deg,avg_temp,uv))

# if date is in next week
def forecaste(lat, lng,idx):
    r =requests.get('http://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}&units=imperial'.format(lat,lng,api_key))
    data = r.json()
    data = data['daily'][1]

    
    humidity = data['humidity']
    pressure = data['pressure']
    wind_speed = data['wind_speed']
    wind_deg = data['wind_deg']
    avg_temp = data['temp']['day']
    uv = data['uvi']

    os.system('clear')
    print("Hummidity: {}\n Pressure: {} hPa\n Wind Speed: {}\n Wind Degree: {}\n Average Temperature: {}\n UV Index: {} "
                                                            .format( humidity,pressure,wind_speed,wind_deg,avg_temp,uv))



def weather(inf, cmd):
    today =  str(now)
    today = today[5:10]

# if user enters city name it gets the coordinates of city from coordinate funcation.
    if inf =='city':
        date = cmd[1]
        try:
            lon, lat = coordinates(cmd[0])
        except Exception as e:
            print("type help for more")
    else:  
        lon, lat = cmd[0], cmd[1]
        date = cmd[2]
    
# if wether is in  next 7 days
    if date == today:
        try:
            weather_data = current(lat,lon) 
        except Exception as e:
            return "Make sure data entered is correct"

    elif date in week:
        index = week.index(date)
        try:
            weather_data = forecaste(lat,lon,index) 
        except Exception as e:
            return "Make sure data entered is correct"
    else:
        return 'Please check the date and commands or type "help"'

    
    return weather_data
