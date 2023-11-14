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

print ("Successfully able to read data.json")
print (loaded_data)

#
loaded_data['age'] = 100
loaded_data['interests'].append('travel')

# Writing the modified data back to json
with open('data.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)

print('Modified data written to data.json')
    