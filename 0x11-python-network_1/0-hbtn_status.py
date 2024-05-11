#!/usr/bin/python3

"""
This script fetches the status from https://alx-intranet.hbtn.io/status
and displays the body of the response with information about it.
"""

import urllib.request


def fetch_status():
    """
    Fetches the status from a specified URL and displays the response details.
    """
    url = 'https://alx-intranet.hbtn.io/status'

    # Fetching the URL content using urllib
    with urllib.request.urlopen(url) as response:
        # Reading the response data
        html_content = response.read().decode('utf-8')

        # Displaying the body of the response with tabulation
        print("- Body response:")
        print("\t- type:", type(html_content))
        print("\t- content:", html_content)


if __name__ == "__main__":
    fetch_status()
