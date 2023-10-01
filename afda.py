import requests
import ast
import time 

url = 'https://www.m8clicks.com/_View/svPage/RMOdds1Gen.ashx?ov=0&ot=r&tf=-1&TFStatus=0&update=false&r=1686067981&mt=0&wd=&ia=0&isWC=False&isSiteFav=False&LID=dbc331d821743a04&_=' + str(time.time() * 1000)

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200 indicates success)
if response.status_code == 200:
    # Access the content of the response
    data = response.text
    data = data.replace('[,', '[')
    data = ast.literal_eval(data)
    print(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")