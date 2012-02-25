
import time

from pycious.common import execute


class Widget:
    """"""
    
    def __init__(self, widget_name):
        """widget_name (str) string of the widget declared in rc.lua"""
        if widget_name == None:
            raise ValueError('You must specify the name of a widget declared in rc.lua.')
        
        if widget_name:
            self.widget_name = widget_name
    
    @property
    def visible(self):
        """Returns whether the widget is visible."""
        return execute("return {0}.{1}".format(self.widget_name, 'visible'))
    
    @visible.setter
    def visible(self, b):
        if b:
            bol = 'true'
        else:
            bol = 'false'
        return execute("{0}.{1} = {2}".format(self.widget_name, 'visible', bol))
    
    
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
        


class TextWidget(Widget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, widget_name):
        """Constructor"""
        # XXX Compatibility issue with Python2.7
        # super().__init__(widget_name)
        Widget.__init__(self, widget_name)
 

    @property
    def text(self):
        """return The text to display."""
        return execute("return {0}.{1}".format(self.widget_name, 'text'))
    
    @text.setter
    def text(self, txt):
        """text: The text to display."""
        return execute("{0}.{1} = '{2}'".format(self.widget_name, 'text', txt))
    
    @property
    def width(self):
        """Define the width of the widget."""
        return execute("return {0}.{1}".format(self.widget_name, 'width'))
    
    @width.setter
    def width(self, w):
        """width(int): The width of the textbox. Set to 0 for auto."""
        return execute("{0}.{1} = '{2}'".format(self.widget_name, 'width', str(w)))
    
    @property
    def border_width(self):
        """Define the border width of the widget."""
        return execute("return {0}.{1}".format(self.widget_name, 'border_width'))
    
    @border_width.setter
    def border_width(self, bw):
        """border_width: The border width to draw around."""
        return execute("{0}.{1} = '{2}'".format(self.widget_name, 'border_width', bw))
    
    @property
    def border_color(self):
        """Define the border color of the widget."""
        return execute("return {0}.{1}".format(self.widget_name, 'border_color'))
    
    @border_color.setter
    def border_color(self, bc):
        """border_color: The border color.
           Put 'trasparent' for a trasparent color.
        """
        if bc == 'trasparent':
            bc = '#00000000'
        return execute("{0}.{1} = '{2}'".format(self.widget_name, 'border_color', bc))
    
    @property
    def align(self):
        """Define the tett alignment: left, center or right."""
        return execute("return {0}.{1}".format(self.widget_name, 'align'))
    
    @align.setter
    def align(self, a):
        """align: Text alignment, left, center or right."""
        return execute("{0}.{1} = '{2}'".format(self.widget_name, 'align', a))
    
    @property
    def bg(self):
        """return The background to display."""
        return execute("return {0}.{1}".format(self.widget_name, 'bg'))
    
    @bg.setter
    def bg(self, bk):
        """bk: Background color.
           Put 'trasparent' for a trasparent color.
        """
        if bk == 'trasparent':
            bk = '#00000000'
        return execute("{0}.{1} = '{2}'".format(self.widget_name, 'bg', bk))
    
    
    
    def blink_bg(self, color, timeout=1):
        """Blink the background."""
        self.bg(color)
        time.sleep(timeout)
        self.bg('trasparent')

class GraphWidget(Widget):
    """"""
    def __init__(self, widget_name):
        """Constructor"""

        # XXX Compatibility issue with Python2.7
        # super().__init__(widget_name)
        super(GraphWidget, self).__init__(widget_name)

    def add_value(self, value):
        """"""
        if value >= 0 or value <= 1:
            return execute("{0}:{1}({2})".format(self.widget_name, 'add_value', value))
    
    # TODO Continue with other methods
    # (see API Reference http://awesome.naquadah.org/doc/api/modules/awful.widget.graph.html)


class ImageBoxWidget(Widget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, widget_name):
        """Constructor"""
        super().__init__(widget_name)    
    
        
    #----------------------------------------------------------------------
    def image(self, img):
        """image: The image to display. """
        execute("{0}.{1} = '{2}'".format(self.widget_name, 'image', img))
    
    #----------------------------------------------------------------------
    def bg(self, b):
        """bg: The background color to use. """
        execute("{0}.{1} = '{2}'".format(self.widget_name, 'bg', b))
        
        
class SysTrayWidget(Widget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, widget_name):
        """Constructor"""
        super().__init__(widget_name)
        
        
