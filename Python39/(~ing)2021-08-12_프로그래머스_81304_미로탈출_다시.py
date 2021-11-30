 # 다익스트라
# 32분까지 짰던 건 전 코드랑 다를 게 없음
# + 12분: 
# 수정해야 하는 상황: 인접리스트를 인접행렬로 바꾸고
# if문에서 전 노드도 trap이었으면 두 trap사이의 cost만 바꾸는걸로(이것땜에 인접행렬로 구현해야하는거임)

import heapq
INF = int(10e9)

def solution(n, start, end, roads, traps):

    graph = [ [INF]*(n+1) for _ in range(n+1)] # 1번부터 시작하니까
    r_graph = [ [INF]*(n+1) for _ in range(n+1)]

    for road in roads:
        graph[road[0]][road[1]] = road[2] #(cost,v2)
        r_graph[road[1]][road[0]] = road[2]
    #graph.sort() #꼭 정렬해야하나? 노 우선순위큐에 넣을거니까 상관없을듯
    #r_graph.sort()
    #print("graph=",graph)
    #print("r_graph=",r_graph)
    
    dist = [INF]*(n+1)
    dist[start]=0
    q = []
    heapq.heappush(q,(dist[start],start)) #q=[(0,start)]
    check = True # 전 노드가 ~trap이면 True 전 노드가 trap이면 false
    ref = graph

    while q:
        distance,now = heapq.heappop(q) 

        if check and not now in traps:          # ~trap -> ~trap | ref=graph라고 무조건 전 노드가 ~trap이라고 할 수 있을까?
            ref = graph     # 그대로 ref=graph
        elif check and now in traps:            # ~trap ->  trap | ref=graph라고 무조건 전 노드가 ~trap이라고 할 수 있을까?
            ref = r_graph 
            check = False       #전노드가 trap
        elif not check and now in traps:        # trap ->  trap
            ref = graph
        else:                                   # trap ->  ~trap
            print("else")

        for nxt in ref[now]: #nxt=(cost,v2)  비용순으로 정렬
            cost = distance+nxt[0]
            #start~nxt = start~now+now~nxt
            if cost<dist[nxt[1]]: #돌아가는 게 더 빠르면/(trap때문에 방문했던 노드 또 가도 상관없음)
                dist[nxt[1]]=cost
                heapq.heappush(q,(cost,nxt[1])) #q=[...,(distance,now),...]
    
    return 

print(solution( 3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))                  # 5
print(solution( 4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))    # 4