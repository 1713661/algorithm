import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start,dest,node,edge):

    graph = [[] for _ in range(node+1)] 

    for _ in range(edge):   
        U,V,P = map(int,input().split())
        graph[U].append((V,P))            # U->V 비용=P 방향그래프 딕셔너리 쓸거면 dict()함수 써야함!!!! {} 쓰면 안되는 것 같음
    

    print(graph)
    q = []                  #우선순위 큐 (weight,v) 튜플 형태 넣을거임
    dist = [INF]*(node+1)   # 최단 거리 테이블
    dist[start] = 0

    path=[[] for _ in range(node+1)]    #path[k]=start~k까지 최단 경로가 지나는 노드들(배열 형태) 흠... 설명 너무 못하는듯
    for p in path:
        p.append(start)                 #시작점 다 넣어주기
 

    heapq.heappush(q,(0,start))
        
    while q:
        distance, now = heapq.heappop(q)
        if distance>dist[now]:
            continue
        for i in graph[now]:    #i=(v,weight)
            cost = distance+i[1]                #########여기가 제일 헷갈리는듯 distance=start~now i[1]=now~v
            if cost<dist[i[0]]:                 ###현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                dist[i[0]]=cost                 #최단 거리 갱신
                heapq.heappush(q,(cost,i[0]))   #####그림이랑 같이 보며 이해하기!!!
                path[i[0]] = path[now].copy()
                path[i[0]].append(i[0])         # 최단 경로에 지금 노드 추가
           # elif cost==dist[i[0]]:
           # 은 맞는 방법이 아닌 것 같다! cost와 dist[i[0]]이 같다는 게 
           # 경로가 '최단 경로'랑 같다는 게 아니라 테이블에 있는 값, 
           # 즉 """""최단 경로가 아닐 수도 있는 값"""""이기 때문에  
           # 인터넷 풀이처럼 bfs로 역추적하는 게 좋은 것 같다. (근데 왜 굳이 '역'추적해야하지??????????????????????????)          
    return graph,path


def delPath(graph, paths):
    delTuples=[]
    for path in paths:
        for i in range(len(path)-1):
            delTuples.append((path[i],path[i+1]))
    print("delTuples=",delTuples)
    return delTuples




while True:
    N,M = map(int,input().split())  # 장소의 수=N, 도로의 수=M
    if N==0 and M==0: 
        break         
    S,D = map(int,input().split())  # 시작점=S, 도착점=D
                  
    graph,path = dijkstra(S,D,N,M) 
    print("graph=",graph)
    print("paths=",path)
    delT = delPath(graph,path)
