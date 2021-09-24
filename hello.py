#!/usr/bin/env python3
import os
import json
from templates import *

print("Content-type: text/html\r\n\r\n")
print("<title>Test CGI</title>")
print("<p>Hello World CMPUT404!</p >")
#print(os.environ)

env_js = json.dumps(dict(os.environ), indent=4)
#print(env_js)

for i in os.environ.keys():
    if (i == 'QUERY_STRING'):
        print('<b>%20s</b>: %s<br>' % (i, os.environ[i]))

for i in os.environ.keys():
    if (i == 'HTTP_USER_AGENT'):
        print('<b>%20s</b>: %s<br>' % (i, os.environ[i]))


print(login_page())