#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    line = line.strip()
    try:
        word, count = line.split('\t')
        # Normalize word by removing non-alphanumeric characters (keep hyphens inside words)
        # Split further if compound
        tokens = re.split(r'[^a-zA-Z0-9]+', word)
        for token in tokens:
            if token:
                print(f"max\t{token.lower()}\t{count}")
    except ValueError:
        continue

