# 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 
# 이게 힌트였을 것 같음.. 다익스트라 한번 실행하는걸로는 절대 못푼다는걸..

# start,v1,v2에 대하여 다익스트라 돌리면 됨!!!!!!!!!!!!!!!!
# 왜 다익스트라 한번 돌리는걸로 다 끝내려고 했을까? 
# 다익스트라 돌아가는 원리 아직도 완전히 이해하지 못한듯(거리가짧은애들부터꺼내서 최단거리테이블갱신)

# 32분
# 일단 테스트케이스 돌리면서 알고리즘 찾아야할듯... 
# 테스트케이스 안보면서 알고리즘 짜기에는 내 머리가 안돌아가..
# 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 


# 파이썬 랭킹1위코드 주석(다익스트라 최소로 돌리는 방법)
# 여기서 엄청난 발견이 있다. 1 -> v_1 -> v_2 -> v와 1 -> v_2 -> v_1 -> v중에서 더 작은 것을 골라야 되는데
# 방향이 없는 그래프이기에, 1 -> v_1과 v_1 -> 1이 같다. 다른 간선들도 모두 마찬가지다.
# 그래서 dijkstra를 최소한으로 돌리기 위해서는, 시작 노드의 수를 최대한 줄이는 것이 좋다.
# 그래서 v_1 -> 1, v_1 -> v_2, v_1 -> v를 한방에 구하고
# 마찬가지로 v_2 -> 1, v_2 -> v를 한방에 구하는 것이다.
import sys
import heapq
input = sys.stdin.readline
INF = int(10e9)

N,E = map(int,input().split()) #정점,간선의개수 2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000

graph=[ [] for _ in range(N+1) ]
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c)) #(노드,거리)
    graph[b].append((a,c)) ############양방향노드니까?

v1,v2 = map(int,input().split())
#반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1)

def dijkstra(start,*end):
    q = []
    dist = [INF]*(N+1)
    dist[start]=0
    heapq.heappush(q,(0,start)) #(거리,노드) 거리가 앞에오게 튜플 만들어야함!!!!!!!!!!!!!
    while q:
        distance,now = heapq.heappop(q) #distance(start~now)
        for next in graph[now]: #next[0]=노드, next[1]=거리(now~next)
            cost = distance + next[1]
            #start~next = start~now + now~next
            if cost<dist[next[0]]: #now거쳐서 가는 게 더 빠른 경우
                dist[next[0]]=cost
                heapq.heappush(q,(cost,next[0]))
    return tuple([dist[e] for e in end])

v1_1, v1_v2, v1_N = dijkstra(v1,1,v2,N) # 다익스트라 최소한으로 호출
v2_N, v2_1 = dijkstra(v2,N,1)
answer = min(v1_1+v1_v2+v2_N, v2_1+v1_v2+v1_N)
print(answer) if answer<=int(2e8) else print(-1) # 문제조건에 맞게 조건 붙여야함!!!
