#!/usr/bin/python

print "Content-Type: text/html"
print ""

import cgi, cgitb
import re
import smtplib
import codecs
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
#from datetime import datetime

cgitb.enable()


form=cgi.FieldStorage()
st=form.getvalue('status')
sub=form.getvalue('subject')
com=form.getvalue('comment')
up=form.getvalue('update')


cm=com.split('\n')

check=re.search("Communication(.*)",sub)
new=check.group()
i=new.split()
x=i.remove('Communication')

j=' '.join(i).replace(" ","")


html_file=j+'.html'


ot=open('/var/www/test/outage/%s'%(html_file),'r')
bt=ot.read()
pt=re.search(r'Time(.*)',bt)
qt=re.search(r'\d+(.*)',pt.group())
mt=qt.group().split()
nt=mt[0]


dt=datetime.datetime.now().strftime('%H:%M')
print dt
FMT='%H:%M'

df=datetime.datetime.strptime(dt,FMT)-datetime.datetime.strptime(nt,FMT)
jt=df.seconds/60

print jt

with open('/var/www/test/outage/%s'%(html_file),'r+') as fn:
        sn=fn.read()
        dn=re.search(r'Downtime</b>:([0-9]+)',sn)
        jn='Downtime</b>:%d'%(jt)
        xn=dn.group()
        sn=re.sub(xn,jn,sn)
        fn.seek(0)
        fn.truncate()

with open('/var/www/test/outage/%s'%(html_file),'a') as gn:
        gn.write(sn)
        gn.close()





m=open('/var/www/test/outage/%s'%(html_file),'r+')
o=m.readlines()
m.seek(0)
ko="<b>ETA:</b>NA<br><br>Regards & Thanks<br>NOC"
for i in o:
	if i !=ko:
		m.write(i)
			
m.truncate()
m.close()



gj=open('/var/www/test/outage/%s'%(html_file),'r')
fg=gj.read()
gj.close()
mk=re.search(r'Next Update(.*)',fg)

ph=fg.replace(mk.group(),'')

gj=open('/var/www/test/outage/%s'%(html_file),'w')
gj.write(ph)
gj.close()


s=open("/var/www/test/outage/%s"%(html_file)).read()
z=re.search('style(.*)',s)
x=z.group()


if st=="amber" and x=="style='color:red'><b><u>Status:</u></b>RED</p>":
	s=s.replace(x,"style='color:orange'><b><u>Status:</u></b>AMBER</p>")
	f=open("/var/www/test/outage/%s"%(html_file),'w')
	f.write(s)
	f.close()
elif st=="amber" and x=="style='color:green'><b><u>Status:</u></b>GREEN</p>":
        s=s.replace(x,"style='color:orange'><b><u>Status:</u></b>AMBER</p>")
        f=open("/var/www/test/outage/%s"%(html_file),'w')
        f.write(s)
        f.close()
elif st=="resolved" and x=="style='color:red'><b><u>Status:</u></b>RED</p>":
	s=s.replace(x,"style='color:green'><b><u>Status:</u></b>GREEN</p>")
        f=open("/var/www/test/outage/%s"%(html_file),'w')
        f.write(s)
        f.close()

elif st=="resolved" and x=="style='color:orange'><b><u>Status:</u></b>AMBER</p>":
	s=s.replace(x,"style='color:green'><b><u>Status:</u></b>GREEN</p>")
        f=open("/var/www/test/outage/%s"%(html_file),'w')
        f.write(s)
        f.close()

elif st=="red" and x=="style='color:orange'><b><u>Status:</u></b>AMBER</p>":
	s=s.replace(x,"style='color:red'><b><u>Status:</u></b>RED</p>")
        f=open("/var/www/test/outage/%s"%(html_file),'w')
        f.write(s)
        f.close()
elif st=="red" and x=="style='color:green'><b><u>Status:</u></b>GREEN</p>":
	s=s.replace(x,"style='color:red'><b><u>Status:</u></b>RED</p>")
        f=open("/var/www/test/outage/%s"%(html_file),'w')
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

#print l.remove('<ul><li>\r</li></ul>')
 
#val="<br><ul><li>{0}</li></ul>".format(com)	

foot="<b>ETA:</b>NA<br><br>Regards & Thanks<br>NOC"
upt="<b>Next Update:</b>%s <br><br>"%(up)

with open("/var/www/test/outage/%s"%html_file, "a") as f:
	for ca in l:
		f.writelines(ca)
		f.write('\n')
	f.write('\n')
	f.write(upt)
	f.write('\n')	
	f.write(foot)
	f.close()

ab=codecs.open('/var/www/test/outage/%s'%html_file)
bc=ab.read()
ab.close()
if "view" in form:
	print bc
	print """
	<FORM><INPUT Type="button" VALUE="Back" onClick="history.go(-1);return true;"></FORM>
	"""
elif "send" in form:
	receipents = ['<receiver1>','<receiver1>']

	def py_mail(SUBJECT, BODY, TO, FROM):
    		MESSAGE = MIMEMultipart('alternative')
    		MESSAGE['subject'] = SUBJECT
    		MESSAGE['To'] = ",".join(receipents)
    		MESSAGE['From'] = FROM
    		HTML_BODY = MIMEText(BODY, 'html')
    		MESSAGE.attach(HTML_BODY)
    		server = smtplib.SMTP('<mail server>')
    		server.sendmail(FROM, TO, MESSAGE.as_string())
    		server.quit()
	if __name__ == "__main__":
    		"""Executes if the script is run as main script (for testing purposes)"""
    		email_content =bc
    
    		FROM = '<sender email-id>'
    
    		py_mail(sub, email_content, receipents, FROM)

else:
    print "Couldn't determine which button was pressed."
