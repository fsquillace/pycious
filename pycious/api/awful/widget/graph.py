'''
Created on Feb 27, 2012

'''

from pycious.lib.common import execute, WidgetDoesNotExist, to_lua


class Graph(object):
    """"""
    def __init__(self, widget_name):
        """Constructor"""
        if widget_name == None:
            raise ValueError('You must specify the name of a widget declared in rc.lua.')
        
        # Checks if the widget already exists in rc.lua otherwise launch Exception
        out = execute('return '+widget_name)
        if not out:
            raise WidgetDoesNotExist
        
        self.widget_name = widget_name
        


    def add_value(self, value, group=None):
        """
            Add a value to the graph
            Parameters: 
            value: The value between 0 and 1.
            group: The stack color group index.

        """
        if type(value) != float and type(value) != int:
            raise TypeError('Error: value='+str(value)+' must be a float or int.')
        
        if value < 0 or value > 1:
            raise ValueError('Error: value='+value+'. It must be between 0 and 1.')  

        execute("{0}:{1}({2})".format(self.widget_name, 'add_value', to_lua(value) ))


    def set_background_color(self, color):
        """
            Set the graph background color.
            Parameters:
            color: The graph background color.
        """
        if type(color) != str:
            raise TypeError('Error: color='+str(color)+' must be a string.')
        
        execute("{0}:{1}('{2}')".format(self.widget_name, 'set_background_color', to_lua(color) ))

    
    def set_border_color(self, color):
        """
            Set the graph border color. 
            If the value is nil, no border will be drawn.
            Parameters:
            color: The border color to set.
        """
        if type(color) != str:
            raise TypeError('Error: color='+str(color)+' must be a string.')
        
        execute("{0}:{1}('{2}')".format(self.widget_name, 'set_border_color', to_lua(color) ))

    def set_color(self, color):
        """
            Set the graph foreground color.
            Parameters:
            color: The graph color.
        """
        if type(color) != str:
            raise TypeError('Error: color='+str(color)+' must be a string.')
        
        execute("{0}:{1}('{2}')".format(self.widget_name, 'set_color', to_lua(color) ))


    def set_gradient_angle(self, gradient_angle):
        """
            Set the graph foreground colors gradient angle.
            Default is 270 degrees (horizontal).
            Parameters:
            gradient_angle: Angle of gradient in degrees.
        """
        if type(gradient_angle) != int and type(gradient_angle) != float:
            raise TypeError('Error: gradient_angle='+str(gradient_angle)+' must be a int or float.')
        
        execute("{0}:{1}({2})".format(self.widget_name, 'set_gradient_angle', to_lua(gradient_angle) ))


    def set_gradient_colors(self, gradient_colors):
        """
            Set the graph foreground color as a gradient.
            Parameters:
            gradient_colors: A table with gradients colors. 
            The distance between each color can also be specified.
            Example: { "red", "blue" } or { "red", "green", "blue", blue = 10 } 
            to specify blue distance from other colors.
        """
        if type(gradient_colors) != set:
            raise TypeError('Error: gradient_colors='+str(gradient_colors)+' must be a dict.')
        
        execute("{0}:{1}({2})".format(self.widget_name, 'set_gradient_colors', to_lua(gradient_colors) ))


    def set_height(self, height):
        """Set the graph height.
            Parameters:
            height: The height to set.
        """
        if type(height) != int and type(height) != float:
            raise TypeError('Error: height='+str(height)+' must be a int or float.')
        
        execute("{0}:{1}({2})".format(self.widget_name, 'set_height', to_lua(height) ))


    def set_max_value(self, value):
        """
            Set the maximum value the graph should handle. 
            If "scale" is also set, the graph never scales up below this value, 
            but it automatically scales down to make all data fit.
            Parameters:
            value: The value.
        """
        if type(value) != int and type(value) != float:
            raise TypeError('Error: value='+str(value)+' must be a int or float.')
        
        execute("{0}:{1}({2})".format(self.widget_name, 'set_max_value', to_lua(value) ))

    def set_scale(self, scale):
        """
            Set the graph to automatically scale its values. 
            Default is false.
            Parameters:
            scale: A boolean value
        """
        if type(scale) != bool:
            raise TypeError('Error: scale='+str(scale)+' must be a bool.')
        
        execute("{0}:{1}({2})".format(self.widget_name, 'set_scale', to_lua(scale) ))


    def set_stack(self, stack):
        """
            Set the graph to draw stacks. 
            Default is false.
            Parameters:
            stack: A boolean value.
        """
        if type(stack) != bool:
            raise TypeError('Error: stack='+str(stack)+' must be a bool.')
        
        execute("{0}:{1}({2})".format(self.widget_name, 'set_stack', to_lua(stack) ))
    
    def set_stack_colors(self, stack_colors):
        """
            Set the graph stacking colors. Order matters.
            Parameters:
            stack_colors: A table with stacking colors.
        """
        if type(stack_colors) != dict:
            raise TypeError('Error: stack_colors='+str(stack_colors)+' must be a dict.')
        
        execute("{0}:{1}({2})".format(self.widget_name, 'set_stack_colors', to_lua(stack_colors) ))
    
    
    def set_width(self, width):
        """
            Set the graph width.
            Parameters:
            width: The width to set.
        """
        if type(width) != int and type(width) != float:
            raise TypeError('Error: width='+str(width)+' must be a int or float.')
        
        execute("{0}:{1}({2})".format(self.widget_name, 'set_width', to_lua(width) ))

