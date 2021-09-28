import argparse
import os
import sys

import db
import weather 

#parser
parser = argparse.ArgumentParser(prog = 'airprobe',description = '<---Welcome to Airprobe--->')
parser.add_argument('usr', metavar='UserName', type=str, help ='Enter Username' )
parser.add_argument('pas', metavar='Password', type=str, help ='Enter Password')

command_help = '''
    ----------Commands Help Menu----------

    exit :  Exit the Program
    --coorhelp : help menu

    [Users creation, deletion, Updation]

    1. create : to create new user 
                eg: create username password

    2. delete : delete a user
                eg: delete username

    3. all : view all the users 

    4. update : update user and password
        |
        |------update username
        |        eg: update username -u new_username
        | 
        |------ update password
        |         eg : update username -p new_password

    [Weather information]

    1: city : weather by city name
             [ city <city_name> <date(month-date)>  ]
              eg: city Delhi 09-28  

    2: Coord : weather by coordinates
                [coord  latitude longitude data]
                  eg: coord 28.644800 77.216721 09-28

    '''

#gets username and password from arguments
credentials = parser.parse_args()
login_status = db.validate(credentials.usr, credentials.pas)


if login_status == False:
    sys.exit('Login failed: Please check credentials')
else:
    print("WELCOME TO AIRPROBE \n <Type --help to know more>")



#execute the commands / users inputs
def execute_command(cmd):
    command =cmd.split()
    
    if command[0] == 'create' and len(command) ==3:
        username , passward = command[1], command[2]
        status = db.new_user(username,passward)
        print(status)
         
    elif command[0]== 'delete' and len(command) ==2:
        user = command[1]
        status = db.remove_user(user)
        print(status)

    elif command[0]== 'all' and len(command) == 1:
        db.all_users()

    elif command[0]== 'update' and len(command)==4 :
        status = db.update_user(command[1], command[2:])
        print(status)

    elif command[0] =='coord' and len(command)==4:
        data= weather.weather(command[0], command[1:])
    
    elif command[0] =='city' and len(command)==3:
        data= weather.weather(command[0], command[1:])

    else:
        print("Enter a Valid command or type help")
        

# Takes contineous input from user.
while True:
    command = input('->').lower()
   
    if command == 'exit':
        print('Bye.......')
        break

    elif command == '--help':
        print(command_help)
        
        

    elif command == '':
        print('Enter Something! or type help ')

    else:
        execute_command(command)




