#!/usr/bin/env python

import sys
import re

proper_name = re.compile(r"^[A-Z][a-z]{5,8}$")

proper_name_lower = re.compile(r"^[a-z]{6,9}$")

current_key = None
lower_last = None
word_sum = 0
flag_dot = 1

stop_words = set()

for line in sys.stdin:
    try:
        key, count = line.strip().split('\t', 1)
    except ValueError as e:
        print(line)
        continue
    #key, count = line.strip().split('\t', 1)
    count = int(count)
    flag = count % 2
    count = int(count / 2)
    if current_key != key:
        if current_key and flag_dot != 0 and word_sum != 0:
            print("{}\t{}".format(current_key, word_sum))
        word_sum = 0
        flag_dot = 1
    word_sum += count
    flag_dot *= flag
    current_key = key

if current_key and flag_dot != 0 and word_sum != 0:
    print("{}\t{}".format(current_key, word_sum))

