import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

##################################지역변수여서 배열값 내가 생각한대로 안되는건가? backup이 내가 생각하는거랑 다르게 돌아가는듯
def dijkstra(start,dest,node,edge):

    graph = [[] for _ in range(node+1)]

    for _ in range(edge):
        U,V,P = map(int,input().split())
        graph[U].append((V,P))      # U->V 비용=P 방향그래프
    print("graph = ",graph)

    q = []  #우선순위 큐 (weight,v) 튜플 형태 넣을거임
    dist = [INF]*(node+1)   # 최단 거리 테이블
    dist[start] = 0
    path=[[] for _ in range(node+1)]    #path[k]=start~k까지 최단 경로 지나는 노드
    
    heapq.heappush(q,(0,start))
    for p in path:
        p.append(start) #시작점 다 넣어주기
        
    print(path)    
    while q:
        distance, now = heapq.heappop(q)

        if distance>dist[now]:
            continue
        for i in graph[now]:    #i=(v,weight)
            backup=[]
            backup= path[now].copy()
            ###################### backup=path[now]라고 하면 안돼!!!! 값을 받아오는 게 아니라 참조하는 거기 때문에!!!! 다시 복습
            cost = distance+i[1]    #########여기가 제일 헷갈리는듯 distance=start~now i[1]=now~v
            if cost<dist[i[0]]:  ###현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                dist[i[0]]=cost #최단 거리 갱신
                heapq.heappush(q,(cost,i[0])) #####그림이랑 같이 보며 이해하기!!!
                path[i[0]].clear()
                path[i[0]]=backup
                #print(i[0],backup)
                path[i[0]].append(i[0])
                #print(path)
    print("final=",path)

while True:
    N,M = map(int,input().split())  # 장소의 수=N, 도로의 수=M
    if N==0 and M==0: 
        break         
    S,D = map(int,input().split())  # 시작점=S, 도착점=D
                  
    dijkstra(S,D,N,M)   #변수 너무 많이 넣는거 아닌가???????????????????아냐이정도는 괜찮을듯

