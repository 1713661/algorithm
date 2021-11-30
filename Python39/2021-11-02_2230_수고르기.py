import sys
input = sys.stdin.readline

N,M = map(int,input().split()) #길이N 수열 그 차이가 M이상인....
li = []
for _ in range(N):
    li.append(int(input().rstrip()))
li.sort()

en = 0
dif = int(2e9)+1
for st in range(N):
    while en<N and li[en]-li[st]<M:
        en += 1
    if en==N: break
    dif = min(dif,li[en]-li[st])
    
print(dif)