#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:59:03 2017

@author: roy
"""

import json


def clean_tweets_data(file_path):
    #load in original json file
    sample_cleaned = {}
    with  open(file_path) as json_data:
    #json_file = [json_file
        d = json.load(json_data)    
        print (d)
    
    # for every key(venue), collect what we need
    '''
    for id in sample.keys():
        print id
    
    return sample_cleaned
    '''

file_path = 'london_users_data.json'    
cleaned_data = clean_tweets_data(file_path)
#saveJsonFile(cleaned_data, 'cleaned_ams_venues_data.json')


print "Finished process"