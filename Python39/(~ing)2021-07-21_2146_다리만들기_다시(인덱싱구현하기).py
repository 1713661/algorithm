# 1시간 23분 메모리초과
# 30분 dist배열 전역으로 선언하고 dist[nx][ny]>=dist[x][y]+1해서 거르려고 했으나 실패.. 천천히보자!!
# barkingdog님처럼 시간,공간복잡도 생각하면서 구상한다음, 그 다음에 코드 짜야겠다
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
    print("i,j=",x,y)
    global graph,isEdge,dist
    idx = graph[x][y]
    queue = deque()
    queue.append((x,y,-1))
    
    while queue:
        x,y,distance = queue.popleft()
        #print("x,y,distance=",x,y,distance)
        #print("x,y=",x,y,"isEdge=",isEdge[x][y],"graph[x][y]=",graph[x][y],"idx=",idx)
        if isEdge[x][y] and graph[x][y]!=idx:
            print("hi")
            print("x,y=",x,y,"isEdge=",isEdge[x][y],"graph[x][y]=",graph[x][y],"idx=",idx,"distance=",distance,"dist[x][y]=",dist[x][y])
            return x,y,distance
        for (nx,ny) in (x,y+1),(x,y-1),(x+1,y),(x-1,y): #동서남북
            if 0<=nx<N and 0<=ny<N and graph[nx][ny]!=idx: ####################
                queue.append((nx,ny,distance+1))
    return -1,-1,0

isEdge = [ [False]*N for _ in range(N)]
cnt = -1
for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            indexing(i,j,cnt)
            cnt -= 1

print("graph")
for i in range(N):
    print(graph[i])

'''
print("isEdge")
for i in range(N):
    for j in range(N):
        if isEdge[i][j]:
            print("E",end=" ")
        else:
            print(".",end=" ")
    print("\n")
'''

'''
#visited = [ [False]*N for _ in range(N)]
answers = []
for i in range(N):
    for j in range(N):
        if isEdge[i][j]:
            #print("i,j=",i,j)
            answer = bfs(i,j)
            #print("answer=",answer)
            if answer!=None:
                answers.append(answer)
answers.sort()
#print(answers)
print(answers[0])

dist = [ [INF]*N for _ in range(N)]
#print(min(bfs(i,j) for j in range(N) for i in range(N) if isEdge[i][j]))
'''
dist = [ [2*N]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if isEdge[i][j]:
            x,y,distance = bfs(i,j)
            if x==-1 and y==-1: #다리 놓을 방법 없다는거니까
                continue
            print("newx,newy=",x,y,"distance=",distance)
            dist[x][y] = min(dist[x][y],distance)

answer=int(10e9)
for i in range(N):
    for j in range(N):
        if dist[i][j]==-1:
            continue
        answer = min(answer,dist[i][j])
print(answer)








                    
                
                    
