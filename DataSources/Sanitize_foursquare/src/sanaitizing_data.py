#Zohaib Creeds
from creed import *

'''For using Foursquare wraper'''
'''https://github.com/mLewisLogic/foursquare.git '''
import foursquare
import tqdm
import json as json
# Construct the client object
client = foursquare.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URL)

# Build the authorization url for your app
auth_uri = client.oauth.auth_url()

client = foursquare.Foursquare(access_token=ACCESS_TOKEN)
auth_uri = client.oauth.auth_url()


crs = open("../../../DataSources/FourCityDataset/twitter/amsterdam.txt","r")
fullJsonVenue = []
res = []



def printVenues():
	venuesArray = []
	for columns in ( raw.strip().split() for raw in crs ):  
		venuesArray.append(columns[1])
		#print columns[1] + " This "
	#print "Finished Saving Venues"
	return venuesArray


#fullJsonVenue.append(venue)
def obtainFoursquareVenue(data):

	'''Just create two venues'''
	venue = client.venues("4c1119843ce120a17b21091c")
	#venue = client.venues(data([1]))
	fullJsonVenue.append(venue)
	venue = client.venues("52b839a1498ee2a84a941e94")
	#venue  = client.venues(data[2])
	fullJsonVenue.append(venue)

	print "Star obtaining Foursquare data"
	str3 = "home";
	#print i.find(str3,0);
	for i in data:
		if(i.find(str3,0)!=-1):
			#print "Here as a home"
			print i
		else:
			#venue = client.venues(i)
			fullJsonVenue.append(1)
	return fullJsonVenue


def saveJsonFile(array):
	with open('venues_data.json','w') as outfile:
		json.dump(res,outfile)
		print "Saved complete JSON"

print "Display the data saved"


array = printVenues()
print "The last entry"
print(array[len(array)-1])
print(array[len(array)-2])
#obtainFoursquareVenue(array)

#Obtain data from each venue
res = obtainFoursquareVenue(array)
print(len(res))
print(res)
saveJsonFile(res)



