#!/usr/bin/python3
import cgi
import os
import func as f
import frontend as fd
import constant
import sys
ip = f.get_ip_address()
formdata = cgi.FieldStorage()
admin_token = formdata.getvalue("admin_token")
uname = formdata.getvalue("uname")
passw = formdata.getvalue("passw")
newpassw = formdata.getvalue("newpassw")
confirmpassw = formdata.getvalue("confirmpassw")
email = formdata.getvalue("email")
token = formdata.getvalue("token")
role = formdata.getvalue("role")
newuser = f.User(uname,newpassw, token, role, ip)
# f.security_check(ip, "unknown")
if f.tokencheck(token, "reg_page"):
    pass
else:
    print("")
    print("Invaild Session")
    sys.exit()
f.tokendel(token,"reg_page")

if admin_token in os.listdir(constant.admin_dir+"login/registration_token/"):
    # os.rmdir(constant.admin_dir+f"login/registration_token/{admin_token}")
    pass
else:
    print("")
    print("You are not allowed to create an account")
    sys.exit()


verify = newuser.createdetailsverify(uname, newpassw, confirmpassw, email, role)
if verify == "1":
    newuser.create(newpassw, confirmpassw, email, role)

elif verify == "2":
    print("Invaild Role Request")
elif verify == "3":
    print("Password didn't match")
elif verify == "4":
    print("Invaild Email")
elif verify == "5":
    print("Username not available")

