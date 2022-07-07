# source:
# https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


if __name__ == '__main__':
        N, M = map(int, input().split(" "))

        for i in range(1,N+1):
            pattern = ".|."
            if i<((N+1)/2):
                print((pattern*(2*i-1)).center(M,"-"))
            elif i==((N+1)/2):
                print("WELCOME".center(M,"-"))
            else:
                print((pattern*(2*(N+1-i)-1)).center(M,"-"))
                
                
               
