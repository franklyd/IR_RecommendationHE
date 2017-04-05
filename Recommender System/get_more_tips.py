# -*- coding: utf-8 -*-
"""
Created on Sat Apr 01 12:01:27 2017

@author: xps
"""
import requests
import json as json
from creed import *

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
        
    venues_id_200 = [id for id in venues_id if venue_tips_count[id]>200]
    venues_id_400 = [id for id in venues_id_200 if venue_tips_count[id]>400]
    venues_id_600 = [id for id in venues_id_400 if venue_tips_count[id]>600]
    venues_id_800 = [id for id in venues_id_600 if venue_tips_count[id]>800]
    venue_ids = [venues_id_200,venues_id_400,venues_id_600,venues_id_800]
    return venue_ids
     
    
def get_more_tips(venues_id,offset):
    url_preffix = 'https://api.foursquare.com/v2/venues/'
    url_suffix = "/tips?sort=popular&limit=500&offset=%d&client_id=%s&client_secret=%s&oauth_token=1GLPU53VFSTNEMFZ2DG0CDNLXN2L4T30ACWZCA1L2MZ5ZLKX&v=20170401" %(offset,CLIENT_ID,CLIENT_SECRET)
    url = url_preffix+venues_id+url_suffix
    data = requests.get(url).text
    data = json.loads(data)
    tips = [tip['text'] for tip in data['response']['tips']['items'] if not tip.has_key('lang')]
    return tips   

def obtain_tips(venues_ids):
    venues_tips = {}
    print "Start obtaining Foursquare data..."
    offset = 200
    for ids in venues_ids:
        for id in ids:
            if offset==200:
                venues_tips[id] = get_more_tips(id,offset)
            else:
                venues_tips[id] += get_more_tips(id,offset)
        offset += 200
    return venues_tips

def saveJsonFile(dic, city):
    with open('%s_venues_more_tips_twitter.json' %city,'w') as outfile:
		json.dump(dic,outfile)
		print "Saved complete JSON"


city = 'london'
crs = open("../DataSources/FourCityDataset/twitter/%s.txt" %city,"r")
venues_ids = get_venues_id(crs)
venues_tips = obtain_tips(venues_ids)
saveJsonFile(venues_tips,city)