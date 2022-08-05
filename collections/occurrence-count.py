# source:https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true

from collections import Counter

s = input()

chars = Counter(s).items()

for char,occurence in sorted(chars, key = lambda c: (-c[1],c[0]))[:3]:
  print(char,occurence)
  
  
