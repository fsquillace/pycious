#!/usr/bin/python

import subprocess
import time

########################################################################
class CommandError(Exception):
    """"""
    pass
    

def execute(cmd):
    st, out = subprocess.getstatusoutput("echo -e \""+cmd+"\" | awesome-client")
    if st!=0:
        raise CommandError("Error: "+out)
    return out


########################################################################
class Widget:
    """"""

    #----------------------------------------------------------------------
    def __init__(self, widget_name=None):
        """Constructor"""
        if widget_name:
            self.widget_name = widget_name
        else:
            # TODO define the widget into the config
            pass
        
    def visible(self, b):
        return execute("{0}.{1} = '{2}'".format(self.widget_name, 'visible', b))
    
    
    def buttons(self, table):
        """
        table is a dict. The key represents the key combinations (i.e. '{ modkey }, 1' means modkey+mouse_butt1).
        The value is a lua function.
        For example:
            butts['{}, 1'] = "function () awful.util.spawn('amixer -q set Master 5%+') end"
        """
        # Adds a table like:
        # widgetbuttons = "widgetbuttons = awful.util.table.join(awful.button({ }, 1, function() ... end))"
        
        
        butts = []
        for k,v in table.items():
            butts.append('awful.button('+k+', '+v+')')
        
        butts = ', '.join(butts)
        
        widgetbuttons = "widgetbuttons = awful.util.table.join("+butts+")"
        
        #print(widgetbuttons)
        execute(widgetbuttons)
        return execute("{0}:{1}({2})".format(self.widget_name, 'buttons', 'widgetbuttons'))
        
    
########################################################################
class TextWidget(Widget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, widget_name):
        """Constructor"""
        super().__init__(widget_name)
        
    def text(self, txt):
        """text: The text to display."""
        return execute("{0}.{1} = '{2}'".format(self.widget_name, 'text', txt))
    
    def width(self, w):
        """width: The width of the textbox. Set to 0 for auto."""
        return execute("{0}.{1} = '{2}'".format(self.widget_name, 'width', w))
    
    def border_width(self, bw):
        """border_width: The border width to draw around."""
        return execute("{0}.{1} = '{2}'".format(self.widget_name, 'border_width', bw))
    
    def border_color(self, bc):
        """border_color: The border color.
           Put trasparent for a trasparent color.
        """
        if bc == 'trasparent':
            bc = '#00000000'
        return execute("{0}.{1} = '{2}'".format(self.widget_name, 'border_color', bc))
    
    def align(self, a):
        """align: Text alignment, left, center or right."""
        return execute("{0}.{1} = '{2}'".format(self.widget_name, 'align', a))
    
    def bg(self, bk):
        """bk: Background color.
           Put trasparent for a trasparent color.
        """
        if bk == 'trasparent':
            bk = '#00000000'
        return execute("{0}.{1} = '{2}'".format(self.widget_name, 'bg', bk))
    
    def blink_bg(self, color, timeout=1):
        """Blink the background."""
        self.bg(color)
        time.sleep(timeout)
        self.bg('trasparent')
        