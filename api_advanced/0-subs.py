"""This module provides a function to query the Reddit API and retrieve
the number of subscribers for a given subreddit.

**Functions:**

* `number_of_subscribers(subreddit)`: Retrieves the number of subscribers
  for a given subreddit. Returns 0 if the subreddit is invalid or an error occurs.

**Error Handling:**

* The function handles potential request errors and missing keys in the response data,
  providing informative messages to the user.
"""

import requests  # Imported alphabetically


def number_of_subscribers(subreddit):
    """Retrieves the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if invalid or an error occurs.
    """

    headers = {'User-Agent': 'MyAPI/0.0.1'}  # Custom User-Agent

    try:
        response = requests.get(f"https://reddit.com/r/{subreddit}.json", headers=headers, allow_redirects=False)
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
    print(f"Output: Existing Subreddit - The subreddit '{subreddit_name}' has {subscribers} subscribers.")
else:
    print(f"Output: Non-existing subreddit - The subreddit '{subreddit_name}' may not exist or an error occurred.")

