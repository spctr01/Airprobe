import argparse
import os
import sys

import db
import weather 


#reading help command file
with open('help.txt') as f:
    help_command = f.read()



def login_validator():
    login_status = False
    while login_status == False:
        username = input('Enter UserName: ')
        password = input('Enter Password: ')
        login_status = db.validate(username, password)

        if login_status == True: 
            os.system('clear')
            print("\n WELCOME TO AIRPROBE \n <Type --help to know more>")
            
        else: 
            print('Login failed: Please check credentials')
        








#execute the commands / users inputs
def execute_command(cmd):
    command =cmd.split()
    status = ''
    
    if command[0] == 'create' and len(command) ==3:
        username = command[1]
        passward = command[2]
        status = db.new_user(username,passward)
         
    elif command[0]== 'delete' and len(command) ==2:
        status = db.remove_user(command[1])
        
    elif command[0]== 'all' and len(command) == 1:
        db.all_users()

    elif command[0]== 'update' and len(command)==4 :
        status = db.update_user(command[1], command[2:])
        
    elif command[0] =='coord' and len(command)==4:
        status= weather.weather(command[0], command[1:])
    
    elif command[0] =='city' and len(command)==3:
        status= weather.weather(command[0], command[1:])

    else:
        print("Enter a Valid command or type --help")


    print(status)


if __name__ == "__main__":
    login_validator()
# Takes contineous input from user.
    while True:
        command = input('\n->').lower()
    
        if command == 'exit': break
        elif command == '--help':  print(help_command)  
        else: execute_command(command)




