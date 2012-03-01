#!/usr/bin/python

import unittest

from pycious.widgets.web import MailTextWidget, GrssTextWidget


# Note: before trying tests you MUST you must be connected and
# define your credentials in credentials file to test positive cases

class MailTestCase(unittest.TestCase):
    """"""
              
    def setUp(self):
        self.wrong_mail = MailTextWidget('mailwidget', 'user','pass','server','port')
        f = open('credentials')
        user = f.readline()
        password = f.readline()
        f.close()
        self.good_mail = MailTextWidget('mailwidget', user[:-1], password[:-1])
        
        
    def tearDown(self):
        pass
    
    def test_no_connection(self):
        self.wrong_mail()
        self.assertEqual(self.wrong_mail.text, 'na')
        
    def test_visual(self):
        self.good_mail()

class GrssTestCase(unittest.TestCase):
    """"""
              
    def setUp(self):
        self.wrong_grss = GrssTextWidget('rsswidget', 'user','pass')
        f = open('credentials')
        user = f.readline()
        password = f.readline()
        f.close()
        self.good_grss = GrssTextWidget('rsswidget', user[:-1], password[:-1])
        
        
    def tearDown(self):
        pass
    
    def test_no_connection(self):
        self.wrong_grss()
        self.assertEqual(self.wrong_grss.text, 'na')
        
    def test_visual(self):
        self.good_grss()
               

if __name__ == "__main__":
    unittest.main()