# 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 
# 이코테 10.그래프이론까지 공부한 다음에 풀어야할듯(사이클때문에)
# BFS로 풀면 최단거리 못잡아내기 때문에 안됨!!
##### 물론 BFS는 너비 우선 탐색이기 때문에 종료조건에서 리턴하는 값은 최솟값이 맞지만(BFS 기본개념)
##### 그 최솟값과 같은 값을 갖는 경로가 꼭 최단경로는 아니기 때문에 dist배열 꼭 만들어야함!!!

# ########## 풀이1 BFS : dist배열에 최단거리 저장(visited대신 dist!!!!!!!!!!!!!!!!!)
# 풀이2 다익스트라: 최단거리테이블 (근데 간선 cost 다 1이기 때문에 다익스트라 쓸 필요없는듯)
# 21분

import sys
import heapq
input = sys.stdin.readline
INF = int(10e9)

def solution(n, edge): #다익스트라
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    #print(graph)
    
    # 다익스트라
    start=1
    dist = [ INF for _ in range(n+1)]
    dist[start]=0
    q = []
    heapq.heappush(q,(start,0))

    answer = 0
    while q:
        now,distance = heapq.heappop(q)
        for next in graph[now]:
            cost = distance+1 
            if cost<dist[next]:
                dist[next]=cost
                heapq.heappush(q,(next,cost))

    #print("dist=",dist)
    list = [item for item in dist if item<INF]
    list.sort(reverse=True)
    #print("list=",list)
    answer = list.count(list[0]) # 파이썬 라이브러리 잘 쓸 수 있도록 복습!!!
    '''
    idx=list[0]
    for l in list:
        if l==idx:
            answer += 1
    '''

    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
print(solution(11, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [3, 6], [4, 8], [4, 9], [5, 9], [5, 10], [6, 10], [6, 11]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(2, [[1, 2]]))
print(solution(5, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]))
print(solution(4, [[1, 4], [1, 3], [2, 3], [2, 1]]))
print(solution(4, [[3, 4], [1, 3], [2, 3], [2, 1]]))
print(solution(4, [[4, 3], [1, 3], [2, 3]]))