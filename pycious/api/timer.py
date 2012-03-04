'''
Created on Feb 25, 2012

'''

import threading
import time

class Timer(threading.Thread):
    """"""
    
    def __init__(self, timeout=1):
        """Constructor"""
        super(Timer, self).__init__()

        # See timer object in awesome
        self.__timeout = timeout
        self.__signals = {}
    
    def add_signal(self, name, func):
        """
        Call functions that will be called by the timer object 
        are stored into a dict
        """
        if not callable(func):
            raise ValueError('Error: func is not callable.')
        
        self.__signals[name] = func
    
    def remove_signal(self, name=''):
        """"""
        del self.__signals[name]
    
    def emit_signal(self, name):
        """"""
        return self.__signals[name]()

    def run(self):
        """"""
        while True:
            for name in self.__signals:
                self.emit_signal(name)
                #print "signal call: ", name
            time.sleep(self.__timeout)

