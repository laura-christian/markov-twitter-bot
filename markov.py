"""A Markov chain generator that can tweet random messages."""

import os
import sys
from random import choice
import twitter
from collections import defaultdict
from itertools import izip
import re


def open_and_read_file(filenames):
    """Take list of files. Open them, read them, and return one long string."""

    body = ""

    for filename in filenames:
        text_file = open(filename)
        body = body + text_file.read()
        text_file.close()

    body = body.translate(None, '0123456789')

    return body


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains."""

    chains = defaultdict(list)

    list_words = text_string.split()

    for a, b, c in izip(list_words, list_words[1:], list_words[2:]):
        chains[(a, b)].append(c)
    # print chains

    return chains


def make_text(chains):
    """Take dictionary of Markov chains; return random text."""

    key = choice(chains.keys())
    words = [key[0], key[1]]
    while key in chains and len(words) < 100:
        # Keep looping until we have a key that isn't in the chains
        # (which would mean it was the end of our original text).
        #
        # Note that for long texts (like a full book), this might mean
        # it would run for a very long time.

        word = choice(chains[key])
        words.append(word)
        key = (key[1], word)

    return " ".join(words)


def tweet(random_text):
    """Create a tweet and send it to the Internet."""

    # Use Python os.environ to get at environmental variables
    # Note: you must run `source secrets.sh` before running this file
    # to make sure these environmental variables are set.    
    
    line_list = []
    i_first_capital = re.search('[A-Z]', random_text).start()
    while len('\n'.join(line_list)) < 280:
        i_next_capital = re.search('[A-Z][a-z]', random_text[i_first_capital+1:]).start()
        line = random_text[i_first_capital:i_first_capital+i_next_capital]
        line_list.append(line)
        # print line_list
        random_text = random_text[i_first_capital + i_next_capital + 1:]
        i_first_capital = 0
    if len('\n'.join(line_list)) > 280:
        line_list = line_list[:-1]

    return '\n'.join(line_list)


