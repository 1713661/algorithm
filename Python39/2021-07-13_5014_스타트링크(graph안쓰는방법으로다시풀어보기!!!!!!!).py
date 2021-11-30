# 백만개까지 갈 수 있으니까 dist배열이 아니라 튜플에 저장하기

import sys
##import heapq 우선순위 큐 아니야!!!!!
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int,input().split())

graph=[[] for _ in range(F+1)]  # n차원 배열에서 *(F+1)이랑 어떻게 다른지..
# 왜 graph=[[0] for _ in range(F+1) for _ in range(F+1)]이 아니라
# graph=[[0]*(F+1) for _ in range(F+1)] 이렇게 쓰는지
for i in range(F+1):
    if i+U<F+1:     #연산자 우선순위??
        graph[i].append(i+U)
    if i-D>0:
        graph[i].append(i-D)
#print(graph)

# 이렇게 쓰면 시간초과(deque에 '튜플' 저장해서 오래걸리는듯)
'''
q = deque()
q.append((S,0))
visited = [False]*(F+1)
while q:
    now,count = q.popleft()
    visited[now] = True
    if now == G:
        print(count)
        break
    for i in graph[now]:
        if not visited[i]:
            q.append((i,count+1))
if now != G:    #break쓰면 now==G만족해도 여기로 오니까!!! return문이랑 헷갈리면 안돼!!
    print("use the stairs")
'''
# 이건 메모리 200MB잡아먹음.. S,G,F다 100만까지 갈 수 있으니까 기존 방식대로 그래프 만드는건 비효율적인듯
# 파이썬 랭킹 제일 높은 코드 보니까 "나머지" 연산써서 그래프 길이 줄이는듯!!!!
'''
def bfs():
    #visited = [False]*(F+1)
    distance = [-1]*(F+1)   #출발점에서 각 노드의 거리값 저장할 배열!!!!! 이거 쓰면 visited배열 쓸 필요 없을듯? 아냐 있어야할듯
    queue = deque([S])
    distance[S]=0   #자기자신과의 거리는 0
    while queue:
        now = queue.popleft()
        if now == G:
            return distance[now]
        for i in graph[now]:
            if distance[i]==-1: # i는 아직 방문하지 않는 노드라는 거니까
                distance[i] = distance[now]+1
                queue.append(i)
    return "use the stairs"
'''

#함수 안쓰면 메모리 좀 줄어들까? 아냐 똑같음..
distance = [-1]*(F+1)   #출발점에서 각 노드의 거리값 저장할 배열!!!!! 이거 쓰면 visited배열 쓸 필요 없을듯? 아냐 있어야할듯
queue = deque([S])
distance[S]=0   #자기자신과의 거리는 0
while queue:
    now = queue.popleft()
    if now == G:
        print(distance[now])
        break
    for i in graph[now]:
        if distance[i]==-1: # i는 아직 방문하지 않는 노드라는 거니까
            distance[i] = distance[now]+1
            queue.append(i)
if now!=G:
    print("use the stairs")






