#!/usr/bin/env python2.7
"""
new_password.py
By Simon Pratt

Generates strong passwords
"""

DICT_FILE  = '/usr/share/dict/words'
NUM_WORDS  = 4
MIN_LENGTH = 4
MAX_LENGTH = 6

# count lines in file
nlines = 0
for line in open(DICT_FILE).xreadlines():
    nlines += 1

import linecache
from random import randint

words = []

while len(words) < NUM_WORDS:
    n = randint(0, nlines)
    word = linecache.getline(DICT_FILE, n).strip()
    if len(word) >= MIN_LENGTH and len(word) <= MAX_LENGTH:
        words.append(word)

for word in words:
    print word,

