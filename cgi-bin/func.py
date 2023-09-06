import time
import sys
from datetime import datetime
import random 
import requests
import constant
import os
import string

import json


# Call the function to get the IP address

def currentTime(what="all"): #error = 0001

	error = "0001"
	# datetime object containing current date and time
	try:
		now = datetime.now()
		# dd/mm/YY H:M:S
		dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	except Exception as error:
		print(f"Error Faced: {error}")
		sys.exit("ERROR-00001")		
	if what in ["date", "time"]:
		if what  == "date":
			date = now.strftime("%d/%m/%Y")
			date = str(date)
			return date
		elif what == "time":
			time = str(now.strftime("%H:%M:%S"))
			return time
		elif what == "all":
			dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
			date_time = str(dt_string)
			return date_time
	else:
		# print("Invaild Argument")
		# print("Returing)
		dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
		date_time = str(dt_string)
		return date_time
def line_prepender(filename, string):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(string.rstrip('\r\n') + '\n' + content)
def passivelogger(log,error="regular-log"):
	logname = "passivelog.txt"
	log_dir = constant.log_folder+f"/{logname}"
	log = f"[PASSIVE-{error}]-[{currentTime()}]-[{log}]"
	try:
		line_prepender(log_dir, log)
	except FileNotFoundError:
		print("File Not Found-Error Code = 0002->0003")

		#error-fix-0003
		with open(log_dir,"w") as errorfix0003:
			errorfix0003.write("")
			errorfix0003.close()
	# finally:
	# 	line_prepender(log_dir,log)
def errorlog(error, log):
	logname = "errorlog.txt"
	log_dir = constant.log_folder+f"/{logname}"
	log = f"[PASSIVE-{error}]-[{currentTime()}]-[{log}]"
	try:
		line_prepender(log_dir, log)
	except FileNotFoundError:
		print("File Not Found-Error Code = 0002->0003")

		#error-fix-0003
		with open(log_dir,"w") as errorfix0003:
			errorfix0003.write("")
			errorfix0003.close()
	finally:
		line_prepender(log_dir,log)

def tokengen():

	new_token = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
	passivelogger(f"Token Generated at {currentTime()} | {new_token}")
	return new_token
def tokenset(token, timeframe):
	token_db = constant.admin_dir+"tokens/"
	token,timeframe = str(token), str(timeframe)
	timeframe = token+"_"+timeframe
	# print(token)
	
	try:
		with open(token_db+timeframe, "w") as tokenlogger:
			tokenlogger.write(token)
			tokenlogger.close()
	except Exception as error:
		errorlog("0004", error)
def tokencheck(token, timeframe):
	token_db = constant.admin_dir+"tokens/"
	token, timeframe = str(token), str(timeframe)
	#print(token)
	timeframe = token+"_"+timeframe

	try:
		previous_token = open(token_db+timeframe,"r").read()
		x = "pure"
	except FileNotFoundError:
		x = "nice"
		return False
	if x != "nice":
		previous_token = open(token_db+timeframe,"r").read()
		if token == previous_token:
			return True
		else:
			# print("")
			# print("Invaild Session")
			return False

		
	
	# previous_token = open(token_db+timeframe,"r").read()

def tokendel(token, timeframe):
	token_db = constant.admin_dir+"tokens/"
	# token_db = constant.admin_dir+"tokens/"
	token, timeframe = str(token), str(timeframe)
	timeframe = token+"_"+timeframe
	os.system(f"cd {token_db} && rm {timeframe}")



def get_ip_address():
    url = 'https://api.ipify.org'
    response = requests.get(url)
    ip_address = response.text
    return ip_address
def ip_log(comment="uncommented"):
	ip = get_ip_address()
	ip = "0.0.0.0"
	passivelogger(f"{ip}-{comment}")

def security_check(ip, username="unknown"):
	banned_ip=open(constant.admin_dir+"logs/bannedip.txt", "r").read().splitlines()
	if ip in banned_ip:
		print("")
		print("You are ip banned from this panel")
		passivelogger(f"{banned_ip} banned ip | username")
		sys.exit()
		# return False
	else:
		banned_user = open(constant.admin_dir+"logs/banneduser.txt", "r").read().splitlines()
		if username != "unknown":
			if username in banned_user:
				print("")
				print("You are banned from this panel")
				# return False
				sys.exit()
			else:
				timeout = open(constant.admin_dir+"logs/timeout.txt", "r").read().splitlines()
				if username in timeout:
					time.sleep(constant.timeout_time)
					# return True
