# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 20:49:58 2017

@author: Yadong
"""

import json

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
            for tip in info['tips']['group s'][0]['items']:
                if tip['lang'] == 'en':
                    sample_cleaned[id]['tips'].append(tip['text'])
                if len(sample_cleaned[id]['tips']) ==3:
                    break
                    
        except:
            sample_cleaned[id]['tips'] = None
    
    return sample_cleaned
    
def saveJsonFile(dic, file_name):
    with open(file_name,'w') as outfile:
		json.dump(dic,outfile)
		print "Saved complete JSON"

file_path = './ams_venues_data.json'    
cleaned_data = clean_data(file_path)
saveJsonFile(cleaned_data, 'cleaned_ams_venues_data.json')
