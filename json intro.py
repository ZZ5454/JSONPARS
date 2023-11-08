#
import json


#Create the data dictionary

data = {

    'name': 'John Doe',
    'age':25,
    'city':'Seattle,WA',
    'interests': ['Sports','Music','Movies'],
    'Student': True
    }

##
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)

print('Data has been written to data.json')



#
with open('data.json',"r") as json_file:

    loaded_data = json.load(json_file)


    