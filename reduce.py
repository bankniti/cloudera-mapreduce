#!/usr/bin/python
import sys
import string

oldkey = ""
count = 0

for line in sys.stdin:
    words = line.split(":")
    key = words[0].strip()
    val = words[1].strip()
    if (oldkey==""):
        oldkey=key
    if (oldkey!=key):
        print oldkey+":"+str(count)
        oldkey=key
        count=0
    count=count+1

