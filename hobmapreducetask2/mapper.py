#!/usr/bin/env python

import sys
import re

#reload(sys)
#sys.setdefaultencoding('utf-8') # required to convert to unicode

proper_name = re.compile(r"^[A-Z][a-z]{5,8}$")

proper_name_lower = re.compile(r"^[a-z]{6,9}$")

flag = 0
count = 0

for line in sys.stdin:
    try:
        article_id, text = line.strip().split('\t', 1)
    except ValueError as e:
        continue
    words = re.split('\W*\s+\W*', text, flags=re.UNICODE)
    for word in words:
        flag = 1
        count = 0
        if re.match(proper_name, word):
            count = 1
        if re.match(proper_name_lower, word):
            flag = 0

        print("{}\t{}".format(word.lower(), int(count*2 + flag)))

