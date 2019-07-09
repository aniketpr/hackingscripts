#!/usr/bin/env python
import requests
import re
import urlparse

target_url = "https://www.firstrade.com/"
target_links = []

def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)

def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urlparse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            print(link)
            with open("out_{}.txt".format("firstrade"), 'a') as f:
                print >> f, link + "\n"
            crawl(link)

crawl(target_url)
