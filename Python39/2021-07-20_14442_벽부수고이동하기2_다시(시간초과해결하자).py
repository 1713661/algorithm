# 벽을 K개 까지 부수고 이동하여도 된다.
############ 벽도 visited 체크해야함!!!!!!!!

import sys
from collections import deque
input = sys.stdin.readline

N,M,K = map(int,input().split()) #세로의크기,가로의크기,부술수있는벽의개수

graph=[]
for _ in range(N):
    graph.append(list(map(int,input().rstrip())))

def bfs(x,y):
    visited = [ [[False]*(K+1) for _ in range(M)] for _ in range(N) ]
    distance = 0
    #print(visited)
    queue = deque()
    queue.append((x,y,0,0))
    while queue:
        x,y,crashed,distance = queue.popleft()
        #print("now=",x,y,"crashed=",crashed)
        #print("queueeue=",queue)
        if x==N-1 and y==M-1:
            return distance+1
        for (nx,ny) in (x,y+1),(x,y-1),(x+1,y),(x-1,y): # 동서남북
            if nx<0 or nx>=N or ny<0 or ny>=M:  # 범위를 벗어나면
                continue
            if graph[nx][ny]==0 and not visited[nx][ny][crashed]: # 갈수 있는 칸이고 벽K번부순상태(crashed)로는아직 방문하지 않은 칸이면
                visited[nx][ny][crashed]=True
                #(x,y)와 같은 상태 넣어줘야함
                queue.append((nx,ny,crashed,distance+1)) #distance 배열 대신 큐에 저장
            elif graph[nx][ny]==1 and crashed<K and not visited[nx][ny][crashed+1]: ####### 벽도 visited 체크해야함!!!!!!!!
                visited[nx][ny][crashed+1]=True
                queue.append((nx,ny,crashed+1,distance+1))
        #print("afterfor=",queue)
    return -1



print(bfs(0,0))