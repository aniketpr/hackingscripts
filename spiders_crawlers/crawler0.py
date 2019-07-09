#!/usr/bin/env python
import requests

url = "www.firstrade.com/content/en-us/welcome"

try:
    get_resposne = requests.get("http://"+url)
    print(get_resposne)
except requests.exceptions.ConnectionError:
    pass