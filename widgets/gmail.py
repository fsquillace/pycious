#!/usr/bin/python

import awrap
import imaplib
import time


def connect(username, password):
    #first field is imap server, second - port (993 for gmail SSL IMAP)
    M=imaplib.IMAP4_SSL("imap.gmail.com", 993)
    #first field is imap login (gmail uses login with domain and '@' character), second - password
    M.login(username, password)
    return M


if __name__ == '__main__':
    mailwidget = awrap.TextWidget("mailwidget")
    
    username = ""
    password = ""
    
    if not username or not password:
        raise Exception()
    
    M = None
    
    while True:
        try:
            if not M:
                raise Exception()
            
            status, counts = M.status("Inbox","(MESSAGES UNSEEN)")
            unread = counts[0].split()[4][:-1]
        
            if unread == b'0':
                mailwidget.text("<b><small>no mails</small></b>")
                mailwidget.bg("trasparent")
            else:
                #red bg color when you have unseen mail
                # Convert bytes to Unicode
                unread = str(unread, encoding='utf-8')
                mailwidget.text('<b><small>'+unread+' mails</small></b>')
                mailwidget.blink_bg("red")
                #M.logout()

        except:
            M = connect(username, password)
            mailwidget.text('<b><small>na</small></b>')
            mailwidget.bg('trasparent')
            
            
        time.sleep(10)
    
