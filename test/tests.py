#!/usr/bin/python

import unittest
import awrap

########################################################################
class WidgetTestCase(unittest.TestCase):
    """"""


              
    def setUp(self):
        self.textwidget = awrap.TextWidget('mailwidget')
        
    def test_change_text_bg(self):
        self.textwidget.text("ciao")
        self.textwidget.bg("yellow")
        
    
    



if __name__ == "__main__":
    unittest.main()