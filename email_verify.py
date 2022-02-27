import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('sitarealemail_API')

email_address = "aidenpearcewd01@gmail.com"
response = requests.get(
    "https://isitarealemail.com/api/email/validate",
    params = {'email': email_address},
    headers = {'Authorization': "Bearer " + api_key })

status = response.json()['status']
if status == "valid":
  print("email is valid")
elif status == "invalid":
  print("email is invalid")
else:
  print("email was unknown")