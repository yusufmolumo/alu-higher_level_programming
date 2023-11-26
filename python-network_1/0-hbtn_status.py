#!/usr/bin/python3
"""
Fetches both https://alu-intranet.hbtn.io/status and https://intranet.hbtn.io/status
"""

import urllib.request

def fetch_and_print(url):
    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf_content = content.decode('utf-8')

        print(f"Body response for {url}:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", utf_content)

if __name__ == "__main__":
    url1 = 'https://alu-intranet.hbtn.io/status'
    url2 = 'https://intranet.hbtn.io/status'

    fetch_and_print(url1)
    fetch_and_print(url2)
