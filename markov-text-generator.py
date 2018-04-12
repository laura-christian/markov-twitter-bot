"""Generate Markov text from text files."""

from random import choice
import sys
from collections import defaultdict
from itertools import izip

def open_and_read_file(file_list):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    combined_text = ''
    for _file in file_list:
        text_file = open(_file)
        combined_text += text_file.read()
        text_file.close()

    combined_text = combined_text.translate(None, '0123456789')

    # print combined_text
    return combined_text


# def open_and_read_file(input_path):
#     """Take file path as string; return text as string.

#     Takes a string that is a file path, opens the file, and turns
#     the file's contents as one string of text.
#     """
#     combined_text = ''
#     text_file = open(input_path)
#     combined_text += text_file.read()
#     text_file.close()
#     return combined_text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    chains = defaultdict(list)

    list_words = text_string.split()

    for a, b, c in izip(list_words, list_words[1:], list_words[2:]):
        chains[(a, b)].append(c)
    # print chains
    return chains


# text = open_and_read_file('green-eggs.txt')
# make_chains(text)


def make_text(chains):
    """Return text from chains."""

    words = []

    rkey = choice(chains.keys())
    words.extend(list(rkey))

    while rkey in chains:
        rword = choice(chains[rkey])
        if rword:
            words.append(rword)
            rkey = (rkey[1], rword)
        else:
            break
    return " ".join(words)



input_path = sys.argv[1:]

# for file in input_path:
#     input_path = ['federalist.txt', 'whitman.txt']
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

# print random_text
