#!/usr/bin/python

import unittest

from pycious.api.widget import TextWidget 
from pycious.api.timer import Timer

from pycious.lib.common import execute, WidgetDoesNotExist

# Note: before trying tests you MUST declare the widgets in rc.lua


class WidgetTestCase(unittest.TestCase):
    """"""
              
    def setUp(self):
        self.textwidget = TextWidget('mailwidget')
        
    def tearDown(self):
        self.textwidget.bg = 'trasparent'
        self.textwidget.visible = True
        

    def test_init(self):
        self.assertRaises(WidgetDoesNotExist, TextWidget, 'no_exists')
        
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
        
    def test_visible(self):
        vis= False
        self.textwidget.visible = vis
        self.assertEqual(self.textwidget.visible, vis)
    
    def test_border_color(self):
        color = 'yellow' 
        color_hex = '#ffff00'
        self.textwidget.border_color = color
        self.assertEqual(self.textwidget.border_color, color_hex)
        
    def test_align(self):
        txt = 'right'
        self.textwidget.align = txt
        self.assertEqual(self.textwidget.align, txt)
        
#class TimerTestCase(unittest.TestCase):
#    """"""
#    def setUp(self):
#        self.battery_widget = TextWidget("batterywidget")
#        self.battery_timer = Timer(2)
#        
#    def test_add_signal(self):
#        self.battery_timer.add_signal("battery", lambda: battery(self.battery_widget))
#        self.assert_('battery' in self.battery_timer.__signals)
#
#    def test_remove_signal(self):
#        self.battery_timer.remove_signal("battery")
#        self.assert_('battery' in self.battery_timer.__signals)
#    
#    def test_start(self):
#        self.battery_timer.add_signal("battery", lambda: battery(self.battery_widget))
#        self.battery_timer.start()


if __name__ == "__main__":
    unittest.main()