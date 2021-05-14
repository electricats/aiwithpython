import requests

# this code can help you generate accessToken
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=P3UGM0YGLR5Uw2GOrrOFSQ41&client_secret=3hki6KCCfItLPcvPHK95G0pn88x0G9sG'
response = requests.get(host)
if response:
    print(response.json())