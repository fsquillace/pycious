#!/usr/bin/python

import unittest

from pycious.lib.web import Mail, Grss


# Note: before trying tests you MUST you must be connected and
# define your credentials in credentials file to test positive cases

class MailTestCase(unittest.TestCase):
    """"""
              
    def setUp(self):
        self.wrong_mail = Mail('user','pass','server','port')
        f = open('credentials')
        user = f.readline()
        password = f.readline()
        f.close()
        self.good_mail = Mail(user[:-1], password[:-1])
        
        
    def tearDown(self):
        pass
    
    def test_no_connection(self):
        self.assertEqual(self.wrong_mail(), -1)
        
    def test_integer(self):
        ur = self.good_mail()

        self.assertGreaterEqual(ur, 0)


class GrssTestCase(unittest.TestCase):
    """"""
              
    def setUp(self):
        self.wrong_grss = Grss('user','pass')
        f = open('credentials')
        user = f.readline()
        password = f.readline()
        f.close()
        self.good_grss = Grss(user[:-1], password[:-1])
        
        
    def tearDown(self):
        pass
    
    def test_no_connection(self):
        self.assertEqual(self.wrong_grss(), -1)
        
    def test_integer(self):
        self.assertGreaterEqual(self.good_grss(), 0)
        

if __name__ == "__main__":
    unittest.main()