#!/usr/bin/env python

import sys
import re


for line in sys.stdin:
    datetime = line.split(' ')[0][5:-1].replace('-', '').replace(':', '').replace('.', '')
    if "UUID of player" in line:
        print("{}\t{}".format(line.split(' ')[5], datetime + '0'))
    if "lost connection:" in line:
        if "com.mojang.authlib.GameProfile" in line:
            print("{}\t{}".format(re.search(r'name=\w+', line).group(0).split('=')[-1], datetime + '2'))
        else:
            print("{}\t{}".format(line.split(' ')[3], datetime + '2'))
    if "issued server command:" in line:
        print("{}\t{}".format(line.split(' ')[3], datetime + '1'))

