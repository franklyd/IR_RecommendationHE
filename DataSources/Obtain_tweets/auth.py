

from creed import *
import twitter
import json as json

api = twitter.Api(consumer_key= CONSUMER_KEY,
                      consumer_secret= CONSUMER_SECRET,
                      access_token_key= ACCESS_TOKEN,
                      access_token_secret=ACCESS_TOKEN_SECRET)


#print(api.VerifyCredentials())

#statuses = api.GetUserTimeline(screen_name="bobb_robinson")
#print([s.text for s in statuses])
#print statuses


#print api.GetHomeTimeline()
#users = api.GetFriends()
#print users




def get_users_id(crs):
    users_id = [raw.strip().split()[0] for raw in crs if raw.strip().split()[0].find('home')==-1]
    users_id= set(users_id)
    return users_id

def obtainTwitterUserTimeline(users_id):
    users_meta = {}
    print "Start obtaining Tweets from users"
    statuses = api.GetUserTimeline(screen_name="bobb_robinson",count =30)
    print type(statuses)
    print statuses[0]
    
    try: 
        users_meta["bobb"] = statuses[1]
    except:
        pass
    
    #users_meta["bobb"] = statuses(1)
    return users_meta

def saveJsonFile(dic, city):
    with open('%s_users_data.json' %city,'w') as outfile:
		#json.dump(dic,outfile)
        json.dumps(dic, cls=SetEncoder)
        print "Saved complete JSON"


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
       if isinstance(obj, set):
           return list(obj)
       return json.JSONEncoder.default(self, obj) 

def obtainUsernam(user_id):
    username = api.GetUserTimeline(screen_name)
    
    
    return username


cities = ['amsterdam']

for city in cities:
    crs = open("../FourCityDataset/twitter/%s.txt" %city,"r")
    users_id = get_users_id(crs)
    users_meta = obtainTwitterUserTimeline(users_id)
    saveJsonFile(users_meta,city)
    print "Finished program for", city
    

#print users_id

