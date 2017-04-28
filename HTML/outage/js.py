#!/usr/bin/python

print "Content-type: text/html"
print ""

import json

g='NewTestingOutage.json'

with open(g) as f:
	d=json.load(f)


print d

c=g.split('.')

print """
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>


<body>

<table>
  <tr>
    <th>Issue</th>
    <th>Application Impacted</th>
    <th>Jira</th>
    <th>Slack</th>
   <th>Status</th>
  </tr>
  <tr>
    <td>{0}</td>
    <td>{1}</td>
    <td>{2}</td>
    <td>{3}</td>
   <td>{4}</td>
  </tr>
</table>

</body>
""".format(c[0],d['Application Impacted'],d['Jira'],d['Slack'],d['Downtime'])


