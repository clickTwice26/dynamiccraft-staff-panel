import sys
from datetime import datetime
def currentTime(what):


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
