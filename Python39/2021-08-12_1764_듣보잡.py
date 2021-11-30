# 8분 시간초과
# 17분 짱나.. 그냥 파이썬 집합연산쓰면되는거였음.. 나같은 풀이는 어딨지? 
# 코드를 짜놓고 어떻게 돌아갈지 모른다는 게 가장 큰 문제야..(while 무한루프)
# 디버깅 하는 방법 훈련해야돼!!!!!! 졸업생인데 아직도 디버깅을 못한다는 건 큰 문제야...
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

l1 = []
l2 = []
answer = []
for _ in range(N):
    l1.append(input().rstrip())
l1.sort()
#print(l1)

for _ in range(M):
    l2.append(input().rstrip())
l2.sort()
#print(l2)

idx1,idx2 = 0,0

while True:
    #print(idx1,idx2)
    if idx1>N-1 or idx2>M-1: break

    if l1[idx1]==l2[idx2]:
        answer.append(l1[idx1])
        idx1 += 1
        idx2 += 1
    
    while idx1<=N-1 and idx2<=M-1 and l1[idx1]<l2[idx2]: # 인덱스범위먼저써야함
        idx1 += 1
    while idx1<=N-1 and idx2<=M-1 and l1[idx1]>l2[idx2]:
        idx2 += 1
        
            



answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])
