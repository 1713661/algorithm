
# +17분
# for문에서 바로 큐에 넣으면 안됨(꽃이필좌표는 빼줘야하기 때문)
# 그래서 cand에 넣고 두 while q문 다음에 집합으로 처리해줘야하는거임
# 3055 탈출은 물 먼저 가고 그 담에 고슴도치가 가는거기 때문에
# 동시에 도착하는 점을 고려할 필요가 없었음
# 또한 고슴도치는 하나밖에 없기 때문에 q에 중복좌표 들어갈 일도 없었음
###### 아 그냥 두 문제 비교하지 말고 양치기 하는 게 답인듯

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
        q1.append( (green[0],green[1]) )
        board[green[0]][green[1]]=3

    for red in reds:
        q2.append( (red[0],red[1]) )
        board[red[0]][red[1]]=-3

    answer = 0

    while q1:

        gcand = set()
        rcand = set()

        # q에서는 아직 board값 갱신하지 않음
        while q1:
            gx,gy = q1.popleft()
            for (ngx,ngy) in (gx,gy+1),(gx,gy-1),(gx+1,gy),(gx-1,gy): # 동서남북
                if OOB(ngx,ngy): continue
                if board[ngx][ngy]==1 or board[ngx][ngy]==2:
                    gcand.add((ngx,ngy))

        while q2:
            rx,ry = q2.popleft()
            for (nrx,nry) in (rx,ry+1),(rx,ry-1),(rx+1,ry),(rx-1,ry): # 동서남북
                if OOB(nrx,nry): continue
                if board[nrx][nry]==1 or board[nrx][nry]==2:
                    rcand.add((nrx,nry))

        flower = gcand&rcand
        gcand = gcand-flower
        rcand = rcand-flower

        for f in flower:
            board[f[0]][f[1]]='f'
            answer += 1
        for row, col in gcand:
            board[row][col] = 3
        for row, col in rcand:
            board[row][col] = -3
        q1.extend(gcand)
        q2.extend(rcand)
        '''
        for i in range(N):
            print(board[i])
        '''

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