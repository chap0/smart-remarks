#!/usr/bin/env python
# Smart Remarks is a simple script that scrapes comments out of HTML
# currently it supports two functions, web scraping a single site from
# user input and providing a list to read from. Both must be provided
# in URL format with the preceding "http[s]://". The URLs provided in
# from a file, each URL must be on a seperate line.
# Questions/comments: 0xchap0@gmail.com
# Updates are planned I would like the script to take arguments in the CLI

import urllib, re

from htmlentitydefs import name2codepoint
from HTMLParser import HTMLParser

class GrabComment(HTMLParser):
        def handle_comment(self, data):
                print "Comment Found: ", data
optone = '1'
opttwo = '2'

print ("SMART REMARKS - Scraping comments from html")
print ("Enter 1 for a single site scan or 2 to read from a file")

start = raw_input("Enter 1 or 2: ")

if not start:
	print ("Enter 1 for a single site scan or 2 to read from a file.")
	exit()
if re.match(start,optone):

	target = raw_input("Enter target site: ")
	if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', target):
       		site = urllib.urlopen(target)
       		parser = GrabComment()
       		parser.feed(site.read())
       		parser.close()
       		site.close()
		print ("[+]Done with: %s" % target) 
       		exit(1)
	else:
       		print ("URL invalid. Enter a valid URL.\n eg: http[s]://www.example.com")
        	exit()

elif re.match(start, opttwo):

	print("URLs must contain http:// or https://. Each URL on a single line.")
	usrfile = raw_input("Enter a filename with URLs: ")
	print "In the Loop..."

	with open(usrfile) as f:
		for line in f:
			if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line):
				site = urllib.urlopen(line)
				parser = GrabComment()
				parser.feed(site.read())
				parser.close()
				site.close()
				print ("[+] Done with: %s" % line)
