#!/usr/bin/python
print "Content-Type: text/html"
print ""

import smtplib, sys
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import cgi, cgitb
from termcolor import colored
import os
def send_error(sender, recipient, headers, body):
    SMTP_SERVER = '<mail server>'
    session = smtplib.SMTP('<mail server>')
    session.ehlo()
    send_it = session.sendmail(sender, recipient, headers + "\r\n\r\n" +  body)
    session.quit()
    return send_it


SMTP_SERVER = '<mail server>'
sender = '<sender email-id>'
recipient = ['<receiver1>','<receiver1>']
x=datetime.datetime.now().strftime("%d/%B/%Y %H:%M")
s=x.split()
d=s[0]
t=s[1]
form=cgi.FieldStorage()
pr=form.getvalue('priority')
sub=form.getvalue('subject')
jira=form.getvalue('jira')
slack=form.getvalue('slack')
app=form.getvalue('app')
bu=form.getvalue('business')
re=form.getvalue('region')
desc=form.getvalue('desc')

st="""
<p style='color:red'><b><u>Status:</u></b>RED</p>
"""
head="""
<b><center><u>%s Outage Communication</u></center></b>
"""%(pr.upper())
j="""
<a href=https://jira.corp.inmobi.com:8443/browse/{0}>{1}</a>
""".format(jira,jira)

slk="""
<a href=https://inmobi.slack.com/messages/{0}>{1}</a>
""".format(slack,slack)

status='RED'

msg = "%s<br><br> <b>Date</b>:%s <br> <br> <strong>Time</strong>:%s <br> %s <br><b>Issue</b>:%s <br> <b>Jira:</b>%s <br><b>Slack:</b>%s<br> <br><b>Application Impacted:</b>%s <br> <b>Buisness Impact:</b>%s <br> <b>Region Impacted:</b>%s <br> <br> <b><u>Summary:</b></u><br>"%(head,d,t,st,sub,j,slk,app,bu,re)


ab=desc.split('\n')

l=[]
for i in ab:
	val="<ul><li>%s</li></ul>"%(i)
	l.append(val)

de=''.join(l)

foot="<b>ETA:</b>NA<br><br>Regards & Thanks<br>NOC"

body=msg+de+foot

subject=status+':'+pr.upper()+'Outage Communication'+''+sub

headers = ["From: " + sender,
               "Subject: " + subject,
               "To: " + ", ".join(recipient),
               "MIME-Version: 1.0",
               "Content-Type: text/html"]
headers = "\r\n".join(headers)
send_error(sender, recipient, headers, body)

q=sub.replace(" ","")

path='/var/www/html/outage/'
os.system('touch /var/www/html/outage/{0}.html'.format(q))

with open(path+q+'.html','w') as f:
	f.write(msg)
	f.write("\n")
#	f.write(foot)
	f.close()
