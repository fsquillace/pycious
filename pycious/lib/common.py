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
    l = result.split()
    parsed_result = result

    if l != None and len(l)>0:
        if l[0]=='string':
            parsed_result = l[1].replace('"','')
        elif l[0]=='double':
            parsed_result = float(l[1])
        elif l[0]=='boolean':
            parsed_result = l[1]=='true'
    return parsed_result
    

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


