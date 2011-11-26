#!/usr/bin/python

import re
import subprocess
import time
import awrap


#----------------------------------------------------------------------
def get_state():
    """"""
    st, out = subprocess.getstatusoutput('amixer get Master')
    for line in out.split('\n'):
        m = re.match('.* \[(\d+%)\] +\[(.+)\]', line)
        if m:
            if m.groups()[1]=='off':
                return 'off'
            elif m.groups()[1]=='on':
                return m.groups()[0]
    


if __name__ == '__main__':
    
    volumewidget = awrap.TextWidget('volumewidget')
    butts = {}
    butts['{}, 1'] = """function () awful.util.spawn('amixer -q set Master 5%+') end"""
    butts['{}, 3'] = """function () awful.util.spawn('amixer -q set Master 5%-') end"""
    volumewidget.buttons(butts)
    # Update to a initial state
    volumewidget.text('<b><small>'+get_state()+'</small></b>')
    


    

