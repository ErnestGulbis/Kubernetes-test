#!/usr/bin/python3

import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('url', type=str, help="Your URL")
args = parser.parse_args()

def main(url):
    result = ''
    try:
        response = requests.get(url)
        if response.status_code == 200:
            result = 'success'
        else:
            result = 'failure'
    except requests.exceptions.RequestException as e:
        result = 'failure'
    return result

if __name__ == '__main__':
    main(args.url)