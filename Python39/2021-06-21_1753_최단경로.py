import sys
import heapq
input = sys.stdin.readline #라이브러리뭐였지? sys.stdline.readline

INF = int(1e9) #숫자 표현하는법? int(1e9)

V,E = map(int,input().split()) #split함수도 까먹다니? map함수였음!!!!!!!!어쩐지 이상하드라..
start = int(input())

graph = [[] for _ in range(V+1)] #배열 for문 이렇게 선언하는거 맞았었나?
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w)) #append안에 배열로 선언했었나? 튜플? 튜플로 초기화 맞음!
    #graph[v].append((u,w)) 방향 그래프니까 바꿔서 넣으면 안됨???
'''
for i in range(V):   #정렬해야 찾기 편하니까 근데 튜플이어서 sort()쓰는 게 맞는건지..
    graph[i].sort()  #dfs/bfs랑 다르게 정렬할 필요 없을듯?
''' 
print(graph)

dist = [INF]*(V+1) #시작점에서 각 점까지의 최단경로 [INF]*(V+1)

def dijkstra(start):
    q = [] #힙 배열이랑 똑같이 초기화!!!
    heapq.heappush(q,(start,0)) #튜플로 넣어주는거맞나?
    dist[start] = 0
    while q:
        now, distance = heapq.heappop(q) #튜플을 꺼내서 now,distance에 어떻게 넣어주지? split함수?
        if dist[now]<distance:
            continue
        for i in graph[now]: #i는 [(v,w),(v2,w2),...]꼴의 '배열'!!!!!!!!!!!!!!!! 반대로!!!! 우선순위큐기 때문에!!!!!
            cost = distance+i[1] #최단 경로 테이블 갱신받기 전에 cost로 받아야함
            if cost<dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (i[0],cost))
        print(dist)
        
dijkstra(start)

for i in range(1,V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])

                               

                    
    
