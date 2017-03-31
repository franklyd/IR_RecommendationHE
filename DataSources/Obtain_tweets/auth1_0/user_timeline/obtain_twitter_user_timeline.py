# -*- coding: utf-8 -*-


from creed import *
from requests_oauthlib import OAuth1Session
import urllib 
import json as json
import time

NUMBER_OF_TWEETS = 3000;
NUMER_PROFILES = 10000;
LANGUAGE = "en" #Obtain english language

def obtainAuthenticationUrl():
    twitter = OAuth1Session(    client_key = CONSUMER_KEY,
                            client_secret = CONSUMER_SECRET,
                            resource_owner_key = ACCESS_TOKEN,
                            resource_owner_secret = ACCESS_TOKEN_SECRET )
    return twitter

def get_users_id(crs):
    users_id = [raw.strip().split()[0] for raw in crs if raw.strip().split()[0].find('home')==-1]
    users_id= set(users_id)
    return users_id



def obtainTwitterUserNameJSON(user_id):
    client = obtainAuthenticationUrl()
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?count=%s&user_id=%s' % (NUMBER_OF_TWEETS,user_id)
    user_metadata = client.get(url)
    #print user_metadata.text
    user_metadata = json.loads(user_metadata.text)
    return user_metadata

'''TODO must put TIME '''
def obtainUserProfile(users_id,city):    
    temp_users_meta = {}
    users_meta ={}
    #user_meta
    user = {}
    tweets_meta = {}
    print "Start obtaining users profile"
    for i, id in enumerate(users_id):
        print "INDEX:",i
        try:
            #Obtain first tweet
            
            user = obtainTwitterUserNameJSON(id)
            if(user[0]["text"]!=None):
                users_meta[id] = user         
                #print "Name of the User:", user[0]["text"]
                print "Length user: ", len(user)
                #users_meta[id] = user
                for tweet in range(len(user)):
                    print "j=", tweet
                    try: 
                        if(user[tweet]["lang"]=='en'):
                            print "Tweet ", user[tweet]["text"]
                            #tweets_meta[tweet] = user[tweet]
                            #print (users_meta[id][tweet])
                            users_meta[id][tweet] = user[tweet]
                        else:
                            users_meta[id][tweet] = None
                    except:
                        pass
        except:
            print "There was an error"
            #user = obtainTwitterUserNameJSON(id)
            try:
                if(user["error"] !=None):
                    print "Not authorized"
                    print (user["error"])
    
            except:
                pass
            try:
                if(user["errors"][0]["code"] == 34):
                    print (user["errors"][0]["message"])
                    #users_meta[id] = user["errors"][0]["message"]
                    #pass        
            except:
                pass
            try:
                if(user["errors"][0]["code"] == 88):
                    print (user["errors"][0]["message"])
                    time.sleep(900)
                    user = obtainTwitterUserNameJSON(id)                   
            except:
                pass
            
                try:
                        if(user[0]["text"]!=None):
                            #users_meta[id] = user         
                            #print "Name of the User:", user[0]["text"]
                            for tweet in range(len(user)):
                                if(user[tweet]["lang"]=='en'):
                                    print "Tweet ", user[tweet]["text"]
                                    users_meta[id] =  user[tweet]
                except:
                    pass
                    
                    
        if(i==NUMER_PROFILES):
            saveConstantJSON(users_meta, city)
            break
        
        #saveJsonFile(users_meta, city)
    return users_meta


def saveConstantJSON(users_meta,city):
    #a_dict = {'new_key': 'new_value'}
    
    with open('%s_users_data_3000t10000us.json' %city) as f:
        data = json.load(f)
    
    data.update(users_meta)
    
    with open('%s_users_data_3000t10000us.json' %city,'w') as f:
        json.dump(data, f)


def saveJsonFile(dic, city):
    with open('%s_users_data_3000t10000us.json' %city,'w') as outfile:
        json.dump(dic,outfile)
        #json.dumps(dic, cls=SetEncoder)
        print "Saved complete JSON"


cities = ['london','amsterdam','paris','rome']
cities = ['london']

for city in cities:
    crs = open("../../../FourCityDataset/twitter/%s.txt" %city,"r")
    users_id = get_users_id(crs)
    users_meta = obtainUserProfile(users_id,city)
    #saveJsonFile(users_meta,city)
    print "Finished program for", city



#rob = obtainTwitterUserNameJSON(40594003)    
#print rob

print "Process finished"