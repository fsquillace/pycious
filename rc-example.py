#!/usr/bin/python

from __future__ import division


from pycious.widgets.system import BatteryTextWidget, DateTextWidget
from pycious.widgets.web import MailTextWidget

from pycious.api.timer import Timer


if __name__ == "__main__":

    # Retrieve all available widgets defined in rc.lua
    # You MUST define the widget in rc.lua before
    battery_widget = BatteryTextWidget("battery_widget")
    date_widget = DateTextWidget("date_widget")
    mail_widget = MailTextWidget("mail_widget", 'username', 'password')
    
    # Define timer
    battery_timer = Timer(31)
    date_timer = Timer(60)
    mail_timer = Timer(31)
    
    
    # Attach functions to each timer
    battery_timer.add_signal("battery", battery_widget)
    date_timer.add_signal("date", date_widget)
    mail_timer.add_signal("mail", mail_widget)

    # Starts all the timers
    battery_timer.start()
    date_timer.start()
    mail_timer.start()
