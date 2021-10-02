import os
import requests , json
import datetime
from datetime import datetime, timedelta

api_key = '0b2bf94be643dd6af52cce220e8390d4'



#current month-date
now = datetime.now()
today =  str(now)
today = today[5:10]
#make a list for date in next week
week = []
for x in range(7):
    dates = now + timedelta(days=x)
    week.append(dates.strftime("%m-%d"))



#convert unix date in api  to simple date format
def date(unix):
    return datetime.fromtimestamp(int(unix)).strftime('%m-%d')
    



# returns latitide and longitude of place
def coordinates(city):
    r =requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city,api_key))
    data = r.json()

    try:
        lon = data['coord']['lon']
        lat = data['coord']['lat']
        return (lon, lat)

    except Exception as e:
        print( "Please check the city name make sure spelling is correct")
    
    return (None, None)

    



# prints current weather of place 
def current(lat, lon):
    r = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&units={}&appid={}'.format(lat,lon,'imperial',api_key))
    data = r.json()
    
    humidity = data['current']['humidity']
    pressure = data['current']['pressure']
    wind_speed = data['current']['wind_speed']
    wind_deg = data['current']['wind_deg']
    avg_temp = data['current']['temp']
    uv = data['current']['uvi']

    os.system('clear')
    return("\n Hummidity: {}\n Pressure: {} hPa\n Wind Speed: {}\n Wind Degree: {}\n Average Temperature: {}\n UV Index: {} "
                                                            .format( humidity,pressure,wind_speed,wind_deg,avg_temp,uv))





# gives weather forecaste of 1 week 
def forecaste(lat, lng,idx):
    r =requests.get('http://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}&units=imperial'.format(lat,lng,api_key))
    data = r.json()
    data = data['daily'][idx]


    humidity = data['humidity']
    pressure = data['pressure']
    wind_speed = data['wind_speed']
    wind_deg = data['wind_deg']
    avg_temp = data['temp']['day']
    uv = data['uvi']

    os.system('clear')
    return("\n Hummidity: {}\n Pressure: {} hPa\n Wind Speed: {}\n Wind Degree: {}\n Average Temperature: {}\n UV Index: {} "
                                                            .format( humidity,pressure,wind_speed,wind_deg,avg_temp,uv))






def weather(inf, cmd):
    if inf =='city':  # if city name it gets the coordinates of city from coordinate function.
        date = cmd[1]
        lon, lat = coordinates(cmd[0])   

    else: 
        date = cmd[2] 
        lon, lat = cmd[0], cmd[1]
        
    
# if wether is in  next 7 days
    if date == today:
        try:
            return current(lat,lon) 
        except Exception as e:
            return '''Make sure "city_name" or 
                    "latitude/longitude" entered is correct'''

    elif date in week:
        index = week.index(date)
        try:
            return forecaste(lat,lon,index) 
        except Exception as e:
            return '''Make sure "city_name" or 
                    "latitude/longitude" entered is correct'''

    else:
        return ('Please check the date  or type "--help"')

    
    
