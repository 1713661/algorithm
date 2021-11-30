# L=육지 W=바다
# 보물은 '서로 간에 최단 거리로 이동하는데 있어'??? 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다.
# 최대 거리 출력하면 될듯???
# visited 배열말고 dist배열 만들어야함!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
# 시작점 걸러내는 건 시간초과나는듯 -> 1로 맞추고 마지막에 1빼기
# 그냥 언어 pypy로 바꿨음!
# 점마다 dx,dy,dist 새로 선언해서 메모리 많이잡아먹는듯

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split()) #세로의크기, 가로의크기
graph = []
for _ in range(N):
    graph.append(list(map(str,input().rstrip()))) # 공백없는경우 split()함수 소용없음!!!
#print(graph)
#print(dist)

# 최댓값만 리턴하기
# dist[x][y]는 최대값일 아닐 수 있음 max() 함수 써야함!!!
def bfs(x,y):
    MAX = 0
    dx = [0,0,1,-1] # 동서남북
    dy = [1,-1,0,0]
    dist[x][y]=1
    queue = deque()
    queue.append((x,y))
    #print(queue)
    while queue:
        x,y = queue.popleft()
        #print("now=",x,y)
        for i in range(4): # 동서남북 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            #print("startX,startY=",startX,startY)
            #print("nx,ny=",nx,ny)
            if graph[nx][ny]=='L' and dist[nx][ny]==0: #(nx,ny)가 방문하지 않은 좌표이면
                queue.append((nx,ny))
                #print(queue)
                dist[nx][ny] = dist[x][y]+1
                MAX = max(MAX, dist[nx][ny])
    return MAX-1


answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j]=='L':
            dist = [ [0]*M for _ in range(N) ] #각 섬 방문했는지
            #print("dist 초기화=",dist)
            distance = bfs(i,j)
            #print("distance=",distance)
            #print("bfs한 후 dist 배열=",dist)
            if answer<distance:
                answer = distance
                #print("answer=",answer)

print(answer)
