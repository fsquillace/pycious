#!/usr/bin/python

from __future__ import division


from awrap.widget import TextWidget, GraphWidget
from awrap.timer import Timer

from widgets.sys import battery, cpu_usage, network_statistics, date


if __name__ == "__main__":

    # Retrieve all available widgets defined in rc.lua
    # You MUST define the widget in rc.lua before
    battery_widget = TextWidget("battery_widget")
    cpu_widget = GraphWidget("cpu_widget")
    mem_widget = GraphWidget("mem_widget")
    network_widget = TextWidget("network_widget")
    date_widget = TextWidget("date_widget")
    
    # Define timer
    battery_timer = Timer(30)
    cpu_mem_timer = Timer(1)
    network_timer = Timer(1)
    date_timer = Timer(60)
    
    
    def battery_text():
        battery_widget.text = battery()
    
    # Attach functions to each timer
    battery_timer.add_signal("battery", battery_text)
    cpu_mem_timer.add_signal("cpu_usage", cpu_usage)
    network_timer.add_signal("network_statistics", network_statistics)
    date_timer.add_signal("date", date)

    # Starts all the timers
    battery_timer.start()
    cpu_mem_timer.start()
    network_timer.start()
    date_timer.start()
