#!/usr/bin/python3
import cgi
import os
import func as f
import frontend as fd
import constant as C
import sys
import json
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
    role = "staff"
    staff = f.User(uname, "from_staff", token, role, f.get_ip_address())
    if staff.changestatus(status):
        if status == "online":
            staff.activityupdate(status)
        if status == "offline":
            userdir = C.userdir+f"{uname}/{uname}.json"
            userJSON = open(userdir,"r")
            userJSONdata = json.load(userJSON)
            userJSON.close()
            id = userJSONdata["status_id"]
            staff.activityupdate(status, id)
    else:
        print("Could'nt update")
        sys.exit()

    fd.staff_panel(uname, new_token)

else:
    f.tokendel(token, "logged_in")
    print("Invalid Session")
    sys.exit()

