# 상단의 좌표를 (1, 1) 가로방향으로 놓여있는 상태
# 앞뒤 구분없이 움직일 수 있습니다.
# 로봇이 차지하는 두 칸 중 어느 한 칸이라도 (N, N) 위치에 도착하면 됩니다.
# 회전이 가능(반시계)
# 어느 칸이든 축이 될 수 있지만, 회전하는 방향(축이 되는 칸으로부터 대각선 방향에 있는 칸)에는 벽이 없어야 합니다. 
# 로봇이 한 칸 이동하거나 90도 회전하는 데는 걸리는 시간은 정확히 1초 입니다.
# 위치까지 이동하는데 필요한 최소 시간

# 로봇이 처음에 놓여 있는 칸 (1, 1), (1, 2)는 항상 0으로 주어집니다.
# 로봇이 항상 목적지에 도착할 수 있는 경우만 입력으로 주어집니다.


###### 4가지 경우 중 가능한 경우만을 리스트에 넣어 리턴
# 대각선이 벽인 경우에는 continue
# 돌린 결과가 벽인거 continue는 dfs에서 할거임

# 36분 경우의 수 너무 많아서 이거 다 일일히 구현하는 게 맞나싶어서 답지봄
# +13분 (가로/세로,시계/반시계,위로/아래로) 총 8가지 경우의 수 그림으로 그려봄


# 25분 bfs로 다시짜기(move를 생각을못했음)
# 34분 getSoutheastPoint 함수만들기 (이거 전혀 필요없었음 그냥 set자료형쓰면되는거였는데...) 
# 40분 변수가독성떨어져서우왕좌왕
# 51분 동서남북 다 move해야함(ㄹ자로이동할수있기때문)
# 61분 서,북 newPoints에 넣어야하는지(이것도 move랑 마찬가지)
# 65분 그림그려서확인
# 86분 getEnableBorders 함수만들기
# 90분 로봇이 세로일때도 그려줬음
# 108분 rotate border,obs를 그때그때 바꾸려고 하지말고 4개원소배열만든다음에 (i+1)%4하도록 아냐 근데 그러면 4*4 2차원배열만들어야하니까 그냥원래하려던방법대로하자
# 120분 아 힘들어...
from collections import deque

#######bn-1을 기준으로 bn을 구하는 게 아니라 a기준으로 bn구하면 그냥 dx,dy 동서남북 쓰면 되는데.......
### 너무 어렵게 생각하고 있었음(항상 이래... 쉽게 푸는 방법을 생각을 못하겠음..)
### 그래도 이 방법도 끝까지 풀어보기!!
# 두 칸 다 빌 때만 회전할 수 있고 enables에 추가할 수 있음
# 두 칸 다 비는것만 조건문으로 쓰면 되기 때문에 굳이 '90도회전일반화코드' 구현할필요없었음
# 언제쯤이면 이렇게 단순한 알고리즘으로 생각할 수 있을까.. 핵심을 파악하지 못하니까 자꾸 어려운 길로 가는거다
def rotateB(ax,ay,bx,by): #반시계방향
    dx,dy = bx-ax,by-ay
    return (ax-dy,ay) if dx==0 else (ax,ay+dx)

def rotateO(x,y):


def getEnableBorders(board,pList):
    N = len(board)
    enables = []
    for i in range(2): 
        axis,border = pList[i],pList[1-i] #더 동남쪽에있는좌표가 축이되어야함 #################### 꼭 그래야하나? 노노노 아님
        ax,ay = axis[0],axis[1]
        bx,by = border[0],border[1]
        dx,dy = bx-ax,by-ay
        ####### 바꿔야함
        #obs = [ (ax-1,ay-1),(ax+1,ay-1),(ax+1,ay+1),(ax-1,ay+1) ] #축을 기준으로 대각선
        obs = (ax-dy,by) if dx==0 else (ax+dx,by) #############
        for j in range(4):
            # 아니 잠깐 이렇게 짜면 안되지... 180도 회전하는 것까지 enables에 넣어버리잖아
            nbx,nby = rotateB(ax,ay,bx,by)
            nox,noy = rotateO(ax,ay,bx,by) ########### obs rotate 타이밍 잘 못잡겠음
            if 0<=obs[j][0]<N and 0<=obs[j][1]<N and 0<=nbx<N and 0<=nby<N:
                if board[obs[j][0]][obs[j][1]]==1: #대각선 방향에 벽이 있으면
                    continue
                enables.append( () )
                
                

    return enables



    
    if axis[0]==border[0]: # 가로로 있을때
        print("가로")
        newborder = #시계방향으로 회전
        newborder_counter = (border[0],axis[1])#반시계방향으로 회전
    elif axis[1]==border[1]:  # 세로로 있을때
        print("세로")
    else:
        print("who are you?")

    # 기준1)로봇 가로로 있을때,세로로 있을때
    # 기준2) 시계,반시계
    N = len(robots) # 한변의길이
    for x in range(N):
        for y in range(N):
            robots[x][y]  

