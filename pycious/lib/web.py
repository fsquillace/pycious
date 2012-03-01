#!/usr/bin/python3

import subprocess
from xml.dom import minidom

import imaplib

from pycious.lib.common import singleton


class Mail:

    def __init__(self, username, password,\
                 server='imap.gmail.com', port=993):
        """
        It returns -1 if there is no connection otherwise it returns
        the number of unread mails.
        """
        
        if not username or not password:
            raise Exception('Error: You must specify the username and '+\
                            'password in your config file of pycious.')
        
        self.username, self.password = username, password
        self.server, self.port = server, port
        
        # Define the connection object to None
        self.M = None


    def __connect(self):
        self.M=imaplib.IMAP4_SSL(self.server , self.port)
        #First field is imap login (gmail uses login with 
        #domain and '@' character), second - password
        self.M.login(self.username, self.password)
        
    def __call__(self):
        """
        It returns -1 if it's not available the information otherwise
         returns the number of unread mail.
        """
        try:

            if not self.M:
                self.__connect()
            

            status, counts = self.M.status("Inbox","(MESSAGES UNSEEN)")
            unread = counts[0].split()[4][:-1]
              
            return int(unread)
    
        except:
            self.M = None
            return -1


class Grss:
    
    def __init__(self, username, password):
        """
        It returns -1 if there is no connection otherwise it returns
        the number of unread news.
        """
        
        if not username or not password:
            raise Exception('Error: You must specify the username and '+\
                            'password in your config file of pycious.')
        
        self.username, self.password = username, password
        

    
    def __connect(self):
        st, out = subprocess.getstatusoutput('curl -fs '+\
                                             '"https://www.google.com/accounts/ClientLogin?'+\
                                             'service=reader&Email='+self.username+\
                                             '&Passwd='+self.password+'"')
        if not out or out=="":
            raise Exception()
        
        auth_resp_dict = dict(x.split('=') for x in out.split('\n') if x)
        auth_token = auth_resp_dict["Auth"]
        
        auth = 'GoogleLogin auth='+ auth_token
        command = 'curl -s -X GET http://www.google.com/reader/api/0/unread-count?all=true --header "Authorization: '+auth+'"'
        
        st, out = subprocess.getstatusoutput(command)
        
        xml_doc = minidom.parseString(str(out))
        
        return xml_doc
    
    
    def __call__(self):
        
        try:
            xml_doc = self.__connect()

            list_el = xml_doc.firstChild.getElementsByTagName('list')[0]
            if len(list_el.childNodes)==0:
                return -1
            for obj in list_el.childNodes:
                if obj.getElementsByTagName('string')[0].firstChild.data.find('reading-list')!=-1:
                    for numb in obj.getElementsByTagName('number'):
                        if numb.attributes['name'].value=='count':
                            count = int(numb.firstChild.data)
                            return count
        except:
            return -1
