import sys
from collections import deque
input = sys.stdin.readline

# 구멍에 빠지면 그 구멍 좌표 리턴
def tilt(rx,ry,bx,by,dx,dy):
    global board
    rc,bc = 0,0
    while board[rx+dx][ry+dy]==0:
        rx += dx
        ry += dy
        rc += 1
        if rx==ox and ry==oy:
            break
    while board[bx+dx][by+dy]==0:
        bx += dx
        by += dy
        bc += 1
        if bx==ox and by==oy:
            break
    return rx,ry,bx,by,rc,bc

def bfs(rx,ry,bx,by):
    global board
    queue = deque()
    queue.append((rx,ry,bx,by,0))
    visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)] #### 4차원 배열 써야함!!!
    visited[rx][ry][bx][by]=True

    while queue:
        rx,ry,bx,by,cnt = queue.popleft()

        if cnt>10: 
            return 0
        if bx==ox and by==oy: continue

        if rx==ox and ry==oy: # 파란구슬은 안빠지고 빨간구슬만 빠진 경우
            return 1

        for (dx,dy) in (0,1),(0,-1),(1,0),(-1,0): #동서남북

            if board[rx+dx][ry+dy]==0 or board[bx+dx][by+dy]==0: ########################### 하나라도 갈 수 있으면 ok!!!!
                newrx,newry,newbx,newby,rc,bc = tilt(rx,ry,bx,by,dx,dy)

                # 보정
                if newrx==newbx and newry==newby:
                    #동시에 구멍에 빠지면 continue(return -1하면 안돼!!!!!!!!!! 이 길이 아니었던거고, 다른길중에 가능한길이있을수있기때문)(bfs)
                    if newrx==ox and newry==oy: continue 
                    if rc>bc:
                        newrx -= dx
                        newry -= dy
                    else: #bc>rc
                        newbx -= dx
                        newby -= dy

                if not visited[newrx][newry][newbx][newby]: # 둘다 방문한 적 있어야 이전에 해봤던 시도인듯? 그리고 4차원 배열로 구현해야함
                    visited[newrx][newry][newbx][newby]=True

                    queue.append((newrx,newry,newbx,newby,cnt+1))
    return 0
    

N,M = map(int,input().split()) #세로,가로

board = []
for _ in range(N):
    board.append(list(input().rstrip()))

for i in range(N):
    for j in range(M):
        if board[i][j]=='R':
            rx,ry = i,j
        if board[i][j]=='B':
            bx,by = i,j
        if board[i][j]=='O':
            ox,oy = i,j

        if board[i][j]=='#':
            board[i][j]=-1 #벽
        else:
            board[i][j]=0 #빈공간 R,O,B도 여기에포함

print(bfs(rx,ry,bx,by))