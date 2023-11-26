#!/usr/bin/python3
"""
Fetches https://alu-intranet.hbtn.io/status
"""

import urllib.request

url = 'https://alu-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    content = response.read()
    utf_content = content.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", utf_content)
