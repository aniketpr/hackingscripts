#!/usr/bin/env python
import requests
import datetime
from BeautifulSoup import BeautifulSoup
import urlparse
from termcolor import colored

def request(url):
    try:
        return requests.get("http://"+url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "adityatekkali.edu.in"
with open("nova.txt","r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
           # response1 = request(test_url)
            parsed_html = BeautifulSoup(response.content)
            forms_list = parsed_html.findAll("form")
            # print(test_url)
            print colored(test_url, 'green')
            with open("nova_result.txt", 'a') as f:
                print >> f, test_url + "\n"

