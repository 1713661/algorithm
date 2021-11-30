import heapq
def solution(n, s, a, b, fares):
    answer = 0 #최저택시요금
    graph = [[] for _ in range(n+1)] #graph[0]~graph[n] 2차원배열
    for i in range(len(fares)): #fares[0]~fares[끝]
        c = fares[i][0] #코드 줄이는법 리스트는 split()함수 없다고 함
        d = fares[i][1]
        f = fares[i][2]
        graph[c].append((d,f))
        graph[d].append((c,f))# 무방향 그래프니까 반대로도 넣어야하나? 다익스트라니까 아닐 것 같음 NO!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 넣어야함!!!!!!!!!!!!
    print(graph)
    path=[[] for _ in range(n+1)] #s부터 x까지의 경로 path[4]=[1,2]이면 s-4까지 최단거리 지나는 경로가 s-1-2-4라는 뜻 튜플로 바꿔야하나???
    path_tmp=[]
    #다익스트라
    INF = int(1e9)
    dist = [INF]*(n+1) #최단 거리 테이블
    q = []
    dist[s]=0
    heapq.heappush(q,(0,s)) #(w,v)
    while q:
        distance, now = heapq.heappop(q)
        print(q)
        path[now].append(now) #################################고쳐야 함
        print(path)
        if distance>dist[now]:
            #######이미 방문한 노드 여기다 뭐하면 될 것 같은데!!!!!!!!!!!!!!!!!!!!!!!!!!!
            continue
        for i in graph[now]: #i=(v,w) 튜플
            cost = distance+i[1]
            if cost<dist[i[0]]:
                dist[i[0]] = cost
                #path=[[] for _ in range(n)] #s부터 x까지의 경로 path[4]=[1,2]이면 s-4까지 최단거리 지나는 경로가 s-1-2-4라는 뜻 튜플로 바꿔야하나???
                heapq.heappush(q,(cost,i[0]))
        print(now,"=",dist)
    #print(dist)
    #s-a s-b
    print('path=',path)
    pathA = path[a] #S-A까지 최저요금으로 갈 때 A가 가는 경로
    pathB = path[b]
    print(pathA)
    print(pathB)
    k=0 ##############파이썬은 지역변수 단위 반복문도 해당인가???????????????
    #for i in range(n+1): #이렇게 쓰면 안됨!!!!!!!!! list index out of range
    i=-1
    while True:
        i += 1
        if pathA[i]==pathB[i]: #경로가 같으면 합승
            continue
        #처음 경로가 다르기 시작함. 이 분기점 저장
        else:
            k = pathA[i]
            break   #break문써야하기 때문에 else문 써줘야함(생각을 해 생각을)
    #answer=A+B-합승도착점
    answer = dist[a]+dist[b]-dist[k]
    return answer
