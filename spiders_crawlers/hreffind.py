#!/usr/bin/env python
import requests
import re
import datetime
def request(url):
    try:
        return requests.get("https://"+url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "firstrade.com/content/en-us/welcome"

response = request(target_url)

href_links = re.findall('(?:href=")(.*?)"', response.content)

for link in href_links:
    with open("out_{}.txt".format("htref"), 'a') as f:
        print >> f, link + "\n"
print(href_links)


