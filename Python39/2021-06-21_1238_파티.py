import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N,M,X = map(int,input().split())

graph = [[] for _ in range(N+1)]
graphI = [[] for _ in range(N+1)] #모든점->X에 쓸 그래프

for _ in range(M):
    start, end, T = map(int,input().split())
    graph[start].append((end,T))
    graphI[end].append((start,T)) #end,start 반대로 넣어줌

#print(graph)
#print(graphI)

go = [INF]*(N+1) #모든점->X
come = [INF]*(N+1) #X->모든점

def dijkstra_go(X): #모든점->X 알고리즘 거꾸로?
    q = []
    go[X] = 0
    heapq.heappush(q,(0,X))
    while q:
        dist,now = heapq.heappop(q)
        if dist>go[now]:
            continue
        for i in graphI[now]:
            cost = dist+i[1]
            if cost<go[i[0]]:
                go[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

def dijkstra_come(X): #X->모든점
    q = []
    come[X] = 0
    heapq.heappush(q,(0,X))
    while q:
        dist,now = heapq.heappop(q)
        if dist>come[now]:
            continue
        for i in graph[now]: #i=(v,w)
            cost = dist+i[1]
            if cost<come[i[0]]:
                come[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                

distance = 0
MAX = 0

dijkstra_go(X)
dijkstra_come(X)

print(go)
print(come)

for i in range(1,N+1):
    distance = go[i]+come[i]
    print(i,"=",distance)
    if distance > MAX:
        MAX=distance
print(MAX)

    
