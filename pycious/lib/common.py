'''
Created on Feb 25, 2012
'''

import sys
import lua


getstatusoutput = None
if sys.version_info.major == 3:
    from subprocess import getstatusoutput
else:
    from commands import getstatusoutput

class CommandError(Exception):
    """
    Specify the exception launched when passing a command to dbus.
    """
    pass

class WidgetDoesNotExist(Exception):
    pass

class WidgetTypeError(Exception):
    pass


def execute(cmd):
    """
        Sends a command to awesome-client and return it's output
    """
    st, out = getstatusoutput("echo -e \""+cmd+"\" | awesome-client")
    if st!=0:
        raise CommandError("Error: "+out)
    
    return out

# import the python module in awesome
execute("require('python')")







def to_lua(var):
    """
        Convert a python variable to the corresponding lua variable
        Parameters:
        var: python variable
        Returns:
        res: a string of the corresponding lua variable
    """
    typ = type(var)
    res = var
    
    if typ == bool:
        if var:
            res = 'true'
        else:
            res = 'false'
    elif typ == int or typ == float:
        res = str(var)
    elif typ == str:
        res = var
    
    return res


def to_python(var):
    """
        var is a string got with the 'return var' lua instruction.
        'return var' returns the pair: var = <type value>.
    """
    
    if var == None or var== '':
        return None


    var = var.strip()
    typ = var.split()[0]
    val = var[len(typ)+1:]    
    return lua.eval(val)

    # If the parser is not able to parse 'result' then
    # returns directly 'result' as a string
#    parsed_result = result
#
#    if result != None and len(result)>0:
#
#        if typ=='string':
#            parsed_result = val.replace('"','')
#        elif typ=='double':
#            parsed_result = float(val)
#        elif typ=='boolean':
#            parsed_result = val=='true'
#    return parsed_result
    

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


