# 5분 한달만에 푸니까 확실히 세세한 문법 까먹었음.. 감 잃지 않도록 꾸준히 푸는 것이 중요!
import sys
input = sys.stdin.readline

N = int(input())
li = list()

for _ in range(N):
    pt = tuple(map(int,input().split()))
    li.append(pt)

li = sorted(li,key=lambda x:(x[0],x[1]))
for i in range(N):
    print(str(li[i][0])+" "+str(li[i][1]))