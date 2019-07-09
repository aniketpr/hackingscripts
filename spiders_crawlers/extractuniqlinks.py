#!/usr/bin/env python
import requests
import re
import urlparse

target_url = "http://nettechindia.com/"
target_links = []

def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)

href_links = extract_links_from(target_url)
for link in href_links:
    link = urlparse.urljoin(target_url, link)

    if "#" in link:
        link = link.split("#")[0]

    if target_url in link and link not in target_links:
        print(link)


