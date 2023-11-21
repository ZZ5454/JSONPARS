# Import the JSON module for working with JSON data
import json


#Create the data dictionary

data = {

    'name': 'John Doe',
    'age':25,
    'city':'Seattle,WA',
    'interests': ['Sports','Music','Movies'],
    'Student': True
    }

## Write the initial data to a JSON file
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)

# Print a message indicating that data has been written to data.json
print('Data has been written to data.json')


# Read data from the json file
with open('data.json',"r") as json_file:

    loaded_data = json.load(json_file)

print ("Successfully able to read data.json")
print (loaded_data)

# Modify the loaded data in the json file
loaded_data['age'] = 100
loaded_data['interests'].append('travel')

# Writing the modified data back to json
with open('data.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)

# Print a message indicating that modified data has been written to data.json
print('Modified data written to data.json')
    