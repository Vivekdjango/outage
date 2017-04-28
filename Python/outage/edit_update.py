#!/usr/bin/python

print "Content-Type: text/html"
print ""

import cgi, cgitb
import re
import smtplib
import codecs
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




form=cgi.FieldStorage()
st=form.getvalue('status')
sub=form.getvalue('subject')
com=form.getvalue('comment')


print com

cm=com.split('\n')

print cm

check=re.search("Communication(.*)",sub)
new=check.group()
i=new.split()
x=i.remove('Communication')

j=' '.join(i).replace(" ","")


html_file=j+'.html'


m=open('/var/www/html/outage/%s'%(html_file),'r+')
o=m.readlines()
m.seek(0)
for i in o:
	if i !="<b>ETA:</b>NA<br><br>Regards & Thanks<br>NOC":
		m.write(i)
m.truncate()
m.close()




s=open("/var/www/html/outage/%s"%(html_file)).read()
z=re.search('style(.*)',s)
x=z.group()


if st=="amber" and x=="style='color:red'><b><u>Status:</u></b>RED</p>":
	s=s.replace(x,"style='color:orange'><b><u>Status:</u></b>AMBER</p>")
	f=open("/var/www/html/outage/%s"%(html_file),'w')
	f.write(s)
	f.close()
elif st=="amber" and x=="style='color:green'><b><u>Status:</u></b>GREEN</p>":
        s=s.replace(x,"style='color:orange'><b><u>Status:</u></b>AMBER</p>")
        f=open("/var/www/html/outage/%s"%(html_file),'w')
        f.write(s)
        f.close()
elif st=="resolved" and x=="style='color:red'><b><u>Status:</u></b>RED</p>":
	s=s.replace(x,"style='color:green'><b><u>Status:</u></b>GREEN</p>")
        f=open("/var/www/html/outage/%s"%(html_file),'w')
        f.write(s)
        f.close()

elif st=="resolved" and x=="style='color:orange'><b><u>Status:</u></b>AMBER</p>":
	s=s.replace(x,"style='color:green'><b><u>Status:</u></b>GREEN</p>")
        f=open("/var/www/html/outage/%s"%(html_file),'w')
        f.write(s)
        f.close()

elif st=="red" and x=="style='color:orange'><b><u>Status:</u></b>AMBER</p>":
	s=s.replace(x,"style='color:red'><b><u>Status:</u></b>RED</p>")
        f=open("/var/www/html/outage/%s"%(html_file),'w')
        f.write(s)
        f.close()
elif st=="red" and x=="style='color:green'><b><u>Status:</u></b>GREEN</p>":
	s=s.replace(x,"style='color:red'><b><u>Status:</u></b>RED</p>")
        f=open("/var/www/html/outage/%s"%(html_file),'w')
        f.write(s)
        f.close()


#with open("/var/www/html/outage/%s"%html_file, "r") as f:
#        lines = f.readlines()

#for index, line in enumerate(lines):
#    if line.startswith("ETA \n"):
#        break
#lines.insert(index, "<br><ul><li>{0}</li></ul>".format(com))
#
l=[]
for v in cm:
	val="<ul><li>%s</li></ul>"%(v)
	l.append(val)

print l
#print l.remove('<ul><li>\r</li></ul>')
 
#val="<br><ul><li>{0}</li></ul>".format(com)	

foot="<b>ETA:</b>NA<br><br>Regards & Thanks<br>NOC"


with open("/var/www/html/outage/%s"%html_file, "a") as f:
	for ca in l:
		f.writelines(ca)
		f.write('\n')
	f.write('\n')	
	f.write(foot)
	f.close()

ab=codecs.open('/var/www/html/outage/%s'%html_file)

bc=ab.read()

def py_mail(SUBJECT, BODY, TO, FROM):
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['From'] = FROM
    HTML_BODY = MIMEText(BODY, 'html')
    MESSAGE.attach(HTML_BODY)
    server = smtplib.SMTP('<mail server>')
    server.sendmail(FROM, [TO], MESSAGE.as_string())
    server.quit()
if __name__ == "__main__":
    """Executes if the script is run as main script (for testing purposes)"""
    email_content =bc
    
    FROM = '<sender email-id>'
    TO ='<receiver1>'

    py_mail(sub, email_content, TO, FROM)
