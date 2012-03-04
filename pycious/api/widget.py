
import time

from pycious.lib.common import execute, WidgetDoesNotExist, WidgetTypeError, to_lua, to_python


class Widget(object):
    """"""
    
    def __init__(self, widget_name):
        """widget_name (str) string of the widget declared in rc.lua"""
        if widget_name == None:
            raise ValueError('You must specify the name of a widget declared in rc.lua.')
        
        # Checks if the widget already exists in rc.lua otherwise launch Exception
        out = to_python(execute('return '+widget_name))
        if not out:
            raise WidgetDoesNotExist
        
        if out[:6] != 'widget':
            print(out)
            raise WidgetTypeError("Error: The "+widget_name+" is not a widget.")
        
        self.widget_name = widget_name
    
    @property
    def visible(self):
        """Returns whether the widget is visible."""
        return to_python(execute("return {0}.{1}".format(self.widget_name, 'visible')) )
    
    @visible.setter
    def visible(self, b):
        if type(b) != bool:
            raise TypeError('Error: b='+str(b)+' must be a bool.')
        
        execute("{0}.{1} = {2}".format(self.widget_name, 'visible', to_lua(b) ))
    
    
    def buttons(self, table):
        """
        table is a dict. The key represents the key combinations (i.e. '{ modkey }, 1' means modkey+mouse_butt1).
        The value is a lua function.
        For example:
            butts['{}, 1'] = "function () awful.util.spawn('amixer -q set Master 5%+') end"
        """
        # Adds a table like:
        # widgetbuttons = "widgetbuttons = awful.util.table.join(awful.button({ }, 1, function() ... end))"
        
        
        for k,v in table.items():
            mods = k[0]
            key = k[1]
            
            func_wrap = "function() python.execute("+v+") end"
            
            pass
        
        

        butts = []
        for k,v in table.items():
            butts.append('awful.button('+k+', '+v+')')
        
        butts = ', '.join(butts)
        
        widgetbuttons = "widgetbuttons = awful.util.table.join("+butts+")"
        
        #print(widgetbuttons)
        execute(widgetbuttons)
        return execute("{0}:{1}({2})".format(self.widget_name, 'buttons', 'widgetbuttons'))
        


class TextBoxWidget(Widget):
    """
    """

    #----------------------------------------------------------------------
    def __init__(self, widget_name):
        """Constructor"""
        # XXX Compatibility issue with Python2.7
        # super().__init__(widget_name)
        Widget.__init__(self, widget_name)


    @property
    def text(self):
        """return The text to display."""
        return to_python( execute("return {0}.{1}".format(self.widget_name, 'text')) )
    
    @text.setter
    def text(self, txt):
        """text: The text to display."""
        if type(txt) != str:
            raise TypeError('Error: txt='+str(txt)+' must be a string.')
        
        execute("{0}.{1} = '{2}'".format(self.widget_name, 'text', to_lua(txt) ))
    
    @property
    def width(self):
        """Define the width of the widget."""
        return to_python( execute("return {0}.{1}".format(self.widget_name, 'width')) )
    
    @width.setter
    def width(self, w):
        """width(int or float): The width of the textbox. Set to 0 for auto."""
        if type(w) != int and type(w) != float:
            raise TypeError('Error: w='+str(w)+' must be a int or float.')
        
        execute("{0}.{1} = '{2}'".format(self.widget_name, 'width', to_lua(w)))
    
    @property
    def border_width(self):
        """Define the border width of the widget."""
        return to_python( execute("return {0}.{1}".format(self.widget_name, 'border_width')) )
    
    @border_width.setter
    def border_width(self, bw):
        """border_width: The border width to draw around."""
        if type(bw) != int and type(bw) != float:
            raise TypeError('Error: bw='+str(bw)+' must be a int or float.')
        
        execute("{0}.{1} = '{2}'".format(self.widget_name, 'border_width', to_lua(bw) ))
    
    @property
    def border_color(self):
        """Define the border color of the widget."""
        return to_python(execute("return {0}.{1}".format(self.widget_name, 'border_color')) )
    
    @border_color.setter
    def border_color(self, bc):
        """border_color: The border color.
           Put 'trasparent' for a trasparent color.
        """
        if type(bc) != str:
            raise TypeError('Error: bc='+str(bc)+' must be a string.')
        
        if bc == 'trasparent':
            bc = '#00000000'
        execute("{0}.{1} = '{2}'".format(self.widget_name, 'border_color', to_lua(bc) ))
    
    @property
    def align(self):
        """Define the tetxt alignment: left, center or right."""
        return to_python( execute("return {0}.{1}".format(self.widget_name, 'align')) )
    
    @align.setter
    def align(self, a):
        """align: Text alignment, left, center or right."""
        if type(a) != str:
            raise TypeError('Error: a='+str(a)+' must be a string.')
        
        if a != 'left' and a != 'center' and a!= 'right':
            raise ValueError('Error: align can be either left, center or right.')
        
        execute("{0}.{1} = '{2}'".format(self.widget_name, 'align', to_lua(a) ))
    
    @property
    def bg(self):
        """return The background to display."""
        return to_python( execute("return {0}.{1}".format(self.widget_name, 'bg')) )
    
    @bg.setter
    def bg(self, bk):
        """bk: Background color.
           Put 'trasparent' for a trasparent color.
        """
        if type(bk) != str:
            raise TypeError('Error: bk='+str(bk)+' must be a string.')
        
        if bk == 'trasparent':
            bk = '#00000000'
        execute("{0}.{1} = '{2}'".format(self.widget_name, 'bg', to_lua(bk) ))
    
    
    
    def blink_bg(self, color, timeout=1):
        """Blink the background."""
        self.bg = color
        time.sleep(timeout)
        self.bg = 'trasparent'



class ImageBoxWidget(Widget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, widget_name):
        """Constructor"""
        Widget.__init__(self, widget_name)

    # TODO complete the method ofimagebox
    def image(self, img):
        """image: The image to display. """
        execute("{0}.{1} = '{2}'".format(self.widget_name, 'image', img))
    
    @property
    def bg(self):
        """return The background to display."""
        return to_python( execute("return {0}.{1}".format(self.widget_name, 'bg')) )
    
    @bg.setter
    def bg(self, bk):
        """bk: Background color.
           Put 'trasparent' for a trasparent color.
        """
        if type(bk) != str:
            raise TypeError('Error: bk='+str(bk)+' must be a string.')
        
        if bk == 'trasparent':
            bk = '#00000000'
        execute("{0}.{1} = '{2}'".format(self.widget_name, 'bg', to_lua(bk) ))

        
        
class SysTrayWidget(Widget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, widget_name):
        """Constructor"""
        super().__init__(widget_name)
        
        
