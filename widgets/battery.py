#!/usr/bin/python3

import subprocess
import awrap
import time
import sys
import re

if __name__=='__main__':

    batterywidget = awrap.TextWidget("batterywidget")
    
    while True:
        
        (s, o) = subprocess.getstatusoutput('acpi -b')
        if s!=0:
            raise EnvironmentError('Error: acpi appears not installed.')
        
        if o=='':
            batterywidget.visible('false')
        
        timeout = 61
        m = re.match('Battery (\d+):[ a-zA-Z,]*(\d+)%\.*',o)
        if m:
            st = (int)(m.groups()[1])
            if st==100:
                batterywidget.visible('false')
                batterywidget.bg('trasparent')
                timeout = 61
            elif st>=60:
                batterywidget.visible('true')
                batterywidget.bg('green')
                timeout = 31
            elif st>=20:
                batterywidget.visible('true')
                batterywidget.bg('yellow')
                timeout = 17
            else:
                batterywidget.visible('true')
                batterywidget.bg('red')
                timeout = 11
           
            batterywidget.text('<b><small>'+str(st)+'%</small></b>')
            
        time.sleep(timeout)