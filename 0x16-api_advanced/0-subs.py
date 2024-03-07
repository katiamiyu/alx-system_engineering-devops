#!/usr/bin/python3
'''
this module contains the retrieves number_of_subscribers
'''
import requests
from sys import argv


def number_of_subscribers(sub_reddit):
    '''returns the nos for a given subreddit'''

    user = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(sub_reddit), headers=user).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
