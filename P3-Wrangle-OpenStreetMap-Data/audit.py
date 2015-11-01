"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "example.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons", "Way", " Plaza", "Circle"]


expected_city = [
     'Alameda',
     'Albany',
     'Atherton',
     'Belmont',
     'Berkeley',
     'Brisbane',
     'Burlingame',
     'Castro Valley',
     'Daly City',
     'East Palo Alto',
     'El Cerrito',
     'Emeryville',
     'Foster City',
     'Fremont',
     'Greenbrae',
     'Half Moon Bay',
     'Hayward',
     'Kensington',
     'Kentfield',
     'Lafayette',
     'Marin City',
     'Menlo Park',
     'Mill Valley',
     'Montara',
     'Moraga',
     'Newark',
     'Oakland',
     'Orinda',
     'Pacifica',
     'Palo Alto',
     'Piedmont',
     'Pleasant Hill',
     'Redwood City',
     'Richmond',
     'San Bruno',
     'San Carlos',
     'San Leandro',
     'San Mateo',
     'Sausalito',
     'South San Francisco',
     'Tiburon',
     'Union City',
     'Walnut Creek',
     'san francisco']

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street",
            "st" : "Street",
            "street" :"Street",
            "Rd" : "Road",
            "Rd.": "Road",
            "Ave" : "Avenue",
            "Pl" : "Place",
            "avenue" : "Avenue",
            "Blvd" : "Boulevard",
            "Blvd." : "Boulevard",
            "Boulavard" : "Boulevard",
            "Boulvard" : "Boulevard",
            "Dr." : "Drive",
            "Dr" : "Drive",
            "Ln" : "Lane",
            "Ln." : "Lane",
            "Plz" : "Plaza",
            "parkway" : "Parkway"
            }

mapping_city = {
            "Artherton": "Atherton",
            "San Francicsco": "San Francisco",
            "San Francsico": "San Francisco",
            "San Fransisco": "San Francisco",
            "san francisco": "San Francisco"
}
def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

def audit_city_name(city_names, city_name):
    if city_name not in expected_city:
        city_names.add(city_name)

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def is_city_name(elem):
    return (elem.attrib['k'] == "addr:city")


def audit(osmfile, street_types, city_names):
    osm_file = open(osmfile, "r")

    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
                elif is_city_name(tag):
                    audit_city_name(city_names, tag.attrib['v'])


def update_name(name, mapping):

    m = street_type_re.search(name)
    if m:
        v = mapping.get(m.group())
        if v:
            old_name = name
            name = name.replace(m.group(), v)
            #print("Replaced", old_name, name)
    return name

def update_name_city(name, mapping):

    #Remove all the spaces at the end
    name = name.rstrip()

    #Remove the string after comma - In most errors, state or zip code is included in the city name.
    if ',' in name:
        old_name = name
        name, splitter, remainder = name.partition(',')
        print("Removed comma: ", old_name, name)

    #Replace name based on mapping
    v = mapping.get(name)
    if v:
        old_name = name
        name = name.replace(name, v)
        print("Replaced", old_name, name)
    return name


def test():
    street_types = defaultdict(set)
    city_names = set()
    audit(OSMFILE, street_types, city_names)
    assert len(street_types) == 3
    pprint.pprint(dict(street_types))
    pprint.pprint(city_names)
    for st_type, ways in street_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print name, "=>", better_name
            if name == "West Lexington St.":
                assert better_name == "West Lexington Street"
            if name == "Baldwin Rd.":
                assert better_name == "Baldwin Road"


if __name__ == '__main__':
    test()