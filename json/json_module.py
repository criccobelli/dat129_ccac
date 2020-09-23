# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:52:19 2020

@author: chelr
"""

import json


with open ('capitalprojects.geojson', 'r') as projects:
    projects_json = json.load(projects)

#first line accesses the list of dictionaries after "features:"
for project in projects_json['features']:
    
    #nested loop accesses each dictionary after "properties"
    for x in project['properties'].items():
        print("***Project Profile***")
        
        #access and print the key:value for the properties' dictionaries
        for key, value in project['properties'].items():
            print(key + ':', value)
            
        #adds a space in between each project for better appearance    
        print("")