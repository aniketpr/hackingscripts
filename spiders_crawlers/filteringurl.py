#!/usr/bin/env python
import requests
import re
import urlparse

target_url = "http://nettechindia.com/"

def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)

href_links = extract_links_from(target_url)
for link in href_links:
    link = urlparse.urljoin(target_url, link)
#    print(link)
    if target_url in link:
        print(link)

