#!/usr/bin/env python2

with open("mess.txt",'r') as f:
  mess = f.read()
result = ""
counts = {}
for c in mess:
  if counts.has_key(c):
    continue
  counts[c] = mess.count(c)
  if counts[c] < 10:
    result += c

print result