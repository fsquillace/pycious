'''
Created on Feb 27, 2012

'''

# Importing web function
from pycious.lib.web import Gmail

# Importing Base widget
from pycious.api.widget import TextWidget, GraphWidget


class GmailTextWidget(TextWidget):
    def __init__(self, widget_name):
        TextWidget.__init__(self, widget_name)
        
    
    def __call__(self):
        # get the singleton
        gmail = Gmail()
        self.text = gmail()
    