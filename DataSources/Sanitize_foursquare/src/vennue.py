# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:27:50 2017

@author: xps
"""

from creed import *

'''For using Foursquare wraper'''
'''https://github.com/mLewisLogic/foursquare.git '''
import foursquare
import tqdm
import json as json
import time 
# Construct the client object
client = foursquare.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URL)

# Build the authorization url for your app
#auth_uri = client.oauth.auth_url()

#client = foursquare.Foursquare(access_token=ACCESS_TOKEN)
#auth_uri = client.oauth.auth_url()

#amsterdam_sf = gl.SFrame.read_csv('../DataSources/FourCityDataset/instagram/amsterdam.txt',
#                        delimiter=' ',header=False)
#amsterdam_sf.rename({'X1':'user_id','X2':'venue_id','X3':'#visits(normalized)'})
#venue_list  =list(amsterdam_sf['venue_id'])

def get_venues_id(crs):
    venues_id = [raw.strip().split()[1] for raw in crs if raw.strip().split()[1].find('home')==-1]
    venues_id =set(venues_id)
    return venues_id

def obainFoursquareVenue(venues_id): 
    start_time = time.time()
    venues_meta = {}
    print "Start obtaining Foursquare data..."
    for i,id in enumerate(venues_id):
        if i%100 == 0:
            print "Finished ", i
        if i==4590:
            count_time = time.time() - start_time
            if count_time < 3600:
                time.sleep(3600 - count_time)
                start_time = time.time()
        if i==9550:
            count_time = time.time() - start_time
            if count_time < 3600:
                time.sleep(3600 - count_time)   
        if i==14530:
            time.sleep(1800)
        try:
            venues_meta[id] = client.venues(id)
        except:
            time.sleep(3600)
            venues_meta[id] = client.venues(id)
    return venues_meta
    
def saveJsonFile(dic, city):
    with open('%s_venues_data.json' %city,'w') as outfile:
		json.dump(dic,outfile)
		print "Saved complete JSON"

cities = ['london','paris','rome']
cities = ['paris','rome']
for city in cities:
    crs = open("../DataSources/FourCityDataset/instagram/%s.txt" %city,"r")
    venues_id = get_venues_id(crs)
    venues_meta = obainFoursquareVenue(venues_id)
    saveJsonFile(venues_meta,city)