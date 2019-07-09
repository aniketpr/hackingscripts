#!/usr/bin/env python

import requests

target_url = "http://testphp.vulnweb.com/userinfo.php"
data_dict = {"uname":"test", "pass":"test", "login": "submit"}
response = requests.post(target_url, data=data_dict)
print(response.content)