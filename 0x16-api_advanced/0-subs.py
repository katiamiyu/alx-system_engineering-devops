#!/usr/bin/python3
"""
defines the main function to get
the sub count from the reddit
api
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    query the reddit api to get the number of subscribers
    for a particular subreddit
    """
    if subreddit is None:
        return (0)
    endpoint = 'https://www.reddit.com'
    headers = {'user-agent': 'Testapi/1.0 by danjor667'}
    info = requests.get('{}/r/{}/about.json'.format(
        endpoint,
        subreddit), headers=headers, allow_redirects=False)
    if info.status_code == 200:
        data_info = info.json()
        return (data_info.get('data').get('subscribers'))
    else:
        return (0)
