#!/usr/bin/env python3
'''
I need to revise this concepts this can be done by daily practising
'''

import sys

logfile = sys.argv[1]
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        print(line.strip())

