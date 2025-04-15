#!/usr/bin/env python3
import sys

for line in sys.stdin:
    try:
        word, count = line.strip().split('\t')
        print(f"max\t{word}\t{count}")
    except ValueError:
        continue
