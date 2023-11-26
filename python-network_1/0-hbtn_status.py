#!/usr/bin/python3
"""
Fetches http://0.0.0.0:5050/status
"""

import urllib.request

url = 'http://0.0.0.0:5050/status'

with urllib.request.urlopen(url) as response:
    content = response.read()
    utf_content = content.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", utf_content)
