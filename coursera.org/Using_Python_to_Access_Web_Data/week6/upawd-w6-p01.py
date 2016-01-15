import json
import urllib

# getting url from user
url = raw_input('Enter location: ')
if len(url) < 1: url = "http://python-data.dr-chuck.net/comments_42.json"

# url handler
print "Retrieving", url
uh = urllib.urlopen(url)

# load json
data = uh.read()
info = json.loads(data)
print "Retrieved %i characters" % len(data)

# parse json, get numbers
comments = [ int(c['count']) for c in info['comments'] ]
print "Count:", len(comments)
print "Sum:", sum(comments)
