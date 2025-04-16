#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    line = line.strip()
    try:
        word, count = line.split('\t')
        count = int(count)
        # Split on any sequence of non-alphabetic characters
        tokens = re.split(r'[^a-zA-Z]+', word)
        for token in tokens:
            if token:
                print(f"max\t{token.lower()}\t{count}")
    except ValueError:
        continue


