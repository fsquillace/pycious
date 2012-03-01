'''
Created on Feb 25, 2012
'''

import sys

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


def execute(cmd):
    """
    Sends a command to awesome-client and return it's output
    """
    st, out = getstatusoutput("echo -e \""+cmd+"\" | awesome-client")
    if st!=0:
        raise CommandError("Error: "+out)
    
    if cmd.split()[0] == 'return': 
        # The command will return an objects
        out = parse(out)
    
    return out
    

def parse(result):
    
    # If the parser is not able to parse 'result' then
    # returns directly 'result' as a string
    parsed_result = result

    if result != None and len(result)>0:
        result = result.strip()
        typ = result.split()[0]
        val = result[len(typ)+1:]
        if typ=='string':
            parsed_result = val.replace('"','')
        elif typ=='double':
            parsed_result = float(val)
        elif typ=='boolean':
            parsed_result = val=='true'
    return parsed_result
    

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


