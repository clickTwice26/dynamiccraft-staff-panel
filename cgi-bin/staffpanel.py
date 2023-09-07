#!/usr/bin/python3
import cgi
import os
import func as f
import frontend as fd
import constant as C
import sys
formdata = cgi.FieldStorage()
status = formdata.getvalue("status")
uname = formdata.getvalue("uname")
token = formdata.getvalue("token")
print("")

f.security_check(f.get_ip_address(), uname)
if f.value_checker([str(status),str(uname), str(token)]):
    pass
else:
    print("")
    print("Invalid Input")
    sys.exit()
if f.tokencheck(token, "logged_in"):
    f.tokendel(token, "logged_in")
    new_token = f.tokengen()
    f.tokenset(new_token, "logged_in")
    print("")
    fd.staff_panel(uname, "offline", new_token)
else:
    f.tokendel(token, "logged_in")
    print("Invalid Session")
    sys.exit()

