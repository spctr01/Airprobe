import argparse
import os
import sys

 
import db
import weather 

#parser
parser = argparse.ArgumentParser(prog = 'airprobe',description = 'Welcome to Airprobe')
parser.add_argument('usr', metavar='UserName', type=str, help ='Enter Username' )
parser.add_argument('pas', metavar='Password', type=str, help ='Enter Password')


credentials = parser.parse_args()
login_status = db.validate(credentials.usr, credentials.pas)

if login_status == False:
    sys.exit('Login failed: Please check credentials')
else:
    print("WELCOME TO AIRPROBE \n <Type help to know more>")


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

    elif command[0] =='coord':
        data= weather.weather(command[0], command[1:])
        print(data)
    
    elif command[0] =='city':
        data= weather.weather(command[0], command[1:])
        print(data)

    else:
        print("Enter a Valid command or type help")
        

# Takes contineous input from user.
while True:
    command = input('->').lower()
   
    if command == 'exit':
        print('Bye.......')
        break

    elif command == 'help':
        print('help')

    elif command == '':
        print('Enter Something! or type help ')

    else:
        execute_command(command)




