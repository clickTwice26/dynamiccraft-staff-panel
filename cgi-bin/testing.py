#!/usr/bin/python3
import cgi
data = cgi.FieldStorage()
username = data.getvalue("uname")
print("")
print(username)