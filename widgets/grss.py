#!/usr/bin/python3

import subprocess
from xml.dom import minidom
import time
import awrap


def connect(username, password):
    st, out = subprocess.getstatusoutput('curl -fs "https://www.google.com/accounts/ClientLogin?service=reader&Email='+username+'&Passwd='+password+'"')
    if not out or out=="":
        raise Exception()
    
    auth_resp_dict = dict(x.split('=') for x in out.split('\n') if x)
    auth_token = auth_resp_dict["Auth"]
    
    auth = 'GoogleLogin auth='+ auth_token
    command = 'curl -s -X GET http://www.google.com/reader/api/0/unread-count?all=true --header "Authorization: '+auth+'"'
    
    st, out = subprocess.getstatusoutput(command)
    
    xml_doc = minidom.parseString(str(out))
    
    return xml_doc


if __name__ == '__main__':

    rsswidget = awrap.TextWidget('rsswidget')
    
    username = ""
    password = ""
    if not username or not password:
        raise Exception()

    while True:
        try:
            xml_doc = connect(username, password)

    
            list_el = xml_doc.firstChild.getElementsByTagName('list')[0]
            if len(list_el.childNodes)==0:
                rsswidget.text('<b><small>no news</small></b>')
                rsswidget.bg('trasparent')
            for obj in list_el.childNodes:
                if obj.getElementsByTagName('string')[0].firstChild.data.find('reading-list')!=-1:
                    for numb in obj.getElementsByTagName('number'):
                        if numb.attributes['name'].value=='count':
                            count = int(numb.firstChild.data)
                            if count == 0:
                                rsswidget.text('<b><small>no news</small></b>')
                                rsswidget.bg('trasparent')
                            else:
                                rsswidget.text('<b><small>'+str(count)+' news</small></b>')
                                rsswidget.blink_bg('red')

        except:
            rsswidget.text('<b><small>na</small></b>')
            rsswidget.bg('trasparent')
                            
                            
        time.sleep(10)

