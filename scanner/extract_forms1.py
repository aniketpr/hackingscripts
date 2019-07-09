#!/usr/bin/env python

import requests
from BeautifulSoup import BeautifulSoup
import urlparse

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass 

target_url = "http://nettechindia.com/"
response = request(target_url)

parsed_html = BeautifulSoup(response.content)
forms_list = parsed_html.findAll("form")

for form in forms_list:
    action = form.get("action")
    post_url = urlparse.urljoin(target_url, action)
    print(action)
    print(post_url)
    method = form.get("method")
    print(method)

    input_list = form.findAll("input")
    for input in input_list:
        input_name = input.get("name")
        print(input_name)





