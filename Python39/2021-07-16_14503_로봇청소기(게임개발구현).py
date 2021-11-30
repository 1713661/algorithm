import sys
input = sys.stdin.readline

N,M = map(int, input().split()) # 행,열
r,c,direction = map(int, input().split())   # (r,c)=처음로봇청소기가있는좌표 d=바라보는방향(북동남서)

graph=[]
for _ in range(N): # 0=빈칸, 1=벽
    graph.append(list(map(int,input().split())))
#print(graph)

clean = [ [False]*M for _ in range(N) ]

def turn_left():
    global direction
    direction =  (direction-1)%4 #d는 전역변수(방향은 while문 돌때마다 초기화할필요없음)

dx = [-1,0,1,0]# 북동남서
dy = [0,1,0,-1]
x,y = r,c
turn_time = 0
clean[x][y] = True     # 1. 현재 위치를 청소한다
answer = 1
while True: 
    turn_left()             # 2. 왼쪽 방향부터 탐색
    turn_time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]
    print("now=",nx,ny,"clean[nx][ny]=",clean[nx][ny])
    if graph[nx][ny]==0 and clean[nx][ny]==False:    # a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면
        clean[nx][ny]=True
        #print("clean[nx][ny]=", clean[nx][ny])
        answer += 1
        print("answer=",answer)
        x,y = nx,ny                 # 그 방향으로 회전한 다음 한 칸을 전진하고 
        turn_time = 0               # 1번부터 진행
                                    # b. 왼쪽 방향에 청소할 공간이 없다면
                                    # 2번으로 돌아간다.

    if turn_time==4:                # 네 방향 모두 청소가 이미 되어있거나 벽인 경우
        nx = x - dx[direction]
        ny = y - dy[direction]
        print("nx,ny=",nx,ny)
        if graph[nx][ny]==0:         
            x,y = nx,ny             # 바라보는 방향을 유지한 채로 한 칸 후진을 하고
            turn_time = 0           # 2번으로 돌아간다.  

        else:                       # 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 
            break                   # 작동을 멈춘다.
            

print(answer)
#### 로봇 청소기가 청소하는 칸의 개수를 출력
