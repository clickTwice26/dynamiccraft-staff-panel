#!/usr/bin/python3
# import cgi,cgitb
import func
import frontend
import cgi
import sys
func.security_check(func.get_ip_address(), "unknown")

print("")
token_init = func.tokengen()
func.tokenset(token_init, "loginpage")
frontend.login(token_init)