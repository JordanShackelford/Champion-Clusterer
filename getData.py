import requests
import json
from tkinter import *

def saveAPIKey():
	myAPIKey = e1.get()
	print("Your API key has been saved as " + myAPIKey)
	sendQueryAndPrintResponse(myAPIKey)
	
def sendQueryAndPrintResponse(APIKey):
	response = requests.get("http://api.champion.gg/v2/champions?&api_key=" + APIKey)
	content = response.content
	#print(content)
	jcontent = json.loads(content.decode('utf8'))
	#print(jcontent)
	
	print(len(jcontent))
	
master = Tk()
master.resizable(False,False)
Label(master, text="Your API Key: ").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)
b = Button(master, text="Get Data", command = saveAPIKey)
b.grid(row=0, column=3)

eloVar = IntVar() #all the radio buttons are tied to this variable
Radiobutton(master, text="Silver", variable=eloVar, value=1, indicatoron=0).grid(row=1,column=0)
Radiobutton(master, text="Gold", variable=eloVar, value=2, indicatoron=0).grid(row=1,column=1)
Radiobutton(master, text="Platinum", variable=eloVar, value=3, indicatoron=0).grid(row=1,column=2)
Radiobutton(master, text="Diamond", variable=eloVar, value=4, indicatoron=0).grid(row=1,column=3)

w = Scale(master, label="# of Clusters:", from_= 0, to = 100, orient=HORIZONTAL).grid()
mainloop( )






'''



# printing response instead of response.content will not display the data--------

print(content) 
# bytes object needs to be decoded to a string to be used as a JSON object

#--------------------------------------------------------------------------------
'''
