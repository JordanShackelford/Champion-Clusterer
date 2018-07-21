import requests
import json
from tkinter import *

def saveAPIKey():
	myAPIKey = e1.get()
	print("Your API key has been saved as " + myAPIKey)

master = Tk()
myAPIKey = ""
Label(master, text="Your API Key: ").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)
b = Button(master, text="SUBMIT", command=saveAPIKey)
b.grid(row=0, column=2)
mainloop( )



'''
MYAPIKEY = input()

response = requests.get("api.champion.gg/v2/champions/1=" + MYAPIKEY)

# printing response instead of response.content will not display the data--------
content = response.content
print(content) 
# bytes object needs to be decoded to a string to be used as a JSON object
jcontent = json.loads(content.decode('utf8'))
print(jcontent)
#--------------------------------------------------------------------------------
'''
