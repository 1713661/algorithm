# 배양액은 매 초마다 이전에 배양액이 도달한 적이 없는 인접한 땅으로 퍼져간다.
# 하얀색 칸은 배양액을 뿌릴 수 없는 땅을, 황토색 칸은 배양액을 뿌릴 수 있는 땅을, 하늘색 칸은 호수를 의미한다.
# 초록색 배양액과 빨간색 배양액이 동일한 시간에 도달한 땅에서는 두 배양액이 합쳐져서 꽃이 피어난다. 
# 꽃이 피어난 땅에서는 배양액이 사라지기 때문에 더 이상 인접한 땅으로 배양액을 퍼트리지 않는다.

# 모든 배양액을 남김없이 사용해야 한다. 

# 피울 수 있는 꽃의 최대 개수

# 0은 호수, 1은 배양액을 뿌릴 수 없는 땅, 2는 배양액을 뿌릴 수 있는 땅

# 45분 악! while q문 또 잘못 짠 것 같아.. 그냥 greens reds 따로 돌리면 되는거 아닌가?
# +22분

import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N,M,G,R = map(int,input().split()) #2<=행,열<=50 1 ≤ G ≤ 5 1 ≤ R ≤ 5
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
'''
for i in range(N):
    print(board[i])
'''
startPoints=[] #10개 이하
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
    '''
    [1, 0, 1, 3, 1, 3, 1]
    [1, 1, 1, 0, 1, 0, 3]
    [-3, 1, 0, 0, 1, 1, 1]
    [1, 0, -3, 1, 2, 1, 0]
    [0, 2, 1, 1, 0, 1, 2]
    '''
    
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
                        if (board[nx][ny]-1+cnt)==0:
                            board[nx][ny]=0
                            answer += 1
                    elif cnt<=-3:
                        if (board[nx][ny]+1+cnt)==0:
                            board[nx][ny]=0
                            answer += 1
                    
    '''        
    if answer==7:
        print("after")
        for i in range(N):
            print(board[i])
    
    print(answer)
    '''
    return answer

answer = 0
for starts in combinations(startPoints,G+R):
    for greens in combinations(starts,G):
        reds = list(set(starts)-set(greens))
        newboard = [board[i][:] for i in range(N)] 
        #print(starts) # ((0, 3), (0, 5), (1, 6), (2, 0), (4, 6))
        #print(greens) # ((0, 3), (1, 6), (2, 0))
        #print(reds) # {(3, 2), (2, 0)}
        for green in greens:
            newboard[green[0]][green[1]]=3
        for red in reds:
            newboard[red[0]][red[1]]=-3
        '''
        [1, 0, 1, 3, 1, 3, 1]
        [1, 1, 1, 0, 1, 0, 3]
        [-3, 1, 0, 0, 1, 1, 1]
        [1, 0, -3, 1, 2, 1, 0]
        [0, 2, 1, 1, 0, 1, 2]
        '''
        answer = max(answer,bfs(newboard,greens,reds))
print(answer)
        



        


