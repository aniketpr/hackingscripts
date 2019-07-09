#!/usr/bin/env python
import requests
import datetime
def request(url):
    try:
        return requests.get("http://"+url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "foophones.securitybrigade.com:8080"
with open("common.txt","r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered URL -->" + test_url)
            with open("out.txt", 'a') as f:
                print >> f, test_url + "\n"

