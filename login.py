#!/usr/bin/env python3
import cgi
import secret
from templates import *
import os 





form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

if ((username == secret.username) and (password == secret.password)):
    print('Set-Cookie: Username = %s' % secret.username)
    print('Set-Cookie: Password = %s' % secret.password)
    print('Content-type: text/html\r\n\r\n')
    print(secret_page(secret.username, secret.password))
else:
    if (username == None) and (password == None) and (i == 'HTTP_COOKIE' for i in os.environ.keys()):
        print('Content-type: text/html\r\n\r\n')
        print(secret_page(secret.username, secret.password))
    else:
        print('Content-type: text/html\r\n\r\n')
        print(after_login_incorrect())

