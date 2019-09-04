import requests
from requests.auth import HTTPDigestAuth
import json

baseurl = "https://lab10-viyaweb.lab.local"

###############################################################################################
# 1) Get Access Token
#
# In a real case, an app would have been registered in SAS Viya with the procedure detailed in:
# https://developer.sas.com/reference/auth/
# In this case we are usinfg the default sas application sas.ec (no password)
###############################################################################################

app_name = 'sas.ec'
app_secret = ''
# app_name = 'aBeatifulApp'
# app_secret = 'aSuperSecretPassword'
encoding = app_name+':'+app_secret

username = 'siro'
password = 'Orion123'

token_url = "/SASLogon/oauth/token"
headers = {'Content-Type': 'application/x-www-form-urlencoded',
           'Accept': 'application/json'}
requestBody = {'grant_type':'password','username':username,'password':password}

# Get OAUTH Token
myResponse = requests.post(baseurl+token_url, auth=(app_name,app_secret), headers=headers, verify=r'C:/dev/viyacertificates/NordicLabs/NordicLabs_Bundle.pem', data=requestBody)
result = myResponse.json()

access_token = result['access_token']

###############################################################################################
# 2) Get CAS metrics
###############################################################################################



