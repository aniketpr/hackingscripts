#!/usr/bin/env python
import requests
import datetime
def request(url):
    try:
        return requests.get("http://"+url)
    except requests.exceptions.ConnectionError:
        pass

# print(request("google.com"))
# To Open File and read 
#If you want to only remove whitespace from the beginning and end you can use strip
#https://docs.python.org/2/library/stdtypes.html#str.strip
# >>>'   spacious   '.strip()
# 'spacious'
# >>> 'www.example.com'.strip('cmowz.')
# 'example'
target_url = "bigbasket.com"
with open("subdomains.list","r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain -->" + test_url)
            with open(str(target_url)+"_"+str(datetime.datetime.now().date()), 'a') as f:
                print >> f, test_url + "\n"

