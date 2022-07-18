#source:https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

import string
alpha = string.ascii_lowercase

def print_rangoli(size):
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        s = s[::-1] + s[1:]
        L.append(s.center(4*n-3,"-"))
    print('\n'.join(L[:0:-1]+L))
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    
    
