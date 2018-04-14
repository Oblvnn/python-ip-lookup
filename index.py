#!/usr/bin/python

import requests
import sys

suffix = sys.argv[1]
lookup = ("http://json.geoiplookup.io/" + suffix)
response = requests.get(lookup);

print(response.text)