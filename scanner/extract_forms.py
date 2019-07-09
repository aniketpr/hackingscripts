#!/usr/bin/env python

import requests
from BeautifulSoup import BeautifulSoup

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass 

target_url = "https://google.com"
response = request(target_url)

parsed_html = BeautifulSoup(response.content)
forms_list = parsed_html.findAll("form")
print(forms_list)