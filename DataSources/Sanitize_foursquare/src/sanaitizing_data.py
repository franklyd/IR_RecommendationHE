#Zohaib Creeds
from creed import *

'''For using Foursquare wraper'''
'''https://github.com/mLewisLogic/foursquare.git '''
import foursquare
from tqdm import tqdm
import json as json
import urllib2
import time

NUMBER_VENUES_REQUEST = 498;
INDEX_INIT_VENUES = 0;
INDEX_FINAL_VENUES = 498;
DELAY_TIME = 3720; # 1hr2min
ERROR_VENUE = "4daf17ee93a0096fbaae0d6f"
'''Connector foursquare'''

# Construct the client object
client = foursquare.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URL)

# Build the authorization url for your app
auth_uri = client.oauth.auth_url()
client = foursquare.Foursquare(access_token=ACCESS_TOKEN)
auth_uri = client.oauth.auth_url()

'''Source of the data'''
crs = open("../../../DataSources/FourCityDataset/twitter/amsterdam.txt","r")
''' Delted Venues found '''
crs_deleted = open("deletedVenues.txt","r")

fullJsonVenue = {}
res = []




def obtainVenues(crs):
	venuesArray = []
	for columns in ( raw.strip().split() for raw in crs ):
		venuesArray.append(columns[1])
	return venuesArray

def obtainDeletedVenues(crs):
	venuesArray = []
	for columns in ( raw.strip().split() for raw in crs ):
		venuesArray.append(columns[0])
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
	for i in tqdm(range(0,len(data))):
		##Check for the "home" characters
		if(data[i].find(str3,0)==-1):
			if(isDeleted(data[i])!= True):
				venue = client.venues.tips(data[i])
				#venue = obtainVenueTips(ERROR_VENUE)
				dictionary[data[i]] = venue;
				if((i+1) % NUMBER_VENUES_REQUEST==0):
					time.sleep(DELAY_TIME)

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

def obtainVenueTips(venue_id):
	try:
		print "Obtaing venue tips"
		venue = client.venues.tips(venue_id)
	except urllib2.HTTPError as err:
		if err.code == 404:
			print "There is a 404. No elment found"
			return 0
		else:
			return venue
			print "Error"

def isDeleted(venue_id):
	#deleted_venues file
	for i in deleted_venues:
		if(i == venue_id):
			return True
		else:
			return False


'''*** Main ***'''

if __name__ == '__main__':
	print "**Display the data saved**"
	#Call all the files that are deleted
	deleted_venues = obtainDeletedVenues(crs_deleted)


	listVenues = obtainVenues(crs)
	print "**The last entry**"
	print(listVenues[len(listVenues)-1])
	print(listVenues[len(listVenues)-2])

	print "**Venues size: ", len(listVenues)
	listVenues =  deleteRepeated(listVenues)
	print "**After repeated VENUES deleted size:", len(listVenues)


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
	saveJsonTips(res)
	
	print "****JSON Tips Saved****"
	#Example for obtaining the review or text. First review from venue 4a6da31ff964a520d1d21fe3
	#print "Text:" , res["4a6da31ff964a520d1d21fe3"]["tips"]["items"][1]["text"]
	
	print deleted_venues
	print isDeleted("4daf17ee93a0096fbaae0d6f")
	