'''
Created on Feb 27, 2012

'''

# Importing web function
from pycious.lib.web import Mail, Grss

# Importing Base widget
from pycious.api.widget import TextWidget


class MailTextWidget(TextWidget):
    def __init__(self, widget_name, username, password, server='imap.gmail.com', port=993):
        TextWidget.__init__(self, widget_name)
        
        # get the mail object
        self.mail = Mail(username, password, server, port)
        
    
    def __call__(self):
        
        unread = self.mail()
        
        if unread == 0:
            self.text = "no mails"
            self.bg = "trasparent"
        elif unread == -1:
            self.text = "na"
            self.bg = "trasparent"
        else:
            #red bg color when you have unseen mail
            self.text = str(unread)+' mails'
            self.blink_bg = "red"


class GrssTextWidget(TextWidget):
    def __init__(self, widget_name, username, password):
        TextWidget.__init__(self, widget_name)
        
        # get the grss object
        self.grss = Grss(username, password)
        
    
    def __call__(self):
        
        unread = self.grss()
        
        if unread == 0:
            self.text = "no news"
            self.bg = "trasparent"
        elif unread == -1:
            self.text = "na"
            self.bg = "trasparent"
        else:
            #red bg color when you have unseen mail
            self.text = str(unread)+' news'
            self.blink_bg = "red"
