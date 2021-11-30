import sys
input = sys.stdin.readline
t = int(input())
MAX = 0
for i in range(t):
    N = int(input())
    for j in range(N):
        S,L = input().split()
        L = int(L)
        #MAX = max(MAX,int(L)):
        if MAX<L:
            MAX = L
            XS = S
    print(XS)
