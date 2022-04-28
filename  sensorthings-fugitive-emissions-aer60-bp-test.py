import requests

def things_name_checker(name):
    # Properties Checker
    # This function checks if the name of the reporting facility (Thing) is a valid AER facility ID.
    # The definition of facility ID in AER 60: As defined in Directive 047, a unique facility identification code, 
    # with 4 letters and 7 numbers (e.g., ABWP1234567), assigned by Petrinex to each facility.
    
    # Inputs: 
    #   1. name: Reporting facility's name which is a facility ID.
    # Outputs: 
    #   Comment on validation or rejection of the facility ID.
    
    # Check if the facility ID consists of or uses both letters and numerals.
    if not name.isalnum():
        print('Facility ID name is not valid. A proper facility ID (Thing) contains 4 letters and 7 numbers.')
    
    name1 = name[0:4]
    name2 = name[4:]
    
    # Check if the first four letters of the facility ID are alphabetical.
    if not name1.isalpha():
        print('The first four letters must be alphabetical.')
    
    # Check if the last seven letters of the facility ID are numerical.
    if not name2.isnumeric():
        print('The last seven letters must be numerical.')

    # Check if facility ID is valid
    if name1.isalpha() and name2.isnumeric():
        print(f"{name} as a thing's name is a valid AER facility ID.")

def datastream_checker(name, ds_number):
    # Relation and property checker
    # This function first checks if the reporting facility (Thing) has at least three or more datastreams.
    # If yes, it will check the names of the datastreams, which shall be:
    # 1. Fugitive Emissions Volume (m3)
    # 2. Fugitive Emissions Mass Methane (kg)
    # 3. Number of identified sources of fugitive emissions
    
    # Inputs: 
    #   1. name: Reporting facility's name which is a facility ID.
    #   2. ds_number: Number of existing datastreams of reporting facility
    # Outputs: 
    #   Comment on number of datastreams and proper names.
    
    # list of three essential datastreams.
    essential_datastream_names = ['Fugitive Emissions Volume (m3)', 'Fugitive Emissions Mass Methane (kg)',
                                'Number of identified sources of fugitive emissions']
    
    existing_datastreams_names = []

    # Check if at least three datastreams exist.
    if ds_number < 3:
        print(f'{ds_number} datastreams detected. Reporting facility with {name} facility ID shall has at least three datastreams.')
    else:
        # Extract existing datastreams names.
        for n in range(ds_number):
            datastream_name = thing_datastreams['value'][n]['name']
            existing_datastreams_names.append(datastream_name)
        
        # Check if three essential datastreams names exist.
        if len(set(essential_datastream_names).intersection(set(existing_datastreams_names))) == 3:
            print(f'{name} facility ID has at least three separate valid Datastreams.')  

def volume_datastream_properities_checker(name, ds_number):
    # Properties Checker
    # This function checks if 'Fugitive Emissions Volume (m3)' datastream has valid properties:
    # 1. observationType 
    # 2. unitOfMeasurement

    # Inputs: 
    #   1. name: Reporting facility's name which is a facility ID.
    #   2. ds_number: Number of existing datastreams of reporting facility
    # Outputs: 
    #   Comment on if properties are valid or how to fix it if they are not correct.
    
    for n in range(ds_number):
            datastream_name = thing_datastreams['value'][n]['name']
            
            # Find a datastream with 'Fugitive Emissions Volume (m3)' name.
            if datastream_name == 'Fugitive Emissions Volume (m3)':
                datastream_property = True
                
                # Check if observationType is valid.
                if not thing_datastreams['value'][n]['observationType'] == 'http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement':
                    print("Fugitive Emissions Volume (m3) datastream Observation type shall be 'OM_Measurement'.")
                    datastream_property = False
                
                # Check if unitOfMeasurement components are valid.
                if not thing_datastreams['value'][n]['unitOfMeasurement']['name'] == 'm3':
                    print("Fugitive Emissions Volume (m3) datastream unitOfMeasurement unit shall be 'm3'.")
                    datastream_property = False
                if not thing_datastreams['value'][n]['unitOfMeasurement']['symbol'] == 'Cubic Meter':
                    print("Fugitive Emissions Volume (m3) datastream unitOfMeasurement symbol shall be 'Cubic Meter'.")
                    datastream_property = False
                if not thing_datastreams['value'][n]['unitOfMeasurement']['definition'] == 'http://qudt.org/vocab/unit/M3':
                    print("Fugitive Emissions Volume (m3) datastream unitOfMeasurement definition shall be 'http://qudt.org/vocab/unit/M3'.")
                    datastream_property = False
                
                if datastream_property:
                    print(f'Properties of Fugitive Emissions Volume (m3) datastream of {name} reporting facility is valid.')

