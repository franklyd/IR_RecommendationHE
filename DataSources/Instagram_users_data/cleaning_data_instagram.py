# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 20:49:58 2017

@author: Yadong
"""

import json

NUMBER_TIPS = 3;


def clean_data(file_path):
    #load in original json file
    sample_cleaned = {}
    json_file = open(file_path)
    sample = json.load(json_file)
    # for every key(venue), collect what we need
    for id in sample.keys():
        info = sample[id]['venue']
        sample_cleaned[id] = {}
        sample_cleaned[id]['name'] = info['name']
        try:
            sample_cleaned[id]['category'] = info['categories'][0]['shortName']
        except:
            sample_cleaned[id]['category'] = None
            
        try:    
            sample_cleaned[id]['description'] = info['description']
        except:
            sample_cleaned[id]['description'] = None
        try:
            sample_cleaned[id]['likes'] = info['likes']['count']
        except:
            sample_cleaned[id]['likes'] = None
            
        sample_cleaned[id]['country'] = info['location']['cc']
        try:
            sample_cleaned[id]['city'] = info['location']['city']
        except:
            sample_cleaned[id]['city'] = None
        
        try:    
            sample_cleaned[id]['rating'] = info['rating']
        except:
            sample_cleaned[id]['rating'] = None
        
        try:
            sample_cleaned[id]['photo'] = [info['BestPhoto']['prefix']+'800x600'+info['BestPhoto']['suffix']]
        except:
            sample_cleaned[id]['photo'] = []
        try:
            info_photo = info['photos']['groups'][0]['items'][0]
            sample_cleaned[id]['photo'].append(info_photo['prefix']+'800x600'+info_photo['suffix'])
            
        except:
            pass
        
        sample_cleaned[id]['checkins'] = info['stats']['checkinsCount']
        sample_cleaned[id]['tags'] = info['tags']
        try:
            sample_cleaned[id]['tips'] = []
            for tip in info['tips']['groups'][0]['items']:
                if tip['lang'] == 'en':
                    sample_cleaned[id]['tips'].append(tip['text'])
                #sample_cleaned[id]['tips'][tip]['language'] = 
                
                if len(sample_cleaned[id]['tips']) == NUMBER_TIPS:
                   break
                    
        except:
            sample_cleaned[id]['tips'] = None
    
        try:
            if
                
                
    return sample_cleaned
    
def saveJsonFile(dic, file_name):
    with open(file_name,'w') as outfile:
		json.dump(dic,outfile)
		print "Saved complete JSON", file_name

https://api.foursquare.com/v2/tips/49f083e770c603bbe81f8eb4
#cities = ['london','amsterdam','paris','rome']
cities = ['london']

for city in cities:

    file_path = "./%s_venues_data.json" % (city,)   
    cleaned_data = clean_data(file_path)
    saveJsonFile(cleaned_data, '../cleaned_data/%s/cleaned_%s_venues_instagram_dataEN3Tips.json'%(city,city))
    
print "Finished program"







































