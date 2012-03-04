# Importing apps functions
from pycious.lib.apps import volume
# Importing Base widget
from pycious.api.widget import TextBoxWidget

from pycious.lib.common import getstatusoutput

# TODO Create a dictionary widget


volumewidget = TextBoxWidget('volumewidget')
butts = {}
butts['{}, 1'] = """function () awful.util.spawn('amixer -q set Master 5%+') end"""
butts['{}, 3'] = """function () awful.util.spawn('amixer -q set Master 5%-') end"""
volumewidget.buttons(butts)
# Update to a initial state
volumewidget.text('<b><small>'+volume()+'</small></b>')




class VolumeTextWidget(TextBoxWidget):
    def __init__(self, widget_name):
        TextBoxWidget.__init__(self, widget_name)
        
        table = {((), 1):self.f_inc, ((), 3):self.f_dec}
        self.buttons(table) 

# TODO try to complete callback function problem

    def f_inc(self):
        getstatusoutput('amixer -q set Master 5%+')
        self()
            
    def f_dec(self):
        getstatusoutput('amixer -q set Master 5%-')
        self()
    
    def __call__(self):
        vol, st = volume()
        if st == 'off':
            self.text = st
        else:
            self.text = str(vol)
            
            
    
