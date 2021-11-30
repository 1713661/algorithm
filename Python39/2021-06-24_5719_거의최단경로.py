########거의 최단 경로란 최단 경로에 포함되지 않는 도로!!!!!!!!로만!!!!!!!!! 이루어진 경로 중 가장 짧은 것을 말한다. 
########문제 잘읽어라 바보야

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start,dest,node,edge):

    graph = [[] for _ in range(node+1)] 

    for _ in range(edge):   
        U,V,P = map(int,input().split())
        #graph[U].append((V,P))              # U->V 비용=P 방향그래프
        dic = graph[U]
        dic[V]=P

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
    return graph,path

'''
def delPath(graph, path):
    #도착점 당 최단 거리 지운 다음에 거의 최단 경로 구하는 건 cost가 큰가? -> 다 지우는 거 아냐!!!!!!!! 시작점->도착점 하나만 지우는거임!!!!!! 문제 똑바로 봐 바보야!!!!!!!
    #응.. 노드 당 다익스트라 실행하는 게 cost가 클듯
    #아냐!!! 다른 사람 코드도 다익스트라 실행->remove_list얻기->graph간선지우기->다익스트라 다시실행
    이런 식으로 진행하고 있음

    !!!!!!!!!!!!!내 코드의 문제는 최단 경로가 여러 개인 경우 잡아내지 못하는 것!!!!!!!!!!!!!
    
    (#### elif cost==dist[i[0]]:은 맞는 방법이 아닌 것 같다! cost와 dist[i[0]]이 같다는 게 
    그 경로가 '최단 경로'랑 같다는 게 아니라 테이블에 있는 값, 즉 "최단 경로가 아닐 수도 있는 값"이기 때문에)
'''

while True:
    N,M = map(int,input().split())  # 장소의 수=N, 도로의 수=M
    if N==0 and M==0: 
        break         
    S,D = map(int,input().split())  # 시작점=S, 도착점=D
                  
    graph,path = dijkstra(S,D,N,M) 
    print("graph=",graph)
    print("paths=",path)
    #delPath(graph,path)
