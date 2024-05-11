#!/usr/bin/python3

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

# Fetching the URL content using urllib
with urllib.request.urlopen(url) as response:
    # Reading the response data
    html_content = response.read().decode('utf-8')

    # Displaying the body of the response with tabulation
    print("- Body response:")
    print("\t- type:", type(html_content))
    print("\t- content:", html_content)
