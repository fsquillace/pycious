import re
import subprocess
import time
import pycious.widget

from pycious.common import getstatusoutput

# TODO Create a dictionary widget


def volume():
    """"""
    st, out = getstatusoutput('amixer get Master')
    for line in out.split('\n'):
        m = re.match('.* \[(\d+%)\] +\[(.+)\]', line)
        if m:
            if m.groups()[1]=='off':
                return 'off'
            elif m.groups()[1]=='on':
                return m.groups()[0]
    


#if __name__ == '__main__':
#    
#    volumewidget = awrap.TextWidget('volumewidget')
#    butts = {}
#    butts['{}, 1'] = """function () awful.util.spawn('amixer -q set Master 5%+') end"""
#    butts['{}, 3'] = """function () awful.util.spawn('amixer -q set Master 5%-') end"""
#    volumewidget.buttons(butts)
#    # Update to a initial state
#    volumewidget.text('<b><small>'+volume()+'</small></b>')
    

