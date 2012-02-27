'''
Created on Feb 27, 2012

'''

from pycious.lib.common import execute
from pycious.api.widget import Widget

class Graph(Widget):
    """"""
    def __init__(self, widget_name):
        """Constructor"""
        Widget.__init__(self, widget_name)

    def add_value(self, value):
        """"""
        if value >= 0 or value <= 1:
            return execute("{0}:{1}({2})".format(self.widget_name, 'add_value', value))
    
    # TODO Continue with other methods
    # (see API Reference http://awesome.naquadah.org/doc/api/modules/awful.widget.graph.html)
