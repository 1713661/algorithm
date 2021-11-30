import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))
#print(graph)
#print(graph[0][0])
#print(graph[0])
# 이동할 네 방향 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1
                #print(graph[nx][ny])
                #print('dir='+str(i),'(',nx,',',ny,')')
                queue.append((nx,ny))
       #print(queue)
    return graph[n-1][m-1]
print(bfs(0,0))

