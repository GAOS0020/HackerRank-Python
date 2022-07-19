/*source:https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true */
  
n = int(input())
s = set(map(int, input().split()))
n_cmd = int(input())

for i in range(n_cmd):
    attr, *kw = input().split()
    if kw:
        getattr(s,attr)(*(map(int, *kw)))
    else:
        getattr(s,attr)()


print(sum(s))