def mass_datastream_properities_checker(name, ds_number):
    # Properties Checker
    # This function checks if 'Fugitive Emissions Mass Methane (kg)' datastream has valid properties:
    # 1. observationType 
    # 2. unitOfMeasurement

    # Inputs: 
    #   1. name: Reporting facility's name which is a facility ID.
    #   2. ds_number: Number of existing datastreams of reporting facility
    # Outputs: 
    #   Comment on if properties are valid or how to fix it if they are not correct.

    for n in range(ds_number):
            datastream_name = thing_datastreams['value'][n]['name']

            # Find a datastream with 'Fugitive Emissions Mass Methane (kg)' name.
            if datastream_name == 'Fugitive Emissions Mass Methane (kg)':
                datastream_property = True
                
                # Check if observationType is valid.
                if not thing_datastreams['value'][n]['observationType'] == 'http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement':
                    print("Fugitive Emissions Mass Methane (kg) datastream Observation type shall be 'OM_Measurement'.")
                    datastream_property = False
                
                # Check if unitOfMeasurement components are valid.
                if not thing_datastreams['value'][n]['unitOfMeasurement']['name'] == 'kg':
                    print("Fugitive Emissions Mass Methane (kg) datastream unitOfMeasurement unit shall be 'm3'.")
                    datastream_property = False
                if not thing_datastreams['value'][n]['unitOfMeasurement']['symbol'] == 'Kilogram':
                    print("Fugitive Emissions Mass Methane (kg) datastream unitOfMeasurement symbol shall be 'Kilogram'.")
                    datastream_property = False
                if not thing_datastreams['value'][n]['unitOfMeasurement']['definition'] == 'http://qudt.org/vocab/unit/KiloGM':
                    print("Fugitive Emissions Mass Methane (kg) datastream unitOfMeasurement definition shall be 'http://qudt.org/vocab/unit/KiloGM'.")
                    datastream_property = False
                
                if datastream_property:
                    print(f'Properties of Fugitive Emissions Mass Methane (kg) datastream of {name} reporting facility is valid.')

def number_of_fg_datastream_properities_checker(name, ds_number):
    # Properties Checker
    # This function checks if 'Number of identified sources of fugitive emissions' datastream has a valid property:
    # 1. observationType 

    # Inputs: 
    #   1. name: Reporting facility's name which is a facility ID.
    #   2. ds_number: Number of existing datastreams of reporting facility
    # Outputs: 
    #   Comment on if observationType is valid or how to fix it if it is not correct.

    for n in range(ds_number):
            datastream_name = thing_datastreams['value'][n]['name']

            # Find a datastream with 'Number of identified sources of fugitive emissions' name.
            if datastream_name == 'Number of identified sources of fugitive emissions':
                datastream_property = True

                # Check if observationType is valid.
                if not thing_datastreams['value'][n]['observationType'] == 'http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_CountObservation':
                    print("Number of identified sources of fugitive emissions datastream Observation type shall be 'OM_CountObservation'.")
                    datastream_property = False
                
                if datastream_property:
                    print(f'Properties of Number of identified sources of fugitive emissions datastream of {name} reporting facility is valid.')

