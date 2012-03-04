#!/usr/bin/python
from __future__ import division

import os

from datetime import datetime

from pycious.lib.common import singleton

# # # BATTERY CHARGE # # #

def battery():
    """
    Display power manager information
    Return a tuple (state,charge percent)
    """

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

            # if state == 'Charging':
            #     battery_text = '<span color=\\\"{0}\\\"><b>+</b> {1}%</span> '
            # elif state == 'Discharging':
            #     battery_text = '<span color=\\\"{0}\\\"><b>-</b> {1}%</span> '

            if state != 'Charged':
                percent = int((charge_now / charge_full) * 100)
                
                # if percent >= 60:
                #     color = 'green'
                # elif percent >= 20:
                #     color = 'yellow'
                # else:
                #     color = 'red'

                return state,percent
            else:
                return state,100
    except:
        return 'na',0

# # # CPU LOAD INFORMATION # # #

@singleton   
class CPU:
    def __init__(self):
        self.prev_work_jiffies = 0
        self.prev_total_jiffies = 0

    def __call__(self):
        """
        Display current CPUs usage
        """
        
        try:
    
            # Retrive main information about CPU load
            # For a reference about the topic, see:
            # 1. http://stackoverflow.com/questions/3017162
            # /how-to-get-total-cpu-usage-in-linux-c
            # 2. http://www.linuxhowtos.org/System/procstat.htm

            with open('/proc/stat') as f:
                l_s = f.readline().split(' ')[2:9]
                cpu_jiffies = [int(x) for x in l_s]

                # Calculate the current number of jiffies
                curr_work_jiffies = sum(cpu_jiffies[0:3])
                curr_total_jiffies = sum(cpu_jiffies)
            
                # Check for previous jiffies
                if self.prev_work_jiffies != 0:
                    # Calculate the percentage of usage
                    cpu_usage = ( curr_work_jiffies - self.prev_work_jiffies ) / \
                                ( curr_total_jiffies - self.prev_total_jiffies )
                    # Display percentage
                    return cpu_usage

                # Update previous jiffies for next call
                self.prev_work_jiffies = curr_work_jiffies
                self.prev_total_jiffies = curr_total_jiffies
                
                return 0.0
        except Exception as e:
            return None

# singleton cpu instance
cpu = CPU()

# # # MEMORY USAGE # # #

def mem_usage():
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
                    return (used_memory / total_memory)
                    
                # Next line
                i += 1
    except Exception as e:
        return None
    
# # # DATE INFORMATION # # #

def date():
    """
    Display current datetime information
    """
    return datetime.today().strftime("%a %b %d, %H:%M ")

# # # NETWORK STATISTICS # # #

@singleton
class NetworkStatistics:
    """
    Generate an Iterator for all ifaces with their main information.
    yield a tuple (iface_name, rx_bytes, tx_bytes)
    """

    def __init__(self):
        self.__ifaces = {}

    def __call__(self):
        """
        Collects and display information about iface network usage
        """
        
        # Used to store temporary information to display
        message = ""

        try:
            # Try to collect all interfaces available
            # on the system
            if len(self.__ifaces) == 0:
                self.__ifaces = {iface:{'tx':0,'rx':0} \
                            for iface in os.listdir('/sys/class/net/') \
                            if iface != 'lo'} # Exclude lo interface, who cares!?

            # For each interfaces display the statistics
            message = ""
            for iface in self.__ifaces:
                # Calculate actual values
                rx = int(open('/sys/class/net/' + iface + '/statistics/rx_bytes')\
                    .readline())
                tx = int(open('/sys/class/net/' + iface + '/statistics/tx_bytes')\
                    .readline())

                # Format values in Bytes
                actual_rx = int((rx - self.__ifaces[iface]['rx'])/1024)
                actual_tx = int((tx - self.__ifaces[iface]['tx'])/1024)
                
                # Format message
                # message += "[<b>{0}:</b> rx: {1}KB tx: {2}KB] ".format(
                #     iface, actual_rx, actual_tx)

                # Updates history values
                self.__ifaces[iface]['rx'] = rx
                self.__ifaces[iface]['tx'] = tx

                # yield a tuple(iface, rx_bytes, tx_bytes)
                yield iface,actual_rx,actual_tx
        except:
            yield None

#singleton NetworkStatistics
network_statistics = NetworkStatistics()

# # # FILESYSTEM USAGE # # #

# TODO
