# source: https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true
# source: https://www.thepoorcoder.com/hackerrank-piling-up-solution/

from collections import deque

def check(dq):
  while dq:
    big = dq.popleft() if dq[0]>dq[-1] else dq.pop()
    if not dq:
      return "Yes"
    if dq[0]>big or dq[-1]>big:
      return "No"

n = input()
for i in range(int(n)):
  size = int(input())
  nums = deque(map(int,input().split(" ")))
  print(check(nums))
  
  
