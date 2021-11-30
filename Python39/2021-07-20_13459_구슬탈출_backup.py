# 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.
# 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다.
# 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 


# 10번 이하로 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램
# 빼낼 수 있으면 1을 없으면 0을 출력

import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split()) #세로,가로

graph=[]
for _ in range(N):
    graph.append(list(input().rstrip()))
print(graph)

for i in range(N):
    for j in range(M):
        if graph[i][j]=='#':
            graph[i][j]=0       # 벽=0
        elif graph[i][j]=='.':
            graph[i][j]=1       # 빈칸=1
        elif graph[i][j]=='R':
            rx,ry=i,j
        elif graph[i][j]=='B':
            bx,by=i,j
        elif graph[i][j]=='O':
            ox,oy=i,j
print(graph)
print(rx,ry,bx,by,ox,oy)

def move(dx,dy):
    while graph[newrx][newry]==1: #기울인 방향에 빈칸이 있으면
        newrx = newrx + dx
        newry = newry + dy
        return newrx,newry

def bfs(rx,ry,bx,by,ox,oy):
    print(rx,ry,bx,by,ox,oy)
    queueRed = deque()
    queueBlue = deque()
    queueRed.append((rx,ry))
    queueRed.append((bx,by))

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for _ in range(1):#while queueRed: #???조건 다시 확인
        for dir in range(4): #동서남북
            newrx = rx + dx[dir]
            newry = ry + dy[dir]
            #print("newrx,newry=",newrx,newry,"graph[newrx][newry]=",graph[newrx][newry])
            if graph[newrx][newry]==1:
                move(dx[dir],dy[dir])
            while graph[newrx][newry]==1: #기울인 방향에 빈칸이 있으면
                newrx = newrx + dx[i]
                newry = newry + dy[i]
                print("(rx,ry)=",newrx,newry)
        
            '''
            if graph[nx][ny]==0: #기울인 방향에 벽이 있으면
                continue
            if graph[nx][ny]==1: #기울인 방향에 빈칸이 있으면
                rx,ry=nx,ny
                '''
                
bfs(rx,ry,bx,by,ox,oy)



