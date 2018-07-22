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
cbvar1 = IntVar()
Checkbutton(master, text="Silver", variable=cbvar1).grid(row=2, column=0)
cbvar2 = IntVar()
Checkbutton(master, text="Gold", variable=cbvar2).grid(row=2, column=1)
cbvar3 = IntVar()
Checkbutton(master, text="Platinum", variable=cbvar3).grid(row=2, column=2)
cbvar4 = IntVar()
Checkbutton(master, text="Diamond", variable=cbvar4).grid(row=2, column=3)
mainloop( )






'''



# printing response instead of response.content will not display the data--------

print(content) 
# bytes object needs to be decoded to a string to be used as a JSON object

#--------------------------------------------------------------------------------
'''
