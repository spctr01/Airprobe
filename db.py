import sqlite3 as sl 

con = sl.connect('user-data.db')
cur = con.cursor()


#checks if table exists or not (users database)
#and if doesnt exist create two demo users
cur.execute(''' SELECT count(name) FROM sqlite_master
                 WHERE type='table' AND name='users' ''')


if cur.fetchone()[0] !=1 :
        cur.execute('''CREATE TABLE 'users'(
                "username"  TEXT,
                "password"  TEXT);''')
        cur.execute("INSERT INTO 'users' VALUES ('root','1234');")
        cur.execute("INSERT INTO 'users' VALUES ('admin','password');")



#validate credentials
def validate(usr, pas):
        sql = "select * from users where username='{}';".format(usr)
        creds = con.execute(sql)

        values = creds.fetchall()
        if values and values[0][1] == pas:
                return True

        return False


#checks if user exist 
def user_exists(usr):
        sql = "select * from users where username='{}';".format(usr)
        val = con.execute(sql)
        if val.fetchone() == None:
                return False

        return True


#create new user
def new_user(usr,pas):

        if user_exists(usr) == True:
                return 'User already exists:'

        sql = "INSERT INTO 'users' VALUES ('{}','{}');".format(usr,pas)
        try:
                cur.execute(sql)
        except Exception as  e:
                print(e)
                return 'User not created:Exception Occured'

        con.commit()
        return 'User Created:'


def update_user(user,cmd):
        user = user

        if user_exists(user) == False:
                return 'check username user not found'


        if cmd[0] == '-p':
                new_pass = cmd[1]
                sql = "UPDATE users SET password ='{}' WHERE username='{}';".format(new_pass,user)
                
                try:
                        cur.execute(sql)
                except Exception as  e:
                        print(e)
                        return "User's passward  not updated"

                con.commit()
                return 'User password Updated Successfully:'



        elif cmd[0] == '-u':
                new_usr = cmd[1]
                sql = "UPDATE users SET username ='{}' WHERE username='{}';".format(new_usr,user)

                try:
                        cur.execute(sql)
                except Exception as  e:
                        print(e)
                        return "Username  not updated"

                con.commit()
                return 'Username Updated Successfully:'
        




#delete user except root user
def remove_user(usr):
        if user_exists(usr) == False or usr=='root':
                return 'User not found:Enter a valid Username / user is "root" '

        sql = "DELETE FROM users WHERE username ='{}';".format(usr)
        cur.execute(sql)
        con.commit()
        return 'User Deleted:'

#returns all the users in database
def all_users():
        cur.execute("SELECT username FROM users")
        print("List of users:")
        for x in cur:
                print(x[0])

con.commit()




