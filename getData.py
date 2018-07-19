import requests
import json

MYAPIKEY = input()

response = requests.get("http://api.champion.gg/v2/champions?elo=SILVER&api_key=" + MYAPIKEY)

# printing response instead of response.content will not display the data--------
content = response.content
print(content) 
# bytes object needs to be decoded to a string to be used as a JSON object
jcontent = json.loads(content.decode('utf8'))
print(jcontent)
#--------------------------------------------------------------------------------
