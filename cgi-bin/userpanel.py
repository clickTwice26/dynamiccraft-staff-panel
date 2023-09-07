#!/usr/bin/python3
import cgi
import os
import func
import sys
import frontend as fd
import constant
import func
#form-value
formdata = cgi.FieldStorage()
username=formdata.getvalue("uname")
password=formdata.getvalue("passw")
token = formdata.getvalue("token")
# ip = func.get_ip_address() #for privacy
ip = "0.0.0.0"
#file-details
func.security_check(ip, username)
print("")
if func.tokencheck(token, "loginpage"):
    func.tokendel(token, "loginpage")
    #new-token-for-staff-panel
    new_token = func.tokengen()
    verif = func.loginverification(username, password, new_token)
    if verif == "1":
        # print("")
        # print("Login Successful")
        staff_token = func.tokengen()
        func.tokenset(staff_token, "logged_in")
        fd.staff_panel(username, "online", staff_token)
    elif verif == "01":
        print("Password didn't match")
    elif verif == "02":
        print("Password not found")
    elif verif == "03":
        print("You are not registered")
    else:
        print("Unknow error")
else:
    print("")
    print("Invalid Session")
    
    
    func.tokendel(token, "loginpage")
    sys.exit()
filename = "userpanel.py"
func.passivelogger(f"{filename} accessed|{username}|{ip}|{password}|{token}")

# print("")
# print(formdata,username,password,token,sep="\n")
