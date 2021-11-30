import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N,M,G,R = map(int,input().split()) #2<=행,열<=50 1 ≤ G ≤ 5 1 ≤ R ≤ 5
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

startPoints=[] # 10개 이하
for i in range(N):
    for j in range(M):
        if board[i][j]==2:
            startPoints.append((i,j))

def bfs(board,greens,reds):
    answer = 0
    q = deque()
    for green in greens:
        q.append((green[0],green[1],3))
    for red in reds:
        q.append((red[0],red[1],-3))
    
    while q:
        x,y,cnt = q.popleft()
        for (nx,ny) in (x,y+1),(x,y-1),(x+1,y),(x-1,y): # 동서남북
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny]==1 or board[nx][ny]==2:
                    if cnt>=3:
                        board[nx][ny] = cnt+1
                        q.append((nx,ny,cnt+1))
                    elif cnt<=-3:
                        board[nx][ny] = cnt-1
                        q.append((nx,ny,cnt-1))
                else:#elif (board[nx][ny]+cnt)==0:
                    if cnt>=3:
                        ####### 첫번째 예시부터 문제
                        ####### -3이 4를 잡아먹어야 하는데 그러지 못함. 고로 이렇게 짜는 게 아님!
                        ##### 바킹독님은 백트래킹으로 풀어야한다고 그랬는데 백트래킹 안쓰고는 못푸나?
                        if (board[nx][ny]-1+cnt)==0: 
                            board[nx][ny]=0
                            answer += 1
                    elif cnt<=-3:
                        if (board[nx][ny]+1+cnt)==0:
                            board[nx][ny]=0
                            answer += 1

    for i in range(N):
        print(board[i])
    print("\n")
                
    return answer

answer = 0
for starts in combinations(startPoints,G+R):
    for greens in combinations(starts,G):
        reds = list(set(starts)-set(greens))
        newboard = [board[i][:] for i in range(N)] 

        for green in greens:
            newboard[green[0]][green[1]]=3
        for red in reds:
            newboard[red[0]][red[1]]=-3
        
        answer = max(answer,bfs(newboard,greens,reds))
print(answer)