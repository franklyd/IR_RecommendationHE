#Zohaib Creeds
from creed import *

'''For using Foursquare wraper'''
'''https://github.com/mLewisLogic/foursquare.git '''
import foursquare
from tqdm import tqdm
import json as json


NUMBER_VENUES = 50;

'''Connector foursquare'''

# Construct the client object
client = foursquare.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URL)

# Build the authorization url for your app
auth_uri = client.oauth.auth_url()
client = foursquare.Foursquare(access_token=ACCESS_TOKEN)
auth_uri = client.oauth.auth_url()

'''Source of the data'''
crs = open("../../../DataSources/FourCityDataset/twitter/amsterdam.txt","r")
fullJsonVenue = {}
res = []


def printVenues():
	venuesArray = []
	for columns in ( raw.strip().split() for raw in crs ):  
		venuesArray.append(columns[1])
		
		#print columns[1] + " This "
	#print "Finished Saving Venues"
	return venuesArray


def obtainFoursquareVenue(data):

	'''Just create two venues'''
	#venue = client.venues("4c1119843ce120a17b21091c")
	dictionary = {}
	print "Delete repeated"
	data = deleteRepeated(data)
	print "Star obtaining Foursquare data"
	#Check for the word home
	str3 = "home";
	'''This for should obtain certain data'''
	for i in range(NUMBER_VENUES):
		if(data[i].find(str3,0)!=-1):
			print "Here as a home"
			#print i
			# s = 1;
		else:
			venue = client.venues(data[i])
			dictionary[data[i]] = venue;

	return dictionary

def obtainFoursquareVenueTips(data):

	'''Just create two venues'''
	#venue = client.venues("4c1119843ce120a17b21091c")
	dictionary = {}
	print "Delete repeated"
	data = deleteRepeated(data)
	print "Star obtaining Foursquare data"
	#Check for the word home
	str3 = "home";
	'''This for should obtain certain data'''
	for i in range(NUMBER_VENUES):
		if(data[i].find(str3,0)!=-1):
			print "Here as a home"
			#print i
			# s = 1;
		else:
			venue = client.venues.tips(data[i])
			dictionary[data[i]] = venue;

	return dictionary


def saveJsonFile(array):
	with open('venues_amsterdam.json','w') as outfile:
		json.dump(res,outfile)
		print "Saved  JSON venues"

def saveJsonTips(array): 
	with open('venues_tips_amsterdam.json','w') as outfile:
		json.dump(res,outfile)
		print "Saved  JSON venue's tips"

def deleteRepeated(venue) :
	newVenue = list(set(venue))
	#print len(newVenue)
	return newVenue



print "**Display the data saved**"

listVenues = printVenues()
print "**The last entry**"
print(listVenues[len(listVenues)-1])
print(listVenues[len(listVenues)-2])


print "**Venues before procesed: ", len(listVenues)
listVenues =  deleteRepeated(listVenues)
print "**After process size:", len(listVenues)

'''Obtain data for each venue'''
'''
res = obtainFoursquareVenue(listVenues)
#print res
print "**Length venues  before saving: " , (len(res))
saveJsonFile(res)
'''

print "**Obtain the tips from venues**"
res = obtainFoursquareVenueTips(listVenues)
print "**Length venues Tips  before saving: " , (len(res))
#Example for obtaining the review or text. First review from venue 4a6da31ff964a520d1d21fe3
print "Text:" , res["4a6da31ff964a520d1d21fe3"]["tips"]["items"][1]["text"]
saveJsonTips(res)

