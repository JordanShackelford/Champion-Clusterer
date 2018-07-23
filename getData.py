import requests
import json
from tkinter import *

def saveAPIKey():
	myAPIKey = e1.get()
	print("Your API key has been saved as " + myAPIKey)
	sendQueryAndPrintResponse()
	
def sendQueryAndPrintResponse():
	response = requests.get("http://api.champion.gg/v2/champions/1&api_key=" + myAPIKey)
	content = response.content
	print(content)
	#jcontent = json.loads(content.decode('utf8'))
	#print(jcontent)
	
master = Tk()
master.resizable(False,False)
myAPIKey = ""
Label(master, text="Your API Key: ").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)
b = Button(master, text="Get Data", command = saveAPIKey)
b.grid(row=0, column=2)

eloVar = IntVar() #all the radio buttons are tied to this variable
Radiobutton(master, text="Silver", variable=eloVar, value=1).grid(row=1,column=0)
Radiobutton(master, text="Gold", variable=eloVar, value=2).grid(row=1,column=1)
Radiobutton(master, text="Platinum", variable=eloVar, value=3).grid(row=1,column=2)
Radiobutton(master, text="Diamond", variable=eloVar, value=4).grid(row=1,column=3)
mainloop( )






'''



# printing response instead of response.content will not display the data--------

print(content) 
# bytes object needs to be decoded to a string to be used as a JSON object

#--------------------------------------------------------------------------------
'''
