#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mapparser
import pprint
import tags
import audit
import data
from collections import defaultdict
def main():
    filename = 'san-francisco.osm'
    #filename = 'sf-sampler.osm'
    #print("\n*** Check the number of tags ***")
    #taglist = mapparser.count_tags(filename)
    #pprint.pprint(taglist)

    #print("\n*** Check k value of each tag ***")
    #keys = tags.process_map(filename)
    #pprint.pprint(keys)

    print("\n*** Audit stree types and city names ***")
    street_types = defaultdict(set)
    city_names = set()
    audit.audit(filename, street_types, city_names)
    pprint.pprint(dict(street_types))
    pprint.pprint(city_names)

    print("\n*** Convert data *** ")
    data.process_map(filename, False)

if __name__ == "__main__":
    main()
