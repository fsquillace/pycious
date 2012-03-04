import re

from pycious.lib.common import getstatusoutput


# TODO Create a dictionary function


def volume():
    """
    Returns: a tuple (vol, state)
    """
    st, out = getstatusoutput('amixer get Master')
    for line in out.split('\n'):
        m = re.match('.* \[(\d+)%\] +\[(.+)\]', line)
        if m:
            vol, st = m.groups()
            return int(vol), st 
    