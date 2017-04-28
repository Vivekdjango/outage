import re
with open('/var/www/html/outage/Vivektest.html','r+') as f:
	s=f.read()
	d=re.search(r'Downtime</b>:([0-9]+)',s)
	j='Downtime</b>:90'
	x=d.group()
	s=re.sub(x,j,s)
	f.seek(0)
	f.truncate()

with open('/var/www/html/outage/Vivektest.html','a') as g:
	g.write(s)
	g.close()
	

