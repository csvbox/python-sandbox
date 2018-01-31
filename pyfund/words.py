#!/usr/bin/env python3
"""Retrieve and print words from a url

Usage:
    python words.py <url>

"""
import sys
from urllib.request import urlopen


def fetch_words(uri):
    """Prints words from a url.

    Args:
        uri: url of a document in utf-8 encoding

    Returns:
        A list of strings containing words from the document

    """
    story_words = []
    with urlopen(uri) as story:
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Prints items, one per line

    Args:
        items: Any iterable set of items

    """
    for item in items:
        print(item)


def main(uri):
    """Prints words from a url.

    Args:
        uri: url of a document in utf-8 encoding

    Returns:
        A list of strings containing words from the document

    """
    print_items(fetch_words(uri))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        url = 'https://sixty-north.com/c/t.txt'
    else:
        url = sys.argv[1]
    main(url)
