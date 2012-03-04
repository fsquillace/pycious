#!/usr/bin/python

from __future__ import division


from pycious.widgets.system import BatteryTextWidget, DateTextWidget, CPUGraphWidget
from pycious.widgets.web import MailTextWidget, GrssTextWidget

from pycious.api.timer import Timer
from pycious.api.widget import ImageBoxWidget


if __name__ == "__main__":

    # DEBUG (remember to backup your own rc.lua):
    # $ cp rc.lua ~/.config/awesome/
    # $ PYTHONPATH=.. python -O rc.py


    # Retrieve all available widgets defined in rc.lua
    # You MUST define the widget in rc.lua before
    
    # 
    f = open('credentials')
    username = f.readline()[:-1]
    password = f.readline()[:-1]
    
    battery_widget = BatteryTextWidget("battery_widget")
    clock_widget = DateTextWidget("clock_widget")
    image_widget = ImageBoxWidget("image_widget")
    mail_widget = MailTextWidget("mail_widget", username, password)
    grss_widget = GrssTextWidget("grss_widget", username, password)
    cpu_widget = CPUGraphWidget('cpu_widget')


################### MAIL WIDGET ########################
    mail_timer = Timer(5)
    mail_timer.add_signal("mail", mail_widget)    
    mail_timer.start()
########################################################

################### GRSS WIDGET ########################
    grss_timer = Timer(7)
    grss_timer.add_signal("mail", grss_widget)    
    grss_timer.start()
########################################################

################### DATE WIDGET ########################
    clock_timer = Timer(60)
    clock_timer.add_signal("date", clock_widget)
    clock_timer.start()
########################################################

################### BATTERY WIDGET #####################
    battery_timer = Timer(11)
    battery_timer.add_signal("battery", battery_widget)
    battery_timer.start()
########################################################    

################### CPU GRAPH WIDGET ###################
    cpu_widget.set_width(50)
    cpu_widget.set_background_color("#494B4F")
    cpu_widget.set_color("#FF5656")
    cpu_widget.set_gradient_colors({ "#FF5656", "#88A175", "#AECF96" })
    cpu_timer = Timer(1)
    cpu_timer.add_signal('cpu', cpu_widget)
    cpu_timer.start()
########################################################