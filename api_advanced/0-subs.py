#!/usr/bin/python3
"""Writing a function that queries the Reddit API and returns
the number of subscribers for a given subreddit.

Returns 0 if the subreddit is invalid or an error occurs."""

import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'MyAPI/0.0.1'}  # Custom User-Agent
    subreddit_url = f"https://reddit.com/r/{subreddit}.json"  # f-string formatting

    try:
        response = requests.get(subreddit_url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise exception for non-200 status codes

        json_data = response.json()
        subscriber_number = json_data.get('data').get('children')[0].get('data').get('subreddit_subscribers')
        return subscriber_number

    except requests.exceptions.RequestException as e:
        # Handle various request errors
        print(f"Error: Could not retrieve data for subreddit '{subreddit}' ({e})")
        return 0

    except KeyError:
        # Handle cases where the expected key 'subreddit_subscribers' is missing
        print(f"Invalid subreddit: '{subreddit}'")
        return 0


# Example usage
subreddit_name = input("Enter a subreddit name: ")
subscribers = number_of_subscribers(subreddit_name)

if subscribers:
    print(f"The subreddit '{subreddit_name}' has {subscribers} subscribers.")
else:
    print(f"The subreddit '{subreddit_name}' may not exist or an error occurred.")

