import sqlite3 as sl 
import hashlib
import os



con = sl.connect('user-data.db')
cur = con.cursor()



#create hash of password
def hash_pas(pas):
        h = hashlib.md5(pas.encode())
        password_hash = h.hexdigest()

        return password_hash



#checks if table exists or not (users database)
#and if doesnt exist create two demo users
cur.execute(''' SELECT count(name) FROM sqlite_master
                 WHERE type='table' AND name='users' ''')

if cur.fetchone()[0] !=1 :
        p1 = hash_pas('1234')
        p2 = hash_pas('password')

        cur.execute('''CREATE TABLE 'users'("username" TEXT,    "password" TEXT);''')
        cur.execute("INSERT INTO 'users' VALUES ('root','{}');".format(p1))
        cur.execute("INSERT INTO 'users' VALUES ('admin','{}');".format(p2))







#validate credentials
def validate(usr, pas):
        sql = "select * from users where username='{}';".format(usr)
        creds = con.execute(sql)

        values = creds.fetchall()
        password = hash_pas(pas)

        if values and values[0][1] == password: return True
        return False





#returns true if user already exists in database
def user_exists(usr):
        sql = "select * from users where username='{}';".format(usr)
        val = con.execute(sql)

        if val.fetchone() == None: return False
        return True




#create new user
def new_user(usr,pas):
        if user_exists(usr) == True: return 'User already exists:'

        password = hash_pas(pas)
        sql = "INSERT INTO 'users' VALUES ('{}','{}');".format(usr,password)
        cur.execute(sql)
        con.commit()

        return 'User Created:'




# Updates username and password
def update_user(user,cmd):
        user = user
        if user_exists(user) == False: return 'check username user not found'

        if cmd[0] == '-p':
                new_pass = cmd[1]
                new_pass = hash_pas(new_pass)
                sql = '''UPDATE users SET password ='{}' 
                        WHERE username='{}';'''.format(new_pass,user)
                cur.execute(sql)
                con.commit()

                return 'User password Updated Successfully:'


        elif cmd[0] == '-u':
                if user =='root': 
                        return 'Cannot change root username'

                new_usr = cmd[1]
                sql = "UPDATE users SET username ='{}' WHERE username='{}';".format(new_usr,user)
                cur.execute(sql)
                con.commit()

                return 'Username Updated Successfully:'
        




#delete user except root user
def remove_user(usr):
        if user_exists(usr) == False or usr=='root': return ('User not found:Enter a valid Username / user is "root" ')

        sql = "DELETE FROM users WHERE username ='{}';".format(usr)
        cur.execute(sql)
        con.commit()
        return 'User Deleted:'




#returns all the users in database
def all_users():
        user_list = []
        cur.execute("SELECT username FROM users")
        print("List of users:")
        
        for x in cur:
                user_list.append(x[0])

        return user_list



con.commit()




