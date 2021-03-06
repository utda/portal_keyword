import sys
import urllib
import json
import argparse
import urllib.request
import time
import os
import requests

api_url = "https://da.dl.itc.u-tokyo.ac.jp/portal/search?items_per_page=200&_format=json&page="

loop_flg = True
page = 0

odir = "data/tmp"
os.makedirs(odir, exist_ok=True)

while loop_flg:
    url = api_url + str(
        page)
    print(url)

    page += 1

    data = requests.get(url).json()

    if len(data) > 0:
        for i in range(len(data)):
            
            url_i = data[i]["id"]

            opath = odir + "/"+url_i.split("/")[-1].split("?")[0]+".json"

            if not os.path.exists(opath):

                try:

                    headers = {"content-type": "application/json"}
                    r = requests.get(url_i, headers=headers)
                    data_i = r.json()

                    fw = open(opath, 'w')
                    json.dump(data_i, fw, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
                
                except:
                    time.sleep(0.1)
                    print("err\t"+url_i)

    # if page < 5 and False:
    #     loop_flg = False 

    else:
        loop_flg = False

