#!/bin/python3

import sys
from main import main
import requests


if __name__ == "__main__":
    try:
        httpResp = requests.get(f"http://{sys.argv[1]}")
        httpsResp = requests.get(f"https://{sys.argv[1]}")

        if httpResp.status_code == 200 or httpsResp.status_code == 200:
            main(sys.argv[1], sys.argv[2])
    except Exception as error:
        print(f"Usage: sudo ./whscovery.py <host> <wordlist>")