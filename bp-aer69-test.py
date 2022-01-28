import requests

def things_name_checker(name):
    # This function checks if the name of the things is a valid AER facility ID
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
    return print(f"{name} as a thing's name has a valid AER facility ID.")

def datastream_checker(name, ds_number):
    # This function checks if the Report facility (Thing) has at least three separate Datastreams which are 
    # 1. Fugitive Emissions Volume (m3)
    # 2. Fugitive Emissions Mass Methane (kg)
    # 3. Number of identified sources of fugitive emissions

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

def volume_datastream_properities_checker(name, ds_number):
    # This function checks if Fugitive Emissions Volume (m3) datastream has a valid properties.
    # Testing observationType and unitOfMeasurement

    Datastream_name_Volume = "Fugitive Emissions Volume (m3)"
    for n in range(ds_number):
            datastream_name = thing_datastreams['value'][n]['name']
            if datastream_name == Datastream_name_Volume:
                
                # Check observationType
                if not thing_datastreams['value'][n]['observationType'] == "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement":
                    return print("Fugitive Emissions Volume (m3) datastream Observation type shall be 'OM_Measurement'.")
                
                # Check unitOfMeasurement
                if not thing_datastreams['value'][n]['unitOfMeasurement']['name'] == "m3":
                    return print("Fugitive Emissions Volume (m3) datastream unitOfMeasurement unit shall be 'm3'.")
                if not thing_datastreams['value'][n]['unitOfMeasurement']['symbol'] == "Cubic Meter":
                    return print("Fugitive Emissions Volume (m3) datastream unitOfMeasurement symbol shall be 'Cubic Meter'.")
                if not thing_datastreams['value'][n]['unitOfMeasurement']['definition'] == "http://qudt.org/vocab/unit/M3":
                    return print("Fugitive Emissions Volume (m3) datastream unitOfMeasurement definition shall be 'http://qudt.org/vocab/unit/M3'.")
            
            return print(f'Fugitive Emissions Volume datastream properties of {name} facility ID is valid as defined.')

def mass_datastream_properities_checker(name, ds_number):
    # This function checks if Fugitive Emissions Mass Methane (kg) datastream has a valid properties.
    # Testing observationType and unitOfMeasurement

    Datastream_name_Volume = "Fugitive Emissions Mass Methane (kg)"
    for n in range(ds_number):
            datastream_name = thing_datastreams['value'][n]['name']
            if datastream_name == Datastream_name_Volume:
                
                # Check observationType
                if not thing_datastreams['value'][n]['observationType'] == "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement":
                    return print("Fugitive Emissions Mass Methane (kg) datastream Observation type shall be 'OM_Measurement'.")
                
                # Check unitOfMeasurement
                if not thing_datastreams['value'][n]['unitOfMeasurement']['name'] == "kg":
                    return print("Fugitive Emissions Mass Methane (kg) datastream unitOfMeasurement unit shall be 'm3'.")
                if not thing_datastreams['value'][n]['unitOfMeasurement']['symbol'] == "Kilogram":
                    return print("Fugitive Emissions Mass Methane (kg) datastream unitOfMeasurement symbol shall be 'Kilogram'.")
                if not thing_datastreams['value'][n]['unitOfMeasurement']['definition'] == "http://qudt.org/vocab/unit/KiloGM":
                    return print("Fugitive Emissions Mass Methane (kg) datastream unitOfMeasurement definition shall be 'http://qudt.org/vocab/unit/KiloGM'.")
            
            return print(f'Fugitive Emissions Mass Methane (kg) datastream properties of {name} facility ID is valid as defined.')

def number_of_fg_datastream_properities_checker(name, ds_number):
    # This function checks if Number of identified sources of fugitive emissions datastream has a valid properties.
    # Testing observationType

    Datastream_name_Volume = "Number of identified sources of fugitive emissions"
    for n in range(ds_number):
            datastream_name = thing_datastreams['value'][n]['name']
            if datastream_name == Datastream_name_Volume:
                
                # Check observationType
                if not thing_datastreams['value'][n]['observationType'] == "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_CountObservation":
                    return print("Number of identified sources of fugitive emissions datastream Observation type shall be 'OM_CountObservation'.")

            return print(f'Number of identified sources of fugitive emissions datastream properties of {name} facility ID is valid as defined.')



req_things = requests.get('http://imsw.gswlab.ca:8080/FROST-Server/v1.1/Things')
things = req_things.json()

# Check the Reporting facility (Thing) has a valid facility ID name.

for n in range(len(things['value'])): 
    thing = things['value'][n]
    things_name_checker(thing['name'])

print()

# Check the Reporting facility (Thing) has at least three valid Datastreams.
for n in range(len(things['value'])): 
    thing = things['value'][n]
    thing_id = things['value'][n]['@iot.id']
    req_thing_datastreams = requests.get('http://imsw.gswlab.ca:8080/FROST-Server/v1.1/Things('+str(thing_id)+')/Datastreams')
    thing_datastreams = req_thing_datastreams.json()
    number_datastream = len(thing_datastreams['value'])
    datastream_checker(thing['name'], number_datastream)
    
print()

# Check 3 valid Datastreams of the Reporting facility (Thing) has valid properties.

for n in range(len(things['value'])): 
    thing = things['value'][n]
    thing_id = things['value'][n]['@iot.id']
    req_thing_datastreams = requests.get('http://imsw.gswlab.ca:8080/FROST-Server/v1.1/Things('+str(thing_id)+')/Datastreams')
    thing_datastreams = req_thing_datastreams.json()
    number_datastream = len(thing_datastreams['value'])
    volume_datastream_properities_checker(thing['name'], number_datastream)
    mass_datastream_properities_checker(thing['name'], number_datastream)
    number_of_fg_datastream_properities_checker(thing['name'], number_datastream)
    print()