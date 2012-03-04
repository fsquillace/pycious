# Importing system functions
from pycious.lib.system import date, battery, cpu, \
    network_statistics, mem_usage

# Importing Base widget
from pycious.api.widget import TextBoxWidget
# This should be "from pycious.api.awful.widget import Graph"
from pycious.api.awful.widget.graph import Graph

class BatteryTextWidget(TextBoxWidget):
    def __init__(self, widget_name):
        TextBoxWidget.__init__(self, widget_name) 
    
    def __call__(self):
        self.text = str(battery()[1])

class DateTextWidget(TextBoxWidget):
    def __init__(self, widget_name):
        TextBoxWidget.__init__(self, widget_name)
    
    def __call__(self):
        self.text = date()
        
class CPUGraphWidget(Graph):
    def __init__(self, widget_name):
        Graph.__init__(self, widget_name)
    
    def __call__(self):
        self.add_value(cpu())
