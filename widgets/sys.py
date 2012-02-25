#!/usr/bin/python


import os

from datetime import datetime


# # # BATTERY CHARGE FUNCTION # # #

def battery(battery_widget):
    """Display power manager information"""
    try:
        battery_path = '/sys/class/power_supply/BAT0/'
        battery_text = ''
        percent = 0

        with open(battery_path + "present") as f:
            charge_full = int(open(battery_path + "charge_full")\
                .readline()[:-1])
            charge_now = int(open(battery_path + "charge_now")\
                .readline()[:-1])
            state = open(battery_path + "status").readline()[:-1]

            if state == 'Charging':
                battery_text = '<span color=\\\"{0}\\\"><b>+</b> {1}%</span> '
            elif state == 'Discharging':
                battery_text = '<span color=\\\"{0}\\\"><b>-</b> {1}%</span> '

            if state != 'Charged':
                percent = int((charge_now / charge_full) * 100)
                
                if percent >= 60:
                    color = 'green'
                elif percent >= 20:
                    color = 'yellow'
                else:
                    color = 'red'

                battery_widget.text(battery_text.format(color,percent))
            else:
                battery_widget.text('')
    except:
        battery_widget.text("na")
        
        
prev_work_jiffies = prev_total_jiffies = 0

def cpu_usage(cpu_widget):
    """
    Display current CPUs usage
    """
    try:
        # Retrieve previous saved cpu jiffies
        global prev_work_jiffies, prev_total_jiffies

        # Retrive main information about CPU load
        # For a reference about the topic, see:
        # 1. http://stackoverflow.com/questions/3017162
        # /how-to-get-total-cpu-usage-in-linux-c
        # 2. http://www.linuxhowtos.org/System/procstat.htm

        with open('/proc/stat') as f:
            cpu_jiffies = map(int, f.readline().split(' ')[2:9])

            # Calculate the current number of jiffies
            curr_work_jiffies = sum(cpu_jiffies[0:3])
            curr_total_jiffies = sum(cpu_jiffies)
        
            # Check for previous jiffies
            if prev_work_jiffies != 0:
                # Calculate the percentage of usage
                cpu_usage = ( curr_work_jiffies - prev_work_jiffies ) / \
                            ( curr_total_jiffies - prev_total_jiffies )
                # Display percentage
                cpu_widget.add_value(cpu_usage)

            # Update previous jiffies for next call
            prev_work_jiffies = curr_work_jiffies
            prev_total_jiffies = curr_total_jiffies
    except:
        pass


def mem_usage(mem_widget):
    """
    Display current Memory usage
    """
    try:
        # Retrieve actual memory usage
        # see: /proc/meminfo

        with open('/proc/meminfo') as f:
            i = 0
            total_memory = used_memory = 0

            for line in f:
                # Read the int value from the line
                int_value = int(line.split(":")[1][:-4].lstrip())

                if i == 0:
                    # Update total_memory
                    total_memory = used_memory = int_value
                elif i < 4:
                    # Read only first four lines!!!
                    # Subtract MemFree, Buffers and Cached from used_memory

                    used_memory -= int_value
                else:
                    # Display memory usage and break loop!
                    mem_widget.add_value(used_memory / total_memory)
                    break
                    
                # Next line
                i += 1
    except Exception as e:
        print(e)


def date(date_widget):
    """
    Display current datetime information
    """
    date_widget.text(datetime.today().strftime("%a %b %d, %H:%M "))



def network_statistics(network_widget, ifaces = {'wlan0':{'tx':0, 'rx':0}}):
    """
    Collects and display information about iface network usage
    """
    
    # Used to store temporary information to display
    message = ""

    try:
        # Try to collect all interfaces available
        # on the system
        if len(ifaces) == 0:
            ifaces = {iface:{'tx':0,'rx':0} \
                        for iface in os.listdir('/sys/class/net/') \
                        if iface != 'lo'} # Exclude lo interface, who cares!?

        # For each interfaces display the statistics
        message = ""
        for iface in ifaces:
            # Calculate actual values
            rx = int(open('/sys/class/net/' + iface + '/statistics/rx_bytes')\
                .readline())
            tx = int(open('/sys/class/net/' + iface + '/statistics/tx_bytes')\
                .readline())

            # Format values
            # TODO: May be useful format current usage regards bytes multiple
            # (e.g. KB, MB, GB, and so on...)
            actual_rx = int((rx - ifaces[iface]['rx'])/1024)
            actual_tx = int((tx - ifaces[iface]['tx'])/1024)
            
            # Format message
            message += "[<b>{0}:</b> rx: {1}KB tx: {2}KB] ".format(
                iface, actual_rx, actual_tx)

            # Updates values
            ifaces[iface]['rx'] = rx
            ifaces[iface]['tx'] = tx

        # Display message
        network_widget.text(message)
    except:
        network_widget.text("Unable to fetch iface activity")

# # # FILESYSTEM USAGE # # #

# TODO
