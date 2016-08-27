#!/usr/bin/python
import sys
import string

for line in sys.stdin:
    words=line.split(" ")
    for word in words:
        word=word.strip("\n")
        if word:
            print word + ":1"

