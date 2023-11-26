#!/usr/bin/python3
"""Fetches a specified URL and displays the body response."""
import urllib.request

def fetch_and_display(url):
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))

if __name__ == "__main__":
    # Fetch and display status from https://alu-intranet.hbtn.io/status
    print("Fetching from https://alu-intranet.hbtn.io/status:")
    fetch_and_display("https://alu-intranet.hbtn.io/status")

    # Fetch and display status from http://0.0.0.0:5050/status
    print("\nFetching from http://0.0.0.0:5050/status:")
    fetch_and_display("http://0.0.0.0:5050/status")
