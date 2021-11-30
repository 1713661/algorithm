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

def dijkstra(g,X,distance): #X->모든점
    q = []
    distance[X] = 0
    heapq.heappush(q,(0,X))
    while q:
        dist,now = heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in g[now]: #i=(v,w)
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance            

x = 0
MAX = 0

go = dijkstra(graphI,X,go)
come = dijkstra(graph,X,come)

#print(go)
#print(come)

for i in range(1,N+1): #1~N
    x = go[i]+come[i]
    #print(i,"=",x)
    if x > MAX:
        MAX=x
print(MAX)
