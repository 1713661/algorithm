# 인접리스트말고 인접행렬(모든 정보 다 저장하는)로 만들어야할듯
# 방향 바뀌는거 구현해야 하니까
# 처음부터 r_graph만들어서 graph vs r_graph 중 뭐 참조할지 정하면 되는 거 아닌가(문제 잘못 봐서 다른길로가서 시간버리면 안된다)
# #################### (문제잘읽자) 이동한 함정과 "연결된" 모든 화살표의 방향이 바뀝니다. (모든 그래프의 간선이 바뀌는 게 아님!!!!)
# 근데 다시 돌아갔어도 처음부터 이 문제 파악하기는 힘들었을 것 같다. 

# 서로 다른 두 방 사이에 직접 연결된 길이 여러 개 존재할 수도 있습니다.

# 20분(일단 짜고 처음 컴파일함) 
# +22분 print문 찍으면서 코드어떻게 잘못생각했는지 확인
# +9분 최단거리테이블 초기화하고 코드 다듬고 제출(첫번째시도)
# +8분 (문제 바르게 이해하고 다시 알고리즘 구상하기)

# 꼭 4가지 경우로 나눠야하나..

import heapq
INF = int(10e9)

def solution(n, start, end, roads, traps):

    graph = [[] for _ in range(n+1)] # 1번부터 시작하니까
    r_graph = [[] for _ in range(n+1)]

    for road in roads:
        # if road[0] in traps:
        graph[road[0]].append((road[1],road[2]))    #graph[u].append((v,c))
        r_graph[road[1]].append((road[0],road[2]))  #graph[v].append((u,c))
    
    #print("graph=",graph)
    #print("r_graph=",r_graph)

    dist = [INF]*(n+1)
    dist[start]=0
    q = []
    heapq.heappush(q,(dist[start],start))
    ref = graph
    check = True # ref = graph면 True ref = r_graph면 false

    while q:
        distance, now = heapq.heappop(q)
        print("now=",now,"queue=",q)

        ##########################
        if now in traps and check:
            ref = r_graph
            #print("r_graph[now]=",ref[now])
            check = False
            #traps.remove(now) # 똑같은 함정 방을 두 번째 방문하게 되면 원래 방향의 길로 돌아옵니다. 즉, 여러 번 방문하여 계속 길의 방향을 반대로 뒤집을 수 있습니다.
            dist[now]=INF ################ 최단거리 테이블 초기화
        elif now in traps and not check:
            ref = graph
            print("graph[now]=",ref[now])
            check = True
            #traps.remove(now)

        for next in ref[now]:
            cost = distance + next[1] ###############
            if cost<dist[next[0]]: ########################### trap때문에 돌아가는경우 if문 만족못함
                dist[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))
                #print("q=",q)
    
    #print("dist=",dist)
    return dist[end]

print(solution( 3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))                  # 5
print(solution( 4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))    # 4