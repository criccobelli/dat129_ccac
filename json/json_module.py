import json

projects_json = {}

with open ("capitalprojects.geojson", "r") as projects:
    projects_json = json.load(projects)


#the below finds and prints the ID numbers of the projects with no area name
features = projects_json['features']#list     
for entry in features:
    properties = entry['properties']#dict
        
    for x, y in properties.items():
        if x == 'id':
            id_number = str(y)
            #print(id_number) 
             
    for key, value in properties.items():
        if key == 'area':
            blank_values = []
            if value == "": #check if keys are blank, add to a list?
                blank_values.append(id_number)
                print("This project is missing a value for 'area':", blank_values)
        else:
            continue