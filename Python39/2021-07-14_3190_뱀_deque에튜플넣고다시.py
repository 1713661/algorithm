import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) #보드의크기=N
K = int(input()) #사과의개수=K

# -1=벽 0=빈공간 1=뱀 2=사과
board = [[0]*(N+2) for _ in range(N+2)]
# board 크기 N이면 충분함!!! 맨 위 맨 좌측이 1행1열부터 시작하니까
for i in range(N+2):
    board[0][i] = -1
    board[N+1][i] = -1
    board[i][0] = -1
    board[i][N+1] = -1
board[1][1]=1   # 뱀 현재위치

#사과 위치 추가하기
for _ in range(K):      
    x,y = map(int,input().split()) #행,열
    board[x][y]=2 #apple은 2

L = int(input()) #뱀의방향변환횟수

timeArr=[0]
dirArr=[0] #동쪽을 바라보고 있으니까
for _ in range(L):
    X,C = input().split() #X초가 끝난 뒤에 C방향(왼쪽(L),오른쪽(D))으로 90도 회전
    timeArr.append(int(X))
    dirArr.append(C)
timeArr.append(10000)

dx = [0,1,0,-1] #동남서북
dy = [1,0,-1,0]

def rotate(dir):        ##### 나머지 연산 이용해서 다시 구하기!!
    global direction
    if dir=='L': #반시계방향 
        if direction==0:
            direction=3
        else:
            direction -= 1
    elif dir=='D': #시계방향
        if direction==3:
            direction=0
        else:
            direction += 1

direction = dirArr[0] #동쪽부터 시작
snake = deque() # 뱀 몸체는 큐로 구현 deque로 구현할 필요없었음!! 
snake.append((1,1))
# 디큐는 안에 튜플 못넣지만 일반 리스트는 안에 튜플 넣을 수 있음 단 일반 리스트는 가장'앞'쪽에 삽입/삭제할때 O(N)걸림
# 이코테 ch5 dfs/bfs 4미로탈출 보니까 가능한데?? 왜 내가 썼을 때는 오류난거지? deque((1,1))로 초기화해도 되는데?

# 게임 시작
def solution():
    global direction
    global snake ################
    x,y,count = 1,1,1
    x_tail, y_tail = 1,1

    for i in range(1,len(timeArr)):   #i=1~len(timeArr)-1
        time = timeArr[i]-timeArr[i-1] #3,12,2
        for _ in range(time): #3,12,2
            # 규칙 구현  
            x_head = x + dx[direction]
            y_head = y + dy[direction]
            #print("nx=",x_head,"ny=",y_head,"time=",time,"count=",count)
            if board[x_head][y_head]==2: #이동한 칸에 사과가 있다면(꼬리는 움직이지 않음)
                #print("apple")
                board[x_head][y_head]=1
                snake.append((x_head,y_head))
                count += 1
                '''
                for j in range(N+2):
                    print(board[j])
                '''
            elif board[x_head][y_head]==0: #비어 있는 칸이라면(꼬리는 움직여야 함)
                #print("~apple")
                board[x_head][y_head]=1
                snake.append((x_head,y_head)) 
                #print("popleft",snake.popleft())    #꼬리는 움직여야함
                #print('x_tail=',x_tail,'y_tail=',y_tail)
                board[x_tail][y_tail]=0
                count += 1
                '''
                for j in range(N+2):
                    print(board[j])
                '''
            elif board[x_head][y_head]==-1 or board[x_head][y_head]==1: #벽이거나 자기 몸이라면
                #print('wall')
                '''
                for j in range(N+2):
                    print(board[j])
                '''
                return count
            x,y = x_head,y_head
        rotate(dirArr[i]) #동=0 남=1 서=2 북=3
        #print(dirArr[i])
        #print("direction=",direction)

print(solution())
        
