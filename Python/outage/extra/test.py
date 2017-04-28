#!/usr/bin/python

import codecs

file=open('hey.txt','r')
s=file.read()
f=codecs.open("/var/www/html/outage/{0}".format(s),'r','utf-8')
print f.read()


