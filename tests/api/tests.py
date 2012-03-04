#!/usr/bin/python

import unittest

from pycious.api.widget import TextBoxWidget 
from pycious.api.timer import Timer

from pycious.lib.common import execute, WidgetDoesNotExist

# Note: before trying tests you MUST declare the widgets in rc.lua


class WidgetTestCase(unittest.TestCase):
    """"""
              
    def setUp(self):
        self.textwidget = TextBoxWidget('mailwidget')
        
    def tearDown(self):
        self.textwidget.visible = True

    def test_init(self):
        self.assertRaises(WidgetDoesNotExist, TextBoxWidget, 'no_exists')
        
    def test_visible(self):
        vis= False
        self.textwidget.visible = vis
        self.assertEqual(self.textwidget.visible, vis)




class TextWidgetTestCase(unittest.TestCase):
    """"""
              
    def setUp(self):
        self.textwidget = TextBoxWidget('mailwidget')
        
    def tearDown(self):
        self.textwidget.bg = 'trasparent'
        self.textwidget.visible = True
        self.textwidget.width = 0
        
    def test_text(self):
        txt = 'ciao'
        self.textwidget.text = txt
        self.assertEqual(self.textwidget.text, txt)
        
    def test_bg(self):
        color = 'yellow' 
        color_hex = '#ffff00'
        self.textwidget.bg = color
        self.assertEqual(self.textwidget.bg, color_hex)
    
    def test_width(self):
        widt= 40
        self.textwidget.width = widt
        self.assertEqual(self.textwidget.width, widt)
        
    def test_border_width(self):
        widt= 40
        self.textwidget.border_width = widt
        self.assertEqual(self.textwidget.border_width, widt)
    
    def test_border_color(self):
        color = 'yellow' 
        color_hex = '#ffff00'
        self.textwidget.border_color = color
        self.assertEqual(self.textwidget.border_color, color_hex)
        
    def test_align(self):
        txt = 'right'
        self.textwidget.align = txt
        self.assertEqual(self.textwidget.align, txt)
        
      
#class ImageBoxWidgetTestCase(unittest.TestCase):
#    """"""
#              
#    def setUp(self):
#        self.textwidget = TextBoxWidget('imagewidget')
#        
#    def tearDown(self):
#        self.textwidget.bg = 'trasparent'
#
#    def test_init(self):
#        self.assertRaises(WidgetDoesNotExist, TextBoxWidget, 'no_exists')
#        
#        
#    def test_image(self):
#        vis= False
#        self.textwidget.visible = vis
#        self.assertEqual(self.textwidget.visible, vis)
        
        


if __name__ == "__main__":
    unittest.main()