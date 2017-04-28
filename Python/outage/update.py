#!/usr/bin/python

print "Content-Type: text/html"
print ""

import cgi, cgitb

form=cgi.FieldStorage()

val=form.getvalue('file')

print "<head>"
print '<meta charset="utf-8">'
print '<meta http-equiv="X-UA-Compatible" content="IE=edge">'
print '<meta name="viewport" content="width=device-width, initial-scale=1">'
print '<title>Update Incident</title>'
print '<link rel="stylesheet" href="update.css">'
print '<body>'
print '<div class="main-content">'
print '<form class="form-basic" method="post" action="/cgi-bin/outage/mail_update.py" style="margin-top:6%; margin-bottom:6%;">'
print '<div class="form-title-row">'
print '<h1>Update Incident</h1>'
print '</div>'          
print '<div class="form-row">'
print '<label>'
print '<span>Status:</span>'
print '<select name="status" style="width:100px;">'
print '<option value="red">RED</option>'
print '<option value="amber">AMBER</option>'
print '<option value="resolved">Resolved</option>'
print '</select>'
print '</label>'
print '</div>'
print '<div class="form-row">'
print '<label>'
print '<span>Subject:</span>'
print '<textarea name="subject" style="margin-left:5%;" required="required"></textarea>'
print '</label>'
print '</div>'
print '<div class="form-row">'
print '<label>'
print '<span>Description:</span>'
print '</label>'
print '<iframe name="desc" class="form-row" src="/outage/{0}" style="width: 90%;height: 600px;margin-left: 5%;">'.format(val)
print '</iframe>'
print '</div>'
        
print """    
<div class="form-row">
<button style="margin-left:50%"><a href="#" >Create</a></button>
</div>
</form>
</div>
</body>

"""

with open('hey.txt','w') as f:
	f.write(val)
	f.close()

