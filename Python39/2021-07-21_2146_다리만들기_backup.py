import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

def indexing(x,y,cnt):
    global graph,isEdge
    graph[x][y]=cnt
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        if graph[x][y]==1:
            graph[x][y]=cnt
        for (nx,ny) in (x,y+1),(x,y-1),(x+1,y),(x-1,y): #동서남북
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny]==1:
                    queue.append((nx,ny))
                elif graph[nx][ny]==0:
                    isEdge[x][y]=True
    return

def bfs(x,y):
    global graph,isEdge
    idx = graph[x][y]
    visited = [ [False]*N for _ in range(N)]
    queue = deque()
    queue.append((x,y,-1))
    
    while queue:
        x,y,distance= queue.popleft()
        visited[x][y]=True
        if isEdge[x][y] and graph[x][y]!=idx:
            return distance
        for (nx,ny) in (x,y+1),(x,y-1),(x+1,y),(x-1,y): #동서남북
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]: #다음칸이 바다면
                if graph[nx][ny]!=idx: ####################
                    queue.append((nx,ny,distance+1))


dist = [ [-1]*N for _ in range(N)]
isEdge = [ [False]*N for _ in range(N)]
cnt = -1
for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            indexing(i,j,cnt)
            cnt -= 1

answers = []
for i in range(N):
    for j in range(N):
        if isEdge[i][j]:
            answer = bfs(i,j)
            if answer!=None:
                answers.append(answer)
answers.sort()
print(answers[0])
                    
                
                    
