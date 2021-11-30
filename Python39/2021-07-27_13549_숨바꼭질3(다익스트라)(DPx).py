# 27분+14분+19분+21분(분기문 좀만 더 깔끔하게 고치면 될 것 같은데.. 하기싫다)

# DP로 풀 수 있나? (start 고정되면 d[i]=i로 오는 가장 최소 비용으로 배열 만들 수 있을듯!!) # DP는 값 순차적으로 구하기 때문에 i+1번째 값 먼저 찾기 힘듦..
# 순간이동할 경우 맨 앞에 값 추가, 이동한 값은 뒤에 값을 추가했다. (생각을 해 생각을)
# 큐에 넣는 걸 최소화!!!
# 우선순위큐에서 뭐가 제일 먼저 뽑혀야할까 생각
# BFS처럼 종료조건 꼭 써야!!!!!! 생각을 해 생각을


import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(10e9)

N,K = map(int,input().split()) #수빈,동생위치

def dijkstra(start, dest):
    q = []
    time = 0
    minTimes = [INF]*100001
    minTimes[start]=0
    heappush(q,(time,-start)) #최대힙
    while q:
        x = heappop(q)
        time,now = x[0],-x[1]
        #print("time,now=",time,now)
        if minTimes[now]<time:
            continue
        if now==dest: # 일반 다익스트라랑 다르게 목적지 도착하면 minTimes반환(근데 코드 다시보니 BFS 같은듯)
            # 우선순위큐에 넣는것도 time=0,1 두개밖에 없으니까 0은 왼쪽에 넣고 1은 오른쪽에 넣는식으로..
            return minTimes[dest]
        for next in (0,now*2), (1,now-1), (1,now+1): 
            cost = time+next[0]
            if 0<=next[1]<=100000 and cost<minTimes[next[1]]:
                minTimes[next[1]]=cost
                heappush(q,(cost,-next[1])) #최대힙
        #print(q)

#print(dijkstra(N,K))

# DP는 값 순차적으로 구하기 때문에 i+1번째 값 먼저 찾기 힘듦..
'''
def DP(start,dest):
    gap = dest-start
    d = [INF]*(gap+1) # d[0]~d[gap]
    d[0]=0
    d[1]=1
    d[2]=0 # 순간이동
    d[3]=1 # 2or4 순간이동+한칸옮기기
    d[4]=0
    d[5]=min((d[4]+1),(d[6]+1),d[5//2])=min(1,?,없음)=1
    d[6]=min((d[5]+1),(d[7]+1),d[6//2])=min((1,?,1))=min

    # d[1]=start~1 최소비용 
    # d[2]=start~2 최소비용
    # ... 
    # 흠.. 
    for i in range(100000):
        if dest%2==0:
            d[i] = d[i//2]+d[i-1]+d[i+1]
'''