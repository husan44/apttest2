#! /usr/bin/env python3
print("This")
#wow this is a really good comment
import sys

out_of = float(sys.argv[1])
while 1:
    line = input()
    total = 0
    for num in line.split(" "):
        total += int(num)
    print("Total: %d (%f%%)" % (total, total * (100.0 / out_of)))

