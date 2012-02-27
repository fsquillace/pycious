'''
Created on Feb 26, 2012

'''

# Importing system functions
from pycious.lib.system import  date, Battery, CPU

# Importing Base widget
from pycious.api.widget import TextWidget, GraphWidget

class BatteryTextWidget(TextWidget):
    def __init__(self, widget_name):
        TextWidget.__init__(self, widget_name)
        
    
    def __call__(self):
        # get the singleton
        batt = Battery()
        self.text = batt()
        pass
    


class DateTextWidget(TextWidget):
    def __init__(self, widget_name):
        TextWidget.__init__(self, widget_name)
        
    
    def __call__(self):
        # get the singleton
        self.text = date()
        
        
class CPUGraphWidget(GraphWidget):
    def __init__(self, widget_name):
        GraphWidget.__init__(self, widget_name)
        
    
    def __call__(self):
        # get the singleton
        cpu = CPU()
        self.add_value(cpu())
