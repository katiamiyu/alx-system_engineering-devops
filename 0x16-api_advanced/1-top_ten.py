#!/usr/bin/python3
'''
this module contains the function to retrieve top_ten
'''
import requests
from sys import argv


def top_ten(sub_reddit):
    '''
    returns the top ten posts
    '''
    user = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(sub_reddit), headers=user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
