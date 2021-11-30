# 물이랑 고슴도치 큐를 따로 만드는 게 포인트
# 큐튜플에 temp도 넣어서 pop할때마다 temp가 기준점 넘으면 다시 넣고(왼쪽으로) break해서 while 큐 빠져나가는 게 포인트

import sys
from collections import deque
input = sys.stdin.readline
INF = int(10e9)

R,C = map(int,input().split()) #행,열

board = []
for _ in range(R):
    board.append(list(input().rstrip()))

waterList = []
for i in range(R):
    for j in range(C):
        if board[i][j]=='S':
            startX,startY = i,j
            board[i][j]=1
        elif board[i][j]=='D':
            destX,destY = i,j
            board[i][j]=1
        elif board[i][j]=='*':
            waterList.append((i,j))
            board[i][j]=-1
        
        if board[i][j]=='.':
            board[i][j]=0
        elif board[i][j]=='X': # 돌
            board[i][j]=-INF
'''
for i in range(R):
    print(board[i])
'''

def bfs(startX,startY,destX,destY,waterList):

    global board

    q_w = deque()
    q = deque()

    for i in range(len(waterList)):
        q_w.append((waterList[i][0],waterList[i][1],-1))
    q.append((startX,startY,1))

    cnt_w,cnt = -1,1
    
    while q:
        # 물
        while q_w:
            x_w,y_w,temp_w = q_w.popleft()
            if temp_w<cnt_w:
                q_w.appendleft((x_w,y_w,temp_w)) #다시넣고 다음 기준점 잡기
                cnt_w -= 1
                break
            for (nx_w,ny_w) in (x_w,y_w+1),(x_w,y_w-1),(x_w+1,y_w),(x_w-1,y_w): #동서남북
                if 0<=nx_w<R and 0<=ny_w<C:
                    if board[nx_w][ny_w]==0:
                        board[nx_w][ny_w] = board[x_w][y_w]-1
                        q_w.append((nx_w,ny_w,temp_w-1))
       
        #고슴도치
        while q:
            x,y,temp = q.popleft()
            if x==destX and y==destY:
                return board[x][y]

            if temp>cnt:
                q.appendleft((x,y,temp)) #다시넣고 다음 기준점 잡기
                cnt += 1
                break

            for (nx,ny) in (x,y+1),(x,y-1),(x+1,y),(x-1,y): #동서남북
                if 0<=nx<R and 0<=ny<C:
                    if board[nx][ny]<0: continue #물이 찰 예정인 칸으로 이동할 수 없다.
                    if board[nx][ny]==0 or (nx==destX and ny==destY):
                        board[nx][ny] = board[x][y]+1
                        q.append((nx,ny,temp+1))
            
        print("newboard")
        for i in range(R):
            for j in range(C):
                print(board[i][j], end=' ') if board[i][j]!=-INF else print("I",end=' ')
            print("\n")
            
    return "KAKTUS"
'''
print("newboard")
for i in range(R):
    for j in range(C):
        print(board[i][j], end=' ') if board[i][j]!=-INF else print("I",end=' ')
    print("\n")
'''

result = bfs(startX,startY,destX,destY,waterList)
if(type(result)==str):
    print(result)
else:
    print(result-1)



    