#!/usr/bin/python

print "Content-Type: text/html"
print ""


import smtplib
import cgi, cgitb
import codecs
from mail_update.py import 

def update_mail(sender,receipent,headers,msg):
	SMTP_SERVER='<mail server>'
	session=smtplib.SMTP('<mail server>')
	session.ehlo()
	send_it = session.sendmail(sender, recipient, headers + "\r\n\r\n" +  msg)
	session.quit()
        return send_it


SMTP_SERVER='mrely.corp.inmobi.com'
sender='<sender email-id>'
recipient = ['<receiver1>','<receiver1>']





msg=desc
subject=sub

print msg
print st
print sub
#headers = ["From: " + sender,
#               "Subject: " + subject,
#               "To: " + ", ".join(recipient),
#               "MIME-Version: 1.0",
#               "Content-Type: text/html"]


#headers = "\r\n".join(headers)
#send_error(sender, recipient, headers, msg)
