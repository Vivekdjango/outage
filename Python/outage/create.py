#!/usr/bin/python
print "Content-Type: text/html"
print ""

from smtplib import SMTP
import smtplib, sys
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import datetime
import cgi, cgitb
from termcolor import colored
import os

cgitb.enable()

sender = '<sender email-id>'
#recipient = '<receiver1>'
receipents = ['<receiver1>']
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
up=form.getvalue('update')


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

msg = "%s<br><br> <b>Date</b>:%s <br> <br> <strong>Time</strong>:%s (IST)<br> %s <br><br><b>Downtime</b>:%s (minute)<br><br><b>Issue</b>:%s <br> <b>Jira:</b>%s <br><b>Slack:</b>%s<br> <br><b>Application Impacted:</b>%s <br> <b>Buisness Impact:</b>%s <br> <b>Region Impacted:</b>%s<br>  <br><b><u>Summary:</b></u><br>"%(head,d,t,st,out,sub,j,slk,app,bu,re)


ab=desc.split('\n')

l=[]
for i in ab:
	val="<ul><li>%s</li></ul>"%(i)
	l.append(val)

de=''.join(l)

upt="<b>Next Update:</b> %s <br>"%(up)

foot="<br><b>ETA:</b>NA<br><br>Regards & Thanks<br>NOC"

body=msg+de+upt+foot

subject=status+':'+pr.upper()+'Outage Communication'+''+sub


messg = MIMEMultipart('alternative')
messg['Subject'] = subject
messg['From'] = sender
#msg['Reply-to'] = '<receiver1>'
messg['To'] = ",".join(receipents)

messg.preamble = 'Multipart massage.\n'

part = MIMEText(body,'html')
messg.attach(part)

#new = MIMEApplication(open('%s'%(ath),'rb').read())
#new.add_header('Content-Disposition', 'attachment', filename="%s"%(ath))
#messg.attach(new)


smtp = SMTP("<mail server>")
smtp.ehlo()

smtp.sendmail(messg['From'], messg['To'], messg.as_string())



q=sub.replace(" ","")

path='/var/www/test/outage/'
os.system('touch /var/www/html/outage/{0}.html'.format(q))


d={'Date':d,'Time':t,'Downtime':st,'Issue':out,'Jira':j,'Slack':slk,'Application Impacted':app,'Buisness Impacted':bu,'Region Impacted':re,'Summary':l}

import json

with open(path+q+'.json','w') as f:
	json.dump(d,f)

par="""
<head>
<title>NOC Outage Tool</title>"

<link type="text/css" rel="stylesheet" href="/css/style1.css">
<link href="https://fonts.googleapis.com/css?family=Oleo+Script" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Orbitron" rel="stylesheet">
<link href="/css/bootstrap.min.css" rel="stylesheet" />

</head>

<body>

<div class="container-fluid dark ">
        <div class="wrapper">
                <div id="logo_left">
                        <h3 style="color: white;margin-top: 0px;margin-left: 500px;align: center;font-family: 'Orbitron', sans-serif;"><u>NOC  &nbsp;  Outage &nbsp;  Tool</u></h3>

                </div>
        </div>          
</div>
<div class="container-fluid  dark">
        <div class="wrapper">

                <ul >
                        <li><a href="/cgi-bin/pts_c.py">Home</a></li>
                        <li><a href="http://localhost:82/test/updated_outage/button.html">Outage Function</a></li>
                        <li><a href="http://localhost:82/test/updated_outage/jira_create.html">Jira Action</a>
                                <ul>
                                        <li><a href="http://localhost:82/test/updated_outage/jira_create.html">Create</a></li>
                                        <li><a href="#">Update</a></li>
                                </ul>
                        </li>
                        <li><a href="http://localhost:82/test/updated_outage/slack_channel.html">Slack Action</a>
                                <ul>
                                        <li><a href="http://localhost:82/test/updated_outage/slack_channel.html">Channel Creation</a></li>
                                        <li><a href="http://localhost:82/test/updated_outage/slack_message.html">Message</a></li>
                                </ul>
                        </li>
                </ul>
        </div>
</div>

"""
frm= """<form action="/cgi-bin/pt_final.py" method="get">

	New Comment: <br/>
	<textarea name="comm" style="height:100px; width:320px;" required="required"></textarea>
       <input type="submit" value="submit" style="margin-top: 50px;background-color: #003366;border-radius:5px;color: white;width: 80px;height:40px;">
	</form>
"""



with open(path+q+'.html','w') as f:
	f.write(par)
	f.write("\n")
	f.write(msg)
	f.write("\n")
	f.write(de)
	f.write("\n")
	f.write(upt)
	f.write("\n")
	f.write(frm)
	f.close()

