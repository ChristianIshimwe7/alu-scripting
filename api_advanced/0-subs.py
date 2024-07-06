#!/usr/bin/python3
"""Writing a function that queries the Reddit API and returns
the number of subscribers for a given subreddit.

Provides informative outputs for both existing and non-existing subreddits."""

import requests


def number_of_subscribers(subreddit):

    headers = {'User-Agent': 'MyAPI/0.0.1'}  # Custom User-Agent for API usage
    subreddit_url = f"https://reddit.com/r/{subreddit}.json"  # f-string formatting

    try:
        response = requests.get(subreddit_url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        json_data = response.json()
        subscriber_number = json_data['data']['children'][0]['data']['subreddit_subscribers']
        return subscriber_number

    except requests.exceptions.RequestException as e:
        # Handle various request errors
        print(f"Error: Could not retrieve data for subreddit '{subreddit}' ({e})")
        return 0

    except KeyError:
        # Handle cases where the expected key 'subreddit_subscribers' is missing
        print(f"Output: Non-existing subreddit '{subreddit}'")
        return 0


# Example usage
subreddit_name = input("Enter a subreddit name: ")
subscribers = number_of_subscribers(subreddit_name)

if subscribers:
    print(f"Output: Existing Subreddit - {subscribers} subscribers")
else:
    print(f"The subreddit '{subreddit_name}' may not exist or an error occurred.")

