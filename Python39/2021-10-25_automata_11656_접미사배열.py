import sys
input = sys.stdin.readline

S = input().rstrip()
li = []
for n in range(len(S)):
    li.append(S[n:])
li.sort()
for l in li:
    print(l)
