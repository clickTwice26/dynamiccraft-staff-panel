import os
import requests
import constants

def error_fixer(code):
    code = str(code)
    if code == "0002":
        os.system(f"cd {constants.admin_dir} && mkdir logs")
        print("Error fixed")