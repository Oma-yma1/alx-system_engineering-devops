#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """function count words"""
    if counts is None:
        counts = {}

    if not subreddit:
        return

    headers = {'User-agent': 'count_words_bot'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else None

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    for post in posts:
        title = post['data']['title']
        for word in word_list:
            word = word.lower()
            count = title.lower().count(word)
            counts[word] = counts.get(word, 0) + count

    if data['data']['after']:
        return count_words(subreddit, word_list, data['data']['after'], counts)

    result = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in result:
        if count > 0:
            print(f"{word}: {count}")


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming
              'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = [x.lower() for x in sys.argv[2].split()]
        count_words(subreddit, keywords)