def observed_property_properties_checker(thing_name, datastream_name, observed_property):
    # Relation and property checker
    # This function checks if datastream has a observerdProperty and if yes, observerdProperty has a valid properties:
    # 1. name
    # 2. definition
    # 3. description

    # Inputs: 
    #   1. thing_name: Reporting facility's name which is a facility ID.
    #   2. datastream_name: Datastream name of reporting facility.
    #   3. observed_property: JSON package which includes observedProperty of datastream_name. 
    # Outputs: 
    #   Comment on if observedProperty properties are valid or how to fix them if they are not correct.
    
    error_message = {'code': 404, 'type': 'error', 'message': 'Nothing found.'}
    
    # Check if observedProperty exists.
    if observed_property == error_message:
        print(f'{datastream_name} needs to have observedProperty.')
    else:
        observed_property_name = observed_property['name']
        observed_property_definition = observed_property['definition']
        observed_property_description = observed_property['description']
        observed_property_properties = True

        # Check if description is valid.
        if not observed_property_description == 'Fugitive methane emissions are the unintentional releases of methane to the atmosphere':
            print("The observedProperty description shall be 'Fugitive methane emissions are the unintentional releases of methane to the atmosphere.'")
            observed_property_properties = False
        
        # Check if definition is valid.
        if not observed_property_definition == 'http://www.opengis.net/def/integrated-methane-sensor-web/observed-properties/fugitive-methane-emissions':
            print("The observedProperty definition shall be 'http://www.opengis.net/def/integrated-methane-sensor-web/observed-properties/fugitive-methane-emissions'.")
            observed_property_properties = False
        
        # Check if name is valid.
        if not observed_property_name == 'Fugitive Methane Emissions':
            print("The observedProperty name shall be 'Fugitive Methane Emissions'." )
            observed_property_properties = False
        
        if observed_property_properties:
            print(f'Properties of observedProperty of {datastream_name} datastream of {thing_name} reporting facility is valid.')

####################################### Main #######################################
print()
print()
url = input('To validate created Things and the required classes and requirement, please insert a link of created Things,\n'
            'for instance, http://imsw.gswlab.ca:8080/FROST-Server/v1.1/Things:\n\n')
url_Datastreams = url.replace("Things", "Datastreams")
req_things = requests.get(url)
things = req_things.json()

# Check the Reporting facility (Thing) has a valid facility ID name.
print()
print('Check if the reporting facilities (Things) have a valid AER facility ID.')
print('--------------------------------------------------------------------------------------------')
print()

for n in range(len(things['value'])): 
    thing = things['value'][n]
    things_name_checker(thing['name'])

# Check the Reporting facility (Thing) has three valid Datastreams.
print()
print('Check if the reporting facilities (Things) have at least three datastreams.')
print('--------------------------------------------------------------------------------------------')
print()

for n in range(len(things['value'])): 
    thing = things['value'][n]
    thing_id = things['value'][n]['@iot.id']
    req_thing_datastreams = requests.get(url + '(' + str(thing_id) + ')/Datastreams')
    thing_datastreams = req_thing_datastreams.json()
    number_datastream = len(thing_datastreams['value'])
    datastream_checker(thing['name'], number_datastream)

# Check 3 Datastreams of the Reporting facility (Thing) has valid properties.
print()
print('Check if each of the reporting facility (Thing) datastreams have valid properties.')
print('--------------------------------------------------------------------------------------------')
print()

for n in range(len(things['value'])): 
    thing = things['value'][n]
    thing_id = things['value'][n]['@iot.id']
    req_thing_datastreams = requests.get(url + '(' + str(thing_id) + ')/Datastreams')
    thing_datastreams = req_thing_datastreams.json()
    number_datastream = len(thing_datastreams['value'])
    volume_datastream_properities_checker(thing['name'], number_datastream)
    mass_datastream_properities_checker(thing['name'], number_datastream)
    number_of_fg_datastream_properities_checker(thing['name'], number_datastream)
    print()

    # Check observedProperty of Datastreams has valid properties.
print()
print('Check each datastream has a observedProperty and if properties of this observedProperty are valid.')
print('--------------------------------------------------------------------------------------------')
print()

for n in range(len(things['value'])): 
    thing = things['value'][n]
    thing_id = things['value'][n]['@iot.id']
    req_thing_datastreams = requests.get(url + '(' + str(thing_id) + ')/Datastreams')
    thing_datastreams = req_thing_datastreams.json()
    number_datastream = len(thing_datastreams['value']) 
    
    for nu in range(number_datastream):
        datastream_id = thing_datastreams['value'][nu]['@iot.id']
        datastream_name = thing_datastreams['value'][nu]['name']
        datastream_observed_property = requests.get(url_Datastreams + '(' + str(datastream_id) + ')/ObservedProperty')
        observed_property = datastream_observed_property.json()
        observed_property_properties_checker(thing['name'], datastream_name, observed_property)
    print()