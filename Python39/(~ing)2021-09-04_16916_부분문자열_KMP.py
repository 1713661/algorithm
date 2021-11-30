import sys
input = sys.stdin.readline

S = input().rstrip()
P = input().rstrip()

if S in P:
    print(1)
else:
    print(0)