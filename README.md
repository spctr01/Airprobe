# Airprobe

Command Line Interface (CLI) solely build in python without any extra framework to Provides weather information .
Gives weather forecaste of 7 days.


---------
## Installation and Usage
Download this repository  cd into directory and run

```
python3 main.py 
```

By default 2 users are created "root" and "admin" with password "1234" and "password" respectively 

--------


## Testing 

  testing.py contains the  16 Test cases for the program.
  #### run
  ```
  python3 testing.py
  ```
  
  to run the unit tests

----
## Directory structure
 ```
Airprove
    |
    |--main.py  :  takes cli inputs
    |
    |--weather.py  : uses openweather api for weather inforamtion
    |
    |--db.py  : rhandles the users database
    |
    |--user-data.db : sqlite dabase (python inbuild)
    |
    |--__init__.py :  __init__ file
    |
    |-- testing.py : unit tests for the program
    |
    |-- help.txt : contains help menu
```
------
## Commands Help Menu

```
exit :  Exit the Program
--help : help menu
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
                  
       "date shoud be current of in next 7 days as openweather free api provides only 7 days forecaste  "
```

