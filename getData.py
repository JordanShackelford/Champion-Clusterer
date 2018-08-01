import numpy as np
import io
import base64
import urllib.request
import requests
import json
from tkinter import *
from sklearn.cluster import KMeans
from PIL import Image, ImageTk



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
	cv.delete("all")
	for i in range(0,int(val)):
		cv.create_image(i * photos[i].width(),0, image=photos[i], anchor='nw')
		#cv.create_image(0,0,image=photos[numClusters],anchor='nw')
	cv.grid(row=3)
	
master = Tk()
master.resizable(False,False)
Label(master, text="Your API Key: ").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)
b = Button(master, text="Get Data", command = saveAPIKey)
b.grid(row=0, column=3)

imgUrls = ["http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Aatrox.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Ahri.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Akali.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Alistar.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Amumu.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Anivia.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Annie.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Ashe.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/AurelionSol.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Azir.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Bard.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Blitzcrank.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Brand.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Braum.png",]
byteImages = []
b64Images = []
photos = []

numClusters = 3

for i in range(0,len(imgUrls)):
	with urllib.request.urlopen(imgUrls[i]) as url:
		byteImages.append(url.read())
	b64Images.append(base64.encodebytes(byteImages[i]))
	photos.append(PhotoImage(data=b64Images[i]))
	photos[i] = photos[i].subsample(2,2)

cv = Canvas(bg='white',width="800",height="600")



clusterSlider = Scale(master, label="# of Clusters:", from_= 1, to = 20, orient=HORIZONTAL, activebackground="blue", command=updateNumClusters).grid(row=2,column=0)
mainloop( )

