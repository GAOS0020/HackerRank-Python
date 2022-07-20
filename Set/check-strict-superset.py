# source: https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
# tag: boolean

set_a = set(map(int,input().split(" ")))
n = int(input())
empty_set = set()
bool_set = False

for i in range(n):
    set_b = set(map(int,input().split(" ")))
    
    if set_b.difference(set_a)==empty_set:
        if set_a.difference(set_b)!=empty_set:
            bool_set = True
        else:
            bool_set = False
            break
    else:
        bool_set = False
        break
        
print(bool_set)

