#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mapparser
import pprint
import tags
import audit
import data
def main():
    filename = 'san-francisco.osm'
    #print("\n*** Check the number of tags ***")
    #taglist = mapparser.count_tags(filename)
    #pprint.pprint(taglist)

    #print("\n*** Check k value of each tag ***")
    #keys = tags.process_map(filename)
    #pprint.pprint(keys)

    #print("\n*** Audit stree types ***")
    #st_types = audit.audit(filename)
    #pprint.pprint(dict(st_types))

    print("\n*** Convert data *** ")
    data.process_map(filename, False)

if __name__ == "__main__":
    main()
