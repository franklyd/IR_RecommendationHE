# -*- coding: utf-8 -*-


from creed import *
from requests_oauthlib import OAuth1Session
import urllib 
import json as json
import time
import tqdm

NUMER_PROFILES = 300;

'''Obtain access to the Twitter API'''
def obtainAuthenticationUrl():
    twitter = OAuth1Session(    client_key = CONSUMER_KEY,
                            client_secret = CONSUMER_SECRET,
                            resource_owner_key = ACCESS_TOKEN,
                            resource_owner_secret = ACCESS_TOKEN_SECRET )
    #url = 'https://api.twitter.com/1.1/users/lookup.json?user_id=5976'
    #result = twitter.get(url)
    return twitter

'''Get the users ids from the .txt file given by @jyang. '''
def get_users_id(crs):
    users_id = [raw.strip().split()[0] for raw in crs if raw.strip().split()[0].find('home')==-1]
    #Delete the repeated users
    users_id= set(users_id)
    print "User list size", len(users_id)
    return users_id

'''Create the HTTP Requst to Twitter API'''
def obtainTwitterUserNameJSON(user_id):
    client = obtainAuthenticationUrl()
    url = 'https://api.twitter.com/1.1/users/lookup.json?user_id=%s' % user_id
    user_metadata = client.get(url)
    user_metadata = json.loads(user_metadata.text)
    return user_metadata

'''Obtain the user profile from twitter'''
def obtainUserProfile(users_id,city):    
    users_meta = {}
    print "Start obtaining users profile"
    for i, id in enumerate(users_id):
        print "INDEX:",i
        try:
            user = obtainTwitterUserNameJSON(id)
            if(user[0]["screen_name"]!=None):
                users_meta[id] = user
                print "Name of the User:", user[0]["screen_name"]
        except:
            print "There was an error"
            #user = obtainTwitterUserNameJSON(id)
            if(user["errors"][0]["code"] == 17):
                print (user["errors"][0]["message"])
                #users_meta[id] = user["errors"][0]["message"]       
            
            if(user["errors"][0]["code"] == 88):
                print (user["errors"][0]["message"])
                time.sleep(900)
                user = obtainTwitterUserNameJSON(id)
                if(user[0]["screen_name"]!=None):
                    users_meta[id] = obtainTwitterUserNameJSON(id)
                    print "Name of the User:", user[0]["screen_name"]
                         
        #if(i==NUMER_PROFILES):
         #   saveConstantJSON(users_meta, city)
          #  break
        saveConstantJSON(users_meta, city)
    return users_meta


def saveConstantJSON(users_meta,city):
    with open('%s_twitter_users_profile_Allus.json' %city) as f:
        data = json.load(f)    
        data.update(users_meta)    
   
    with open('%s_twitter_users_profile_Allus.json' %city,'w') as f:
        json.dump(data, f)
        
def saveJsonFile(dic, city):
    with open('%s_twitter_users_profile_Allus.json' %city,'w') as outfile:
        json.dump(dic,outfile)
        print "Saved complete JSON"
    outfile.close()

#cities = ['london','amsterdam','paris','rome']
'''Just iterate in the city of London'''
cities = ['london']

for city in cities:
    crs = open("../../../FourCityDataset/twitter/%s.txt" %city,"r")
    users_id = get_users_id(crs)
    print "Size of the users first: ", len(users_id)
    print type(users_id)
    users_meta = obtainUserProfile(users_id, city)
    #saveJsonFile(users_meta,city)
    print "Finished program for", city
    

print "Process for obtainin profile finished finished"