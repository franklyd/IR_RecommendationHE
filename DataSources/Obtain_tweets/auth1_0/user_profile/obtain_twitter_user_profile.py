# -*- coding: utf-8 -*-


from creed import *
from requests_oauthlib import OAuth1Session
import urllib 
import json as json
import time
import tqdm

NUMER_PROFILES = 10;

def get_users_id(crs):
    users_id = [raw.strip().split()[0] for raw in crs if raw.strip().split()[0].find('home')==-1]
    users_id= set(users_id)
    return users_id





def obtainAuthenticationUrl():
    twitter = OAuth1Session(    client_key = CONSUMER_KEY,
                            client_secret = CONSUMER_SECRET,
                            resource_owner_key = ACCESS_TOKEN,
                            resource_owner_secret = ACCESS_TOKEN_SECRET )
    #url = 'https://api.twitter.com/1.1/users/lookup.json?user_id=5976'
    #result = twitter.get(url)
    return twitter

def obtainTwitterUserNameJSON(user_id):
    client = obtainAuthenticationUrl()
    url = 'https://api.twitter.com/1.1/users/lookup.json?user_id=%s' % user_id
    user_metadata = client.get(url)
    #print user_metadata.text
    user_metadata = json.loads(user_metadata.text)
    return user_metadata

'''TODO must put the '''
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
                         
        if(i==NUMER_PROFILES):
            saveConstantJSON(users_meta, city)
            break
        saveConstantJSON(users_meta, city)
    return users_meta


def saveConstantJSON(users_meta,city):
    #a_dict = {'new_key': 'new_value'}
    
    with open('%s_users_data.json' %city) as f:
        data = json.load(f)
    
    data.update(users_meta)
    
    with open('%s_users_data.json' %city,'w') as f:
        json.dump(data, f)
        

def saveJsonFile(dic, city):
    with open('%s_users_data.json' %city,'w') as outfile:
        #feeds ={}
        #feeds.append(dic)
        json.dump(dic,outfile)
        #json.dumps(dic, cls=SetEncoder)
        print "Saved complete JSON"
    outfile.close()

#cities = ['london','amsterdam','paris','rome']
cities = ['london']

for city in cities:
    crs = open("../../../FourCityDataset/twitter/%s.txt" %city,"r")
    users_id = get_users_id(crs)
    print "Size of the users first: ", len(users_id)
    print type(users_id)
    users_meta = obtainUserProfile(users_id, city)
    #saveJsonFile(users_meta,city)
    print "Finished program for", city
    



print "Process finished"