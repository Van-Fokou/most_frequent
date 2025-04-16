#!/usr/bin/env python3
import sys

max_word = None
max_count = 0

for line in sys.stdin:
    try:
        _, word, count = line.strip().split('\t')
        word = word.lower()         # Normalize to lowercase
        count = int(count)
        if count > max_count:
            max_count = count
            max_word = word
    except ValueError:
        continue

if max_word:
    print(f"{max_word}\t{max_count}")

