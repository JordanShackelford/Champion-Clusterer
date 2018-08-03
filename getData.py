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
	cv.delete("all") #clear the canvas
	counter = 0
	for i in range(0,14):
		for j in range(0,10):
			if counter < int(val):
				cv.create_image(i * photos[i].width(),j*photos[0].height(), image=photos[counter], anchor='nw')
				counter += 1
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
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Braum.png",

			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Caitlyn.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Camille.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Cassiopeia.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Chogath.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Corki.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Darius.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Diana.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/DrMundo.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Draven.png"]
'''
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Ekko.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Elise.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Evelynn.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Ezreal.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Fiddlesticks.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Fiora.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Fizz.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Galio.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Gangplank.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Garen.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Gnar.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Gragas.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Graves.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Hecarim.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Heimerdinger.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Illaoi.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Irelia.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Ivern.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Janna.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/JarvanIV.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Jax.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Jayce.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Jhin.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Jinx.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Kai'sa.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Kalista",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Karma.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Karthus.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Kassadin.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Katarina.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Kayle.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Kayn.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Kennen.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Khazix.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Kindred.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Kled.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/KogMaw.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/LeBlanc.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/LeeSin.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Leona.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Lissandra.png",
			"http://ddragon.leagueoflegends.com/cdn/8.14.1/img/champion/Lucian.png"
			'''
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

