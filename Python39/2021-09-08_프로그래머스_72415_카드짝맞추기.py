# 11분 첨에 cards받는거 괜히 코드 줄이려다가 시간낭비함
# 27분 bfs 템플릿 대충 짜고 ctrl함수 구현시작
# 41분 ctrl함수 작은 예시에서 돌려봄 
# 53분 ctrl함수 예외처리 다 된 것 같다고 생각해서 for문 다시 구현 시작
# 58분 isPair추가
# 66분 포기...
# 82분 visited해야할것같아서 했는데 생각해보니 안해도 될듯

############ 아 bfs를 order에 대해 돌리는 게 아니라 같은 짝 카드 찾기에 대해 찾는것!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# [Ctrl] 키를 누른 상태에서 방향키 ←, ↑, ↓, → 중 하나를 누르면, 
# 누른 키 방향에 있는 가장 가까운 카드로 한번에 이동합니다.
# 만약, 해당 방향에 카드가 하나도 없다면 그 방향의 가장 마지막 칸으로 이동합니다.
# 만약, 누른 키 방향으로 이동 가능한 카드 또는 '빈 공간이 없어' 이동할 수 없다면 
# 커서는 움직이지 않습니다.
# (같은 그림이 아니라면 원래 상태로 뒷면이 보이도록 뒤집힙니다.) -> 같은 그림이 아니라면 커서는 움직일수 없다
# 모든 카드 다 뒤집어야 하니까 엔터는 2*MAX임

from itertools import permutations
from collections import deque

def solution(board, r, c): # 커서의 처음위치(r,c)
    #cards = [board[i][j] if board[i][j]!=0 else: continue for i in range(4) for j in range(4)]
    #cards = list(filter(lambda x:x!=0, line for line in board))
    cards = set()
    for i in range(4):
        for j in range(4):
            if board[i][j]==0: continue
            cards.add(board[i][j])
    dx = [0,0,1,-1] # 동서남북
    dy = [1,-1,0,0]

    # 만약, 해당 방향에 카드가 하나도 없다면 그 방향의 가장 마지막 칸으로 이동합니다.
    # 만약, 누른 키 방향으로 이동 가능한 카드 또는 '빈 공간이 없어' 이동할 수 없다면 
    # 커서는 움직이지 않습니다.

    def ctrl(x,y,dir,card):
        while 0<=x+dx[dir]<4 and 0<=y+dy[dir]<4 and (board[x+dx[dir]][y+dy[dir]]==0 or board[x+dx[dir]][y+dy[dir]]==card):
            x += dx[dir]
            y += dy[dir]
            if board[x][y]==card:
                break
        return x,y

    answers = set()
    for order in permutations(cards,len(cards)): 
        # order = (1, 2, 3)
        q = deque()
        q.append((r,c,0,False,0))
        visited = [(r,c,False,0)]
        while q:

            x,y,cnt,shouldfindFirst,idx = q.popleft()
            #print("now=",x,y,"count=",cnt,"idx=",idx,"should=",shouldfindFirst)#,"visited=",visited)

            if idx==len(order)-1 and shouldfindFirst==True:
                answers.add(cnt)
                break
            
            ### 아마 내 코드는 
            
            for dir in range(4):
                nx = x+dx[dir]
                ny = y+dy[dir]
                if 0<=nx<4 and 0<=ny<4 and idx<len(order):
                    if not shouldfindFirst: #오른쪽카드찾아야하는거면
                        if board[nx][ny]==0: #그냥방향키, ctrl+방향키 둘다구현해야함
                            if not (nx,ny,shouldfindFirst,cnt+1) in visited:
                                visited.append((nx,ny,shouldfindFirst,cnt+1))
                                q.append((nx,ny,cnt+1,shouldfindFirst,idx))
                            nnx,nny = ctrl(x,y,dir,order[idx])###q.append() ctrl결과 좌표값도 큐에 넣기 ctrl(x,y,dir)
                            if not (nnx,nny,shouldfindFirst,cnt+1) in visited:
                                visited.append((nnx,nny,shouldfindFirst,cnt+1))
                                if board[nnx][nny]==order[idx]: 
                                    shouldfindFirst = True
                                    q.append((nnx,nny,cnt+1,shouldfindFirst,idx+1))
                                else:
                                    q.append((nnx,nny,cnt+1,shouldfindFirst,idx))
                        elif board[nx][ny]==order[idx]: #내가찾는카드가 있었으면
                            if not (nx,ny,shouldfindFirst,cnt+1) in visited:
                                visited.append((nx,ny,shouldfindFirst,cnt+1))
                                shouldfindFirst = True
                                q.append((nx,ny,cnt+1,shouldfindFirst,idx+1))
                    
                    else: #왼쪽카드찾아야하는거면
                        #print("idx=",idx,"now=",nx,ny)
                        if board[nx][ny]==0: 
                            if not (nx,ny,shouldfindFirst) in visited:
                                visited.append((nx,ny,shouldfindFirst))
                                q.append((nx,ny,cnt+1,shouldfindFirst,idx))
                            nnx,nny = ctrl(x,y,dir,order[idx])
                            if not (nnx,nny,shouldfindFirst) in visited:
                                visited.append((nnx,nny,shouldfindFirst))
                                if board[nnx][nny]==order[idx]: 
                                    shouldfindFirst = False #오른쪽카드찾아야함
                                q.append((nnx,nny,cnt+1,shouldfindFirst,idx))
                        elif board[nx][ny]==order[idx]: 
                            if not (nx,ny,shouldfindFirst) in visited:
                                visited.append((nx,ny,shouldfindFirst))
                                shouldfindFirst = False #오른쪽카드찾아야함
                                q.append((nx,ny,cnt+1,shouldfindFirst,idx))
            
        
        #print("answers=",answers)
    
    return answers

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0)) # 14
#print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1)) # 16

'''
dx = [0,0,1,-1] # 동서남북
dy = [1,-1,0,0]

def solution(board, r, c): # 커서의 처음위치(r,c)
    def ctrl(x,y,dir,card):
        while 0<=x+dx[dir]<4 and 0<=y+dy[dir]<4 and (board[x+dx[dir]][y+dy[dir]]==0 or board[x+dx[dir]][y+dy[dir]]==card):
            x += dx[dir]
            y += dy[dir]
            if board[x][y]==card:
                break
        return x,y
    nx,ny = ctrl(0,r,c,1)
    return nx,ny
print(solution([[1,0,0,3]],0,0)) # (0, 2)
print(solution([[1,3,0,0]],0,0)) # (0, 0)
print(solution([[1,0,0,1]],0,0)) # (0, 3)
print(solution([[1,1,0,0]],0,0)) # (0, 1)
'''