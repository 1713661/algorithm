# 57분
from collections import deque
INF = int(10e9)

### dfs로 짜면 길이 막혔을 때 어디로 돌아가야 하는지 찾기 어려움...
# 그리고 첨에는 무조건 cost +100인 것도 구현하기 조금 까다롭고

### 이 경우에는 케이스3에서 ㄱ자인애만 잡혀서 2100이 아니라 2600 나옴 (코너개수,직선도로개수)로 다시짜야할듯

def solution(board):
    N = len(board)
    answer = []

    q = deque()
    q.append((0,0,4)) #x,y,dir

    dx = [0,0,1,-1] #동서남북
    dy = [1,-1,0,0]

    cost = [ [INF]*N for _ in range(N)]
    cost[0][0]=0

    while q:
        x,y,dir = q.popleft()
        #print("now=",x,y,"dir=",dir,"cost=",cost[x][y])

        if x==N-1 and y==N-1:
            answer.append(cost[x][y])
            continue

        for newdir in range(4): #for (nx,ny) in (x,y+1),(x,y-1),(x+1,y),(x-1,y): # 동서남북
            nx = x+dx[newdir]
            ny = y+dy[newdir]
            if 0<=nx<N and 0<=ny<N and board[nx][ny]==0:
                if newdir==dir:
                    if cost[nx][ny]>=cost[x][y]+100: 
                        cost[nx][ny] = cost[x][y]+100 # 바로 cost 바꿔주는 게 아니라
                        q.append((nx,ny,newdir))
                else:
                    if (nx+ny)==1: #처음에는 방향 정해져있지 않으므로 무조건 직선도로
                        cost[nx][ny] = cost[x][y]+100
                        q.append((nx,ny,newdir))

                    else:
                        if cost[nx][ny]>=cost[x][y]+600:
                            cost[nx][ny] = cost[x][y]+600 
                            q.append((nx,ny,newdir))  
        #print("\tq=",q)      
    print("answer=",answer)
    return min(answer)

#print("1",solution([[0,0,0],[0,0,0],[0,0,0]]))
#print("2",solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
#print("3",solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
#print("4",solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))

print("expect 3000",solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]))