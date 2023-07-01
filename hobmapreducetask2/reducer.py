#!/usr/bin/env python

import sys
import re

current_key = None
was_open = False
session_sum = 0
command_sum = 0

for line in sys.stdin:
    key, time = line.strip().split('\t', 1)
    event = time[-1]
    #print(event)

    if current_key != key:
        was_open = False
        if current_key and command_sum != 0 and session_sum != 0:
            print("{} \t {:.2f} \t {}".format(current_key, command_sum / session_sum, session_sum))
        command_sum = 0
        session_sum = 0
    if event == '0':
        was_open = True
        session_sum += 1
    if event == '1':
        command_sum += 1
    current_key = key

if current_key and command_sum != 0 and session_sum != 0:
    print("{}\t{:.2f}\t{}".format(current_key, command_sum / session_sum, session_sum))

