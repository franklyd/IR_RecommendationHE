# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 22:45:32 2017

@author: xps
"""

from creed import *

'''For using Foursquare wraper'''
'''https://github.com/mLewisLogic/foursquare.git '''
import foursquare
import tqdm
import json as json
import time 
import requests

#client_id=CLIENT_ID
#client_secret=CLIENT_SECRET

def get_venues_id(crs):
    venues_id = [raw.strip().split()[1] for raw in crs if raw.strip().split()[1].find('home')==-1]
    venues_id = set(venues_id)
    venues_id = list(venues_id)
    # count tips for venue
    file_path = './london_venues_data_twitter.json'
    json_file = open(file_path)
    jsonObj = json.load(json_file)    
    venue_tips_count = {}
    for id in jsonObj.keys():
        venue = jsonObj[id]['venue']
        venue_tips_count[id] = venue['tips']['count']
        
    venues_id = [id for id in venues_id if venue_tips_count[id]>20]
    return venues_id
    
def get_tips(venues_id):
    url_preffix = 'https://api.foursquare.com/v2/venues/'
    url_suffix = "/tips?sort=popular&limit=500&offset=0&client_id=%s&client_secret=%s&oauth_token=1GLPU53VFSTNEMFZ2DG0CDNLXN2L4T30ACWZCA1L2MZ5ZLKX&v=20170401" %(CLIENT_ID,CLIENT_SECRET)
    url = url_preffix+venues_id+url_suffix
    data = requests.get(url).text
    data = json.loads(data)
    return data      
    
def obainFoursquareVenueTips(venues_id): 
    start_time = time.time()
    venues_tips = {}
    print "Start obtaining Foursquare data..."
    for i,id in enumerate(venues_id):
        if i%10 == 0:
            print "Finished ", i
        if (i+1)%500 == 0:
            count_time = time.time() - start_time
            if count_time < 3600:
                time.sleep(3600 - count_time)
                start_time = time.time()
        try:
            venues_tips[id] = get_tips(id)
        except:
            time.sleep(3600)
            venues_tips[id] = get_tips(id)
    return venues_tips
    
def saveJsonFile(dic, city):
    with open('%s_venues_tips_twitter.json' %city,'w') as outfile:
		json.dump(dic,outfile)
		print "Saved complete JSON"

cities = ['london']
##cities = ['paris','rome']
venues_id = None
for city in cities:
    crs = open("../DataSources/FourCityDataset/twitter/%s.txt" %city,"r")
    venues_id = get_venues_id(crs)
    venues_tips = obainFoursquareVenueTips(venues_id)
    saveJsonFile(venues_tips,city)
