## 조건문 효율적으로 수정해서 다시짜기

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph = []
normal = [ [0]*N for _ in range(N) ] #R=0 G=1 B=2
colorBlind = [ [0]*N for _ in range(N) ] #R,G=0 B=2
visitedN = [ [False]*N for _ in range(N)]
visitedB = [ [False]*N for _ in range(N)]

for _ in range(N):
    graph.append(list(input().rstrip()))
#print(graph)

for i in range(N):
    for j in range(N):
        if graph[i][j]=='R':
            normal[i][j]=0
            colorBlind[i][j]=0
        elif graph[i][j]=='G':
            normal[i][j]=1
            colorBlind[i][j]=0
        elif graph[i][j]=='B':
            normal[i][j]=2
            colorBlind[i][j]=2
'''
for i in range(N):
    print(normal[i]) 

print("\n")
for i in range(N):
    print(colorBlind[i])
'''

def bfs(x,y,graph,visited,count): 
    color = graph[x][y]
    queue = deque()
    if visited[x][y]: 
        return color,count
    visited[x][y] = True
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        #print("now=",x,y)
        for (nx,ny) in (x,y+1),(x,y-1),(x+1,y),(x-1,y):     #동서남북
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny]==color and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    #print("queue=",queue)
    count += 1
    return color,count
                    

def countArea(graph,visited):
    color = -1
    cnt = 0
    for i in range(N):
        for j in range(N):

            #  """"같은"""" 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다.
            # 코드 너무 비효율적이야.. 더 명쾌하게 짜는법???
            # 문제를 잘 보거라..... 추가 조건이 있는 게 아니었어.. 이것땜에 2시간 헤맸음
            '''
            surroundColor = []
            for (ni,nj) in (i,j+1),(i,j-1),(i+1,j),(i-1,j): #동서남북
                if 0<=ni<N and 0<=nj<N:
                    surroundColor.append(graph[ni][nj])
            if len(surroundColor)==4:
                if surroundColor[0]==surroundColor[1] and surroundColor[1]==surroundColor[2] and surroundColor[2]==surroundColor[3]:
                    continue
            '''

            if not visited[i][j]: #graph[i][j]!=color or not visited[i][j]:라고 쓸 필요없음(근데 오히려 시간은 더 걸림)
                #print("visited=",visited)
                #print("(i,j)=",i,j)
                color,cnt = bfs(i,j,graph,visited,cnt)
                #print(cnt)
    return cnt

#print("normal")
answer1 = countArea(normal,visitedN)
#print("blind")
answer2 = countArea(colorBlind,visitedB)
print(answer1,answer2)

            
# 적록색약이 아닌 사람이 봤을 때와 
# 적록색약인 사람이 봤을 때의 함수 따로 구현해야하나? 코드 너무 길어지는 거 아닌가?
# "그래프"를 따로 구현하면 될듯

# 상하좌우가 다 같은 색이고 자기만 다른 색일 때 break or continue하는 문 추가해야할듯

