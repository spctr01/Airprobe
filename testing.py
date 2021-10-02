import unittest
from unittest.mock import patch

import weather
import db
import main
from datetime import datetime, timedelta





class NormalTest(unittest.TestCase):

# database module  unit tests
    def test_validate(self):
        result = db.validate('root','1234')
        self.assertTrue(True)

    def test_user_exists(self):
        result = db.user_exists('admin')
        self.assertTrue(True)
    
    def test_new_user(self):
        result = db.new_user('john','qwe123')
        self.assertTrue('User Created')

    def test_update_user_pass(self):
        cmd = ['-p','newpass']
        result = db.update_user('admin',cmd)
        expected = 'User password Updated Successfully:'
        self.assertTrue(expected)

    def test_update_user(self):
        cmd = ['-u','newuser']
        result = db.update_user('admin',cmd)
        expected = 'Username Updated Successfully:'
        self.assertTrue(expected)


    def test_remove_user(self):
        result = db.remove_user('admin')
        expected = 'User Deleted:'
        self.assertTrue(expected)

    def test_all_users(self):
        result = db.all_users()
        actual = len(result)
        self.assertEqual(actual,2)


#weather  module unit tests--------------
    def test_coordinates(self):
        actual = weather.coordinates('bangalore')
        actual = list(actual)
        expected = [77.6033, 12.9762]
        self.assertListEqual(actual,expected)

    def test_current(self):
        actual = weather.current(77.6033, 12.9762)
        actual = len(actual)
        expected = 116
        self.assertTrue(expected)

    def test_forecaste(self):
        actual = weather.forecaste(77.6033, 12.9762,1)
        actual = len(actual)
        expected = 116
        self.assertTrue(expected)

    def test_weather(self):
        now = datetime.now()
        today =  str(now)
        today = today[5:10]
        command = "city Bangalore {}".format(today)

        actual = weather.weather(command[0], command[1:])
        actual = len(actual)
        expected = 116
        self.assertTrue(expected)




class WrongInputTest(unittest.TestCase):
    
    #wrong city name spelling name error
    def test_coordinates(self):
        actual = weather.coordinates('banglore')
        expected = (None,None)
        self.assertTrue(expected)

    #wrong date input
    def test_weather(self):
        date = '10-2001'
        command = "city Bangalore {}".format(date)
        actual = weather.weather(command[0], command[1:])
        expected = 'Please check the date  or type "--help"'
        self.assertTrue(expected)
        
    #wrong username to delete
    def test_remove_user(self):
        result = db.remove_user('david')
        expected = False
        self.assertFalse(expected)

    #wrong username to update
    def test_update_user(self):
        cmd = ['-u','newpass']
        result = db.update_user('root',cmd)
        expected = 'Cannot change root username'
        self.assertTrue(expected)

    def test_execute_command(self):
        result = main.execute_command('david')
        expected = "Enter a Valid command or type --help"
        self.assertTrue(expected)







if __name__ == "__main__":
    unittest.main()
