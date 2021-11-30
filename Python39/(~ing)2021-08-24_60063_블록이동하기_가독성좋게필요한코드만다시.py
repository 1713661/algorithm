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

#######bn-1을 기준으로 bn을 구하는 게 아니라 a기준으로 bn구하면 그냥 dx,dy 동서남북 쓰면 되는데.......
### 너무 어렵게 생각하고 있었음(항상 이래... 쉽게 푸는 방법을 생각을 못하겠음..)
### 그래도 이 방법도 끝까지 풀어보기!!
# 두 칸 다 빌 때만 회전할 수 있고 enables에 추가할 수 있음
# 두 칸 다 비는것만 조건문으로 쓰면 되기 때문에 굳이 '90도회전일반화코드' 구현할필요없었음
# 언제쯤이면 이렇게 단순한 알고리즘으로 생각할 수 있을까.. 핵심을 파악하지 못하니까 자꾸 어려운 길로 가는거다



# 이코테랑 코드 길이 거의 비슷함. 자신감을 갖자!!!

from collections import deque

# 굳이 회전할 필요가 없음 어떤 칸이 0이면 enables배열에 넣는다는 관점으로 접근하기
def rotateB(ax,ay,bx,by): #반시계방향
    dx,dy = bx-ax,by-ay
    return (ax-dy,ay) if dx==0 else (ax,ay+dx)

############## 바꿔야함
def rotateO(ax,ay,bx,by): #반시계방향
    dx,dy = bx-ax,by-ay
    return (ax-dy,ay) if dx==0 else (ax,ay+dx)

# 아니 잠깐 이렇게 짜면 안되지... 
def getEnableBorders(board,pList):
    N = len(board)
    enables = []
    for i in range(2): 
        axis,border = pList[i],pList[1-i]
        ax,ay = axis[0],axis[1]
        bx,by = border[0],border[1]
        dx,dy = bx-ax,by-ay
        obs = (ax-dy,by) if dx==0 else (ax+dx,by)
        for j in range(4):
            # 아니 잠깐 이렇게 짜면 안되지... 180도 회전하는 것까지 enables에 넣어버리잖아
            nbx,nby = rotateB(ax,ay,bx,by)
            nox,noy = rotateO(ax,ay,bx,by) ########### obs rotate 타이밍 잘 못잡겠음 그냥 for4문에서 그때그때 할당해야
            if 0<=obs[j][0]<N and 0<=obs[j][1]<N and 0<=nbx<N and 0<=nby<N:
                if board[obs[j][0]][obs[j][1]]==1: #대각선 방향에 벽이 있으면
                    continue
                enables.append( () )
    return enables

def bfs(board):
    N = len(board) #한변의길이
    q = deque()
    q.append( {(1,1), (1,2)} ) # 맨 바깥은 튜플대신 집합쓰기
    visited = [[[[False]*N for _ in range(N)] for _ in range(N)] for _ in range(N)] #시간초과나면 큐에 구현하기

    while q:
        p1,p2 = q.popleft()
        x1,y1, x2,y2 = p1[0],p1[1], p2[0],p2[1]

        dx = [0,0,1,-1]
        dy = [1,-1,0,0]

        newPoints = []
        for i in range(4): 
            nx1,ny1 = x1+dx[i],y1+dy[i]
            nx2,ny2 = x2+dx[i],y2+dy[i]
            newPoints.append( {(nx1,ny1),(nx2,ny2)} )
        
        p_list = [p1,p2]
        newPoints.extend(getEnableBorders(p_list))

        for (nx1,ny1),(nx2,ny2) in newPoints:
            if 0<=nx1<N and 0<=ny1<N and 0<=nx2<N and 0<=ny2<N:
                if board[nx2][ny2]==0: # 이건 위에 getEnableBorders함수에서 확인해야 하는거고.. 
                                       # 여기선 visited확인해야함(큐로 만들기)
                    q.append( {(nx1,ny1),(nx2,ny2)} )


def solution(board): # bfs
    bfs(board)
    answer = 0
    return answer