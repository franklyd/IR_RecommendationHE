# -*- coding: utf-8 -*-

import json
import glob
import tqdm



def saveJsonFile(dic, file_name):
    with open(file_name,'w') as outfile:
		json.dump(dic,outfile)
		print "Saved complete JSON", file_name

result = []
for f in glob.glob("*.json"):
    with open(f, "rb") as infile:
        result.append(json.load(infile))
        #result[f]=json.load(infile) 	
        print "Working on file", f

with open("cleaned_london_venues_file.json", "w") as outfile:
     json.dump(result, outfile)
     
## TODO: The venues must not repeat     
     
     
     

