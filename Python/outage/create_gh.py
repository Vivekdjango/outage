#!/usr/bin/python
print "Content-Type: text/html"
print "Location: /outage/res.html\n\n"
print ""

import smtplib, sys
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import cgi, cgitb
from termcolor import colored
import os
cgitb.enable()

messg = MIMEMultipart()

def send_error(sender, recipient, messg):
    SMTP_SERVER = '<mail server>'
    session = smtplib.SMTP('<mail server>')
    session.ehlo()
    send_it = session.sendmail(messg['From'], messg['To'], messg)
    session.quit()
    return send_it


SMTP_SERVER = '<mail server>'
sender = '<sender email-id>'
recipient = ['<receiver1>','<receiver1>']
d=datetime.datetime.now().strftime("%d-%B-%Y")
t=datetime.datetime.now().strftime("%H:%M %p")
form=cgi.FieldStorage()
pr=form.getvalue('priority')
sub=form.getvalue('subject')
jira=form.getvalue('jira')
slack=form.getvalue('slack')
app=form.getvalue('app')
bu=form.getvalue('business')
re=form.getvalue('region')
desc=form.getvalue('desc')
out=form.getvalue('time')
ath=form.getvalue('attach')

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

msg = "%s<br><br> <b>Date</b>:%s <br> <br> <strong>Time</strong>:%s (IST)<br> %s <br><br><b>Downtime</b>:%s (minute)<br><br><b>Issue</b>:%s <br> <b>Jira:</b>%s <br><b>Slack:</b>%s<br> <br><b>Application Impacted:</b>%s <br> <b>Buisness Impact:</b>%s <br> <b>Region Impacted:</b>%s <br> <br> <b><u>Summary:</b></u><br>"%(head,d,t,st,out,sub,j,slk,app,bu,re)


ab=desc.split('\n')

l=[]
for i in ab:
	val="<ul><li>%s</li></ul>"%(i)
	l.append(val)

de=''.join(l)

foot="<b>ETA:</b>NA<br><br>Regards & Thanks<br>NOC"

body=msg+de+foot

messg.attach(body)

subject=status+':'+pr.upper()+'Outage Communication'+''+sub


messg = MIMEMultipart()
messg['Subject'] = subject
messg['From'] = sender
#msg['Reply-to'] = 'otroemail@dominio'
messg['To'] = recipient

messg.preamble = 'Multipart massage.\n'

new = MIMEApplication(open("%s","rb")%(ath).read())
new.add_header('Content-Disposition', 'attachment', filename="%s"%(ath))
messg.attach(new)



'''
headers = ["From: " + sender,
               "Subject: " + subject,
               "To: " + ", ".join(recipient),
               "MIME-Version: 1.0",
               "Content-Type: text/html"]
headers = "\r\n".join(headers)
'''
p=send_error(messg['From'], messg['To'],messg.as_string())


q=sub.replace(" ","")

path='/var/www/html/outage/'
os.system('touch /var/www/html/outage/{0}.html'.format(q))

with open(path+q+'.html','w') as f:
	f.write(msg)
	f.write("\n")
	f.write(de)
	f.close()

#if p=={}:
#	print 'Location:google.co.in'
