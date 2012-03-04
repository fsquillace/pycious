#!/usr/bin/python

from __future__ import division


from pycious.widgets.system import BatteryTextWidget, DateTextWidget, CPUGraphWidget
from pycious.widgets.web import MailTextWidget

from pycious.api.timer import Timer


if __name__ == "__main__":

    # Retrieve all available widgets defined in rc.lua
    # You MUST define the widget in rc.lua before
    battery_widget = BatteryTextWidget("battery_widget")
    date_widget = DateTextWidget("date_widget")
    mail_widget = MailTextWidget("mail_widget", 'username', 'password')
    cpu_widget = CPUGraphWidget('cpuwidget')


    # Comment out the following lines depending to the widgets you prefer.

################### MAIL WIDGET ########################
#    mail_timer = Timer(31)
#    mail_timer.add_signal("mail", mail_widget)    
#    mail_timer.start()
########################################################

################### DATE WIDGET ########################
#    date_timer = Timer(60)
#    date_timer.add_signal("date", date_widget)
#    date_timer.start()
########################################################

################### BATTERY WIDGET #####################
#    battery_timer = Timer(31)
#    battery_timer.add_signal("battery", battery_widget)
#    battery_timer.start()
########################################################    

################### CPU GRAPH WIDGET ###################
#    cpu_widget.set_width(50)
#    cpu_widget.set_background_color("#494B4F")
#    cpu_widget.set_color("#FF5656")
#    cpu_widget.set_gradient_colors({ "#FF5656", "#88A175", "#AECF96" })
#    cpu_timer = Timer(1)
#    cpu_timer.add_signal('cpu', cpu_widget)
#    cpu_timer.start()
########################################################
    



