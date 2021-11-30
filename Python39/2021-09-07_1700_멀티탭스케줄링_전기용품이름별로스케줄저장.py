# 전기용품의 이름이 K 이하의 자연수로 사용 순서대로 주어진다
# 왜 K '이하'????? 아 전기용품 이름이..

# 사용하고 있는 전기용품의 사용순서를 알아내었고, 
# 이를 기반으로 플러그를 빼는 횟수를 최소화하는 방법을 고안

# 39분 한 27분까지는 갔던 것 같음

############ heap보다 각 전기용품이름별로 wait 저장하는 게 나음(그래야 관리하기쉬움)

# +33분
import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int,input().split()) # 1<=멀티탭 구멍의개수, 전기용품총사용횟수<=100

answer = 0
sche = list(map(int,input().split()))

multitap = [0]*N
wait = [deque() for _ in range(K+1)]
length = len(sche)
for idx in range(length):
    wait[sche[idx]].append(idx) # wait[전기용품이름]=시간
#print([list(item) for item in wait])
for idx in range(length):
    if sche[idx] in multitap:
        continue
    else:
        if 0 in multitap:
            multitap[multitap.index(0)]=sche[idx]
        else:
            next = [102]*len(multitap) # next = [멀티탭에꽂힌전기용품의다음사용시간]
            for i in range(N):#for tap in multitap:
                if len(wait[multitap[i]])==0:
                    continue
                while len(wait[multitap[i]])>0 and wait[multitap[i]][0]<idx:
                    wait[multitap[i]].popleft()
                if len(wait[multitap[i]])>0:
                    next[i] = wait[multitap[i]][0] #바로다음사용시간
                #print("idx=",idx,"wait=",[list(item) for item in wait])
            #print("multitap=",multitap)
            #print("next=",next)
            multitap[next.index(max(next))]=sche[idx]
            answer += 1
            #print("idx=",idx,"answer=",answer,"multitap=",multitap)
            
print(answer)

    







