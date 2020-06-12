import sys
import urllib
import json
import argparse
import urllib.request
import time
import os
import requests
import glob
import hashlib

files = glob.glob("data/tmp/*.json")

arr = []

for i in range(len(files)):
    file = files[i]

    if i % 100 == 0:
        print(i+1, len(files))

    try:
        with open(file, 'r') as f:
            data = json.load(f)
        arr.append(data)
    except Exception as e:
        print(file, e)

fw2 = open("data/data.json", 'w')
json.dump(arr, fw2, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
