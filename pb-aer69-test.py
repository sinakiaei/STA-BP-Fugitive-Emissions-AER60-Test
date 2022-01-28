import re
import requests

def things_name_checker(name):
    # This function will check if the name of the things is a valid AER facility ID
    # The definition of facility ID in AER 60:
    # As defined in Directive 047, a unique facility identification code, with 4 letters and
    # 7 numbers (e.g., ABWP1234567), assigned by Petrinex to each facility. 
    if not name.isalnum():
        return print("A proper facility ID contains 4 letters and 7 numbers")
    name1 = name[0:4]
    name2 = name[4:]
    if not name1.isalpha():
        return print("The first four letters must be alphabetical.")
    if not name2.isnumeric():
        return print("The last seven letters must be numerical.")
    return print(f"{name} as a thing's name is a valid AER facility ID.")

def datastream_checker(name, ds_number):
    # This function checks if the Report facility (Thing) has at least three separate Datastreams
    
    Datastream_names = ["Fugitive Emissions Volume (m3)", "Fugitive Emissions Mass Methane (kg)",
                        "Number of identified sources of fugitive emissions"]
    datastream_list = []
    
    if ds_number < 3:
        return print(f'{name} facility ID shall have at least three Datastreams.')
    elif ds_number >=3:
        for n in range(ds_number):
            datastream_name = thing_datastreams['value'][n]['name']
            if not datastream_name in Datastream_names: # Need improvement
                return print("Not a valid datastream name")
    return print(f'{name} facility ID has at least three separate valid Datastreams.')

# def datastream_properities_checker()

    



req_things = requests.get('http://imsw.gswlab.ca:8080/FROST-Server/v1.1/Things')
things = req_things.json()

# Check the Reporting facility (Thing) has a valid facility ID name.

for n in range(len(things['value'])): 
    thing = things['value'][n]
    things_name_checker(thing['name'])

# Check the Reporting facility (Thing) has at least three valid Datastreams.

for n in range(len(things['value'])): 
    thing_id = things['value'][n]['@iot.id']
    req_thing_datastreams = requests.get('http://imsw.gswlab.ca:8080/FROST-Server/v1.1/Things('+str(thing_id)+')/Datastreams')
    thing_datastreams = req_thing_datastreams.json()
    number_datastream = len(thing_datastreams['value'])
    datastream_checker(thing['name'], number_datastream)
