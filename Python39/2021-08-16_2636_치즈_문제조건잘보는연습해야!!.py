# 처음에(0,0)으로 시작해서 1을 찾으면 구멍제외한 가장자리찾을수있음!!!!!! 하......토마토랑 다르게 푸는거였음...
# 궁극적인 알고리즘을 생각하는 것이 중요!!
# 코더가 되지 말고 프로그래머가 되자!!

import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int,input().split()) #가로,세로

board = []
for _ in range(M):
    board.append(list(map(int,input().split())))

def oneHourLater(x,y):
    q = deque()
    q.append((x,y))

    visited = [[False]*N for _ in range(M)] #-1로 값바꾸는것보다 visited쓰는게 나음(-1로 바꾸면 나중에 값 다시바꿔야하니까)
    visited[x][y]=True

    while q:
        x,y = q.popleft()
        for (nx,ny) in (x,y+1),(x,y-1),(x+1,y),(x-1,y): #동서남북
            if 0<=nx<M and 0<=ny<N and not visited[nx][ny]:
                visited[nx][ny]=True
                if board[nx][ny]==0:
                    q.append((nx,ny))
                if board[nx][ny]==1:
                    board[nx][ny] = 0

    return board


newboard = board
cnt = 0
prev_cheese = 0
cheese = 0

while True:

    for i in range(M):
        for j in range(N):
            if newboard[i][j]==1:
                cheese += 1
    if cheese==0: break

    newboard = oneHourLater(0,0)
    for i in range(M):
        print(newboard[i])

    cnt += 1
    prev_cheese = cheese
    cheese = 0 #초기화
    
print(cnt)
print(prev_cheese)

# 이런거 짤필요없음
'''
def isEmpty(board):
    for i in range(M):
        for j in range(N):
            if newboard[i][j]==1:
                return False
    return True

if isEmpty(board):
    print(0)
    print(0)
else:     
    while True:
        newboard = oneHourLater(0,0)

        for i in range(M):
            print(newboard[i])

        for i in range(M):
            for j in range(N):
                if newboard[i][j]==1:
                    cheese += 1
        cnt += 1
        if cheese==0: break

        prev_cheese = cheese
        cheese = 0 #초기화
    print(cnt)
    print(prev_cheese)
'''   