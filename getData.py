import requests
import json
from tkinter import *
from sklearn.cluster import KMeans
import numpy as np
import io
import base64
import urllib.request

def saveAPIKey():
	myAPIKey = e1.get()
	print("Your API key has been saved as " + myAPIKey)
	sendQueryAndPrintResponse(myAPIKey)
	
def sendQueryAndPrintResponse(APIKey):
	response = requests.get("http://api.champion.gg/v2/champions?&api_key=" + APIKey)
	content = response.content
	#print(content)
	jcontent = json.loads(content.decode('utf8'))
	
def generateClusters():
	X = np.array([[1, 2], [1, 4], [1, 0],
			[4, 2], [4, 4], [4, 0]])
	#TODO: Change number of clusters to be equal to the value of the slider on the gui			
	kmeans = KMeans(n_cluster=2, random_state=0).fit(X)
	kmeans.labels_
	kmeans.predict([[0, 0], [4, 4]])
	kmeans.cluster_centers_


def updateNumClusters(val):
	numClusters = val
	print(numClusters)
	
master = Tk()
master.resizable(False,False)
Label(master, text="Your API Key: ").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)
b = Button(master, text="Get Data", command = saveAPIKey)
b.grid(row=0, column=3)

imgUrlAatrox = "ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Aatrox.png"
#imagebytAatrox = urllib.urlopen(imgUrlAatrox).read()
with urllib.request.urlopen("http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Aatrox.png") as url:
	imagebytAatrox = url.read()
imageb64Aatrox = base64.encodestring(imagebytAatrox)
photo = PhotoImage(data=imageb64Aatrox)
cv = Canvas(bg='white')
cv.create_image(10, 10, image = photo, anchor='nw')
cv.grid(row=3)

numClusters = 0
clusterSlider = Scale(master, label="# of Clusters:", from_= 2, to = 20, orient=HORIZONTAL, activebackground="yellow", command=updateNumClusters).grid(row=2,column=0)
mainloop( )