def loginverification(username, password, token):
	username_dir = constant.login+"usernames.txt"
	password_dir = constant.login+"passwords.txt"
	username_list = open(username_dir, "r").read().splitlines()
	if username in username_list:
		user_index = username_list.index(username)
		print(user_index)
		print("Username matched")

		password_list = open(password_dir,"r").read().splitlines()
		if password in password_list:
			if password == password_list[user_index]:
				print("")
				# print("Password Matched")
				print(token)
				tokenset(token, "logged_in")
				return "1"
			else:
				problem = "Wrong Password"
				# print("Password didn't matched")
				return "01"
		else:
			problem = "Wrong Password"
			# print("Password didn't found")
			return "02"
	else:
		
		problem = "You are not registered"
		# print("Username not found")
		return "03"
def emailverification(suspectemail):
	temp_mail = str(suspectemail)
	if temp_mail.endswith("@gmail.com") or temp_mail.endswith("@yahoo.com") or temp_mail.endswith("@proton.me"):
		return True
	else:
		return False
def passwordverify(password1, password2):
	if password1 == password2:
		return True
	else:
		return False
def roleverify(role):
	if role in ["scout", "moderator", "builder"]:
		return True
	else:
		return False
	
def database_init(username):
	init_date = currentTime("date")
	init_year = int(init_date.split("/")[2])
	init_month = int(init_date.split("/")[1])
	month_array = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
	final_month = month_array[init_month-1]
	left_month = month_array[init_month-1:]
	# final_date = init_date.replace("/","_")
	databasedir = constant.admin_dir+f"userdata/{username}/"
	try:
		os.mkdir(databasedir+str(init_year))
	except FileNotFoundError:
		print("User not found")
		sys.exit()
	except FileExistsError:
		pass
	for i in left_month:
		try:
			os.mkdir(databasedir+str(init_year)+"/"+i)
		except FileExistsError:
			pass
	

	# print(init_year, init_month, final_month)


class User:
	"""Base class for all the users"""
	def __init__(self, username, password, token, role, ip) -> None:
		self.username = username
		self.password = password
		self.token = token
		self.role = role
		self.ip = ip
	def createdetailsverify(self,username, newpassword, confirmpassword, email, role):
		if username not in open(constant.admin_dir+"login/usernames.txt").read().splitlines() or username != "unknown":
			if emailverification(email):
				print("")
				if passwordverify(newpassword, confirmpassword):
					if roleverify(role):
						return "1"
					else:
						return "2"
				else:
					return "3"
			else:
				return "4"
		else:
			return "5"			

	def create(self,newpassword, confirmpassword, email, role):
		userdir = constant.userdir+f"{self.username}/{self.username}.json"
		print(userdir)
		currentstatus = "offline"
		
		usertemplate = {
			"username": self.username,
			"ip": self.ip,
			"role": self.role,
			"currentstatus": currentstatus,
			"creation_date:": currentTime("all"),
			"last_login": currentTime(all)
			}
		try:
			os.mkdir(constant.userdir+f"{self.username}")
		except Exception as e:
			print(e)
			print("Creating a new username directory was no successful")
		userdata_json = json.dumps(usertemplate, indent=4)
		with open(userdir, "w") as jsoncreater:
			jsoncreater.write(userdata_json)
			jsoncreater.close()
		database_init(self.username)
		# with open(userdir, 'r+') as f:
		# 	data = json.load(f)
		# 	data['id'] = 134 # <--- add `id` value.
		# 	f.seek(0)        # <--- should reset file position to the beginning.
		# 	json.dump(data, f, indent=4)
		# 	f.truncate()     # remove remaining par
	def changestatus(self, status):	
		userdir = constant.userdir+f"{self.username}/{self.username}.json"
		userJSON = open(userdir,"r")
		userJSONdata = json.load(userJSON)
		userJSON.close()
		#checking valid data of status variable
		if status in ["online", "offline"]:
			if not userJSONdata["currentstatus"] == status:
				passivelogger(f"{self.username} changed status {userJSONdata['currentstatus']} to {status}")
				userJSONdata["currentstatus"] = status
				userdata_json = json.dumps(userJSONdata, indent=4)
				with open(userdir, "w") as jsoncreater:
					jsoncreater.write(userdata_json)
					jsoncreater.close()
								
			else:
				print("current status same")
		else:
			print(f"Invalid-status: {status}")
	


	