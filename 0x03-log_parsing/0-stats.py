#!/usr/bin/python3
"""
Log parsing
"""

import sys
fz = 0
count = 0

try:
    for line in sys.stdin:
        print(line)
        [code, status] = line.split()[-2:]
        print(code, status)
except KeyboardInterrupt:
    print("hello")