def getBigger(p1,p2):
    x1,y1, x2,y2 = p1[0],p1[1], p2[0],p2[1]

    if x1==x2: #로봇이 가로로 있으면
        return p1,p2 if y1<y2 else p2,p1

    else:      #로봇이 세로로 있으면
        return p1,p2 if x1<x2 else p2,p1

'''
def getBigger(p1,p2):
    x1,y1, x2,y2 = p1[0],p1[1], p2[0],p2[1]

    if x1==x2: #로봇이 가로로 있으면
        return p2 if y1<y2 else p1

    else:      #로봇이 세로로 있으면
        return p2 if x1<x2 else p1
'''
def bfs(board):
    N = len(board) #한변의길이
    q = deque()
    q.append( ((1,1), (1,2)) )
    #visited = [[[[False]*N for _ in range(N)] for _ in range(N)] for _ in range(N)]
    # 4차원배열 한변길이 100까지여서 4차원은안될것같음 
    # 근데 visited 안쓰면 구현 힘들텐데.. 그래서 이코테는 visited를 큐 형태로 만듦(그것도 가능이잖아. 진짜 문제 많이 풀어봐야함)
    
    while q:
        #tmp1,tmp2 = q.popleft()
        #(x1,y1),(x2,y2) = getBigger(tmp1,tmp2)
        #(x1,y1),(x2,y2) = q.popleft() #pt1=(1,1) pt2=(1,2)
        p1,p2 = q.popleft()
        x1,y1, x2,y2 = p1[0],p1[1], p2[0],p2[1]

        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        ####### 동서남북 다해야할것같음 아냐안해도될것같음
        ##서,북 가는순간 최소거리가 아님 아니지 ㄹ자면 서,북이어도 최소값일수있음

        newPoints = []
        for i in range(4): #newPoints = [ ((x1,y1+1),(x2,y2+1)), ((x1+1,y1),(x2+1,y2+1))]
            nx1,ny1 = x1+dx[i],y1+dy[i]
            nx2,ny2 = x2+dx[i],y2+dy[i]
            newPoints.append( ((nx1,ny1),(nx2,ny2)) )
        
        p_list = [p1,p2]
        newPoints.extend(getEnableBorders(p_list))

        for (nx1,ny1),(nx2,ny2) in newPoints:
            if 0<=nx1<N and 0<=ny1<N and 0<=nx2<N and 0<=ny2<N:
                if board[nx2][ny2]==0:
                    q.append( (nx1,ny1),(nx2,ny2) )


           
    return
# getEnableBorders말고 move경우를 생각못했음. 최소거리 가야하니까 너비우선탐색해야함
def dfs(board,axis,border):
    newPoints = getEnableBorders(axis,border)

    for (new_axis,new_border) in newPoints: # new_axis=(nx,ny) new_border=(nx,ny)
        if board[new_border[0]][new_border[1]]==0:
            dfs(board,new_axis,new_border)



def solution(board): # dfs
    N = len(board) #한변의길이
    positions = [ (1, 1), (1, 2) ]

    for _ in range(2):
        dfs(positions[0],positions[1])
        dfs(positions[1],positions[0])
    # 반시계방향으로 회전
    getEnableBorders(board)
    
    # 로봇의 위치(두 점)
    # 각각의 점에 대하여 getEnableBorders(시계,반시계)
    # 기준1)로봇 가로로 있을때,세로로 있을때
    # 기준2) 시계,반시계
    #### 벽이 있으면 안되는 칸 4가지 경우로 나눌수있음
    answer = 0
    return answer