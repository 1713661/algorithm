# 40분

import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N,M,G,R = map(int,input().split()) #2<=행,열<=50 1<=초록배양액개수,빨간배양액개수<=5

board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

# 0은 호수, 1은 배양액을 뿌릴 수 없는 땅, 2는 배양액을 뿌릴 수 있는 땅
startPoints = []
for i in range(N):
    for j in range(M):
        if board[i][j]==2:
            startPoints.append((i,j))

def bfs(board,greens,reds):

    def OOB(x,y):
        return x<0 or x>=N or y<0 or y>=M

    q1 = deque() #초록
    q2 = deque() #빨강

    for green in greens:
        q1.append( (green[0],green[1],3) )
        board[green[0]][green[1]]=0

    for red in reds:
        q2.append( (red[0],red[1],-3) )
        board[red[0]][red[1]]=0
    
    pt1,pt2 = [],[]
    gcur,rcur = 3,-3
    answer = 0

    for i in range(N):
        print(board[i])
    print('\n')

    while sum([sum(board[i]) for i in range(N)])!=0: ### 이것도 sum 계산 엄청 오래걸릴걸.. 무엇보다도 내가 짠 코드가 board 다 0으로 만들지도 않음

        # q에서는 아직 board값 갱신하지 않음
        while q1:
            gx,gy,gtmp = q1.popleft()
            print("gcur=",gcur)
            while len(q1)>0 and gtmp<gcur: ##### 여기 while문이랑 if문 이 문제에서는 쓰면 안됨
                gx,gy,gtmp = q1.popleft()
            if gtmp>gcur:
                q1.appendleft((gx,gy,gtmp))
                gcur += 1
                break
            for (ngx,ngy) in (gx,gy+1),(gx,gy-1),(gx+1,gy),(gx-1,gy): # 동서남북
                if OOB(ngx,ngy): continue
                if board[ngx][ngy]==1 or board[ngx][ngy]==2:
                    q1.append((ngx,ngy,gtmp+1))
            print("afterq1=",q1)

        while q2:
            rx,ry,rtmp = q2.popleft()
            while len(q2)>0 and rtmp>rcur:
                rx,ry,rtmp = q2.popleft()
            if rtmp<rcur:
                q2.appendleft((rx,ry,rtmp))
                rcur -= 1
                break
            for (nrx,nry) in (rx,ry+1),(rx,ry-1),(rx+1,ry),(rx-1,ry): # 동서남북
                if OOB(nrx,nry): continue
                if board[nrx][nry]==1 or board[nrx][nry]==2:
                    q2.append((nrx,nry,rtmp-1))
            print("afterq2=",q2)

        # q1, q2에 좌표 중복해서 들어갈 수 있음 초록배양액,빨간배양액 둘 다 여러점에서 시작할 수 있기 때문
        for pt1 in q1:
            for pt2 in q2:
                if pt1[0]==pt2[0] and pt1[1]==pt2[1] and pt1[2]+pt2[2]==0:
                    board[pt1[0]][pt1[1]]=0
                    answer += 1
    
        for i in range(N):
            print(board[i])
        print('\n')

    return answer

answer = 0
for starts in combinations(startPoints,G+R):
    for greens in combinations(starts,G):
        reds = list(set(starts)-set(greens)) # 꼭 set으로만 했어야하나? 아 차집합으로 빼주는 건 집합밖에 못하니까 바보야..
        newboard = [board[i][:] for i in range(N)]
        for green in greens:
            newboard[green[0]][green[1]] = 3
        for red in reds:
            newboard[red[0]][red[1]] = 3
        answer = max(answer,bfs(newboard,greens,reds))

print(answer)




