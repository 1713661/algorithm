# 1. tilt했을때 구슬 하나라도 움직이면 됨(파란구슬만 움직여도 상관없다는 말!) 이건 알고리즘을 제대로 이해했어야했음
# 2. visited 어떤 상태가 돼야 이미 이전에 해본 시도이지?
# NxM 행렬 두개로 visited를 하는게 아닌, NxMxNxM의 visited 4차원 행렬 한개로 체크를 해야합니다., visited 따로구현하면안되나? 
# ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ는 case A에서 갖고오고 visited는 case B에서 갖고왔는데(각각 다른 케이스에서 갖고온건데) 둘다 visited=True니까 queue.append 못하는거임!

# 50분(컴파일 한번도 안했는데...)
# +41분 첫제출 7%에서 틀렸습니다. 
# +22분 테스트케이스 하나 틀릴때마다 코드고치는걸로는 통과할 수 없음. 
# +22분 30%정도에서 틀렸습니다. -> visited배열 4차원으로 만들어야!!!

# 변수 잘못쓰지 않도록 주의! (x,y | r,b) 

import sys
from collections import deque
input = sys.stdin.readline

# 구멍에 빠지면 그 구멍 좌표 리턴
def tilt(rx,ry,bx,by,dx,dy):
    global board
    rc,bc = 0,0
    while board[rx+dx][ry+dy]==0:
        rx += dx
        ry += dy
        rc += 1
        if rx==ox and ry==oy:
            break
    while board[bx+dx][by+dy]==0:
        bx += dx
        by += dy
        bc += 1
        if bx==ox and by==oy:
            break
    return rx,ry,bx,by,rc,bc

def bfs(rx,ry,bx,by):
    global board
    queue = deque()
    visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)] #### 4차원 배열 써야함!!!!
    #print("hibx=",bx,"by=",by)
    queue.append((rx,ry,bx,by,0))
    visited[rx][ry][bx][by]=True

    while queue:
        rx,ry,bx,by,cnt = queue.popleft()
        #print("(rx,ry)=",rx,ry,"(bx,by)=",bx,by,"cnt=",cnt)
        if cnt>10: ########얘를 제일 앞에 써야!!!!!! (시험장에서 이러면 안되는데...)
            return -1

        if bx==ox and by==oy: continue

        if rx==ox and ry==oy: # 파란구슬은 안빠지고 빨간구슬만 빠진 경우
            return cnt


        '''
        for dir in range(4):
            tilt(dir)
        '''
        for (dx,dy) in (0,1),(0,-1),(1,0),(-1,0): #(rx,ry+1),(rx,ry-1),(rx+1,ry),(rx-1,ry):  #동서남북
            #print("(dx,dy)=",dx,dy,"board[rx+dx][ry+dy]=",board[rx+dx][ry+dy])

            if board[rx+dx][ry+dy]==0 or board[bx+dx][by+dy]==0: ########################### 하나라도 갈 수 있으면 ok!!!!
                newrx,newry,newbx,newby,rc,bc = tilt(rx,ry,bx,by,dx,dy)
                #print("1: newrx,newry=",newrx,newry,"newbx,newby=",newbx,newby)
                ####### newrx,newry,newbx,newby 겹치면 rc,bc으로 보정해야함

                # 보정
                if newrx==newbx and newry==newby:
                    #동시에 구멍에 빠지면 continue(return -1하면 안돼!!!!!!!!!! 이 길이 아니었던거고, 다른길중에 가능한길이있을수있기때문)(bfs)
                    if newrx==ox and newry==oy: continue 
                    if rc>bc:
                        newrx -= dx
                        newry -= dy
                    else: #bc>rc
                        newbx -= dx
                        newby -= dy

                #print("newrx,newry=",newrx,newry,"newbx,newby=",newbx,newby)
                #if visited[newrx][newry] or visited[newbx][newby]: continue 이렇게쓰면 처음값 visited=True하기 어려움
                if not visited[newrx][newry][newbx][newby]: # 둘다 방문한 적 있어야 이전에 해봤던 시도인듯?
                    visited[newrx][newry][newbx][newby]=True

                    queue.append((newrx,newry,newbx,newby,cnt+1))
        #print("queue=",queue)
    return -1
    

N,M = map(int,input().split()) #세로,가로

board = []
for _ in range(N):
    board.append(list(input().rstrip()))

for i in range(N):
    for j in range(M):
        if board[i][j]=='R':
            rx,ry = i,j
        if board[i][j]=='B':
            bx,by = i,j
        if board[i][j]=='O':
            ox,oy = i,j

        if board[i][j]=='#':
            board[i][j]=-1 #벽
        else:
            board[i][j]=0 #빈공간 R,O,B도 여기에포함
        
'''
for i in range(N):
    print(board[i])
'''

#print("start: (rx,ry)=",rx,ry,"(bx,by)=",bx,by,"(ox,oy)=",ox,oy)

print(bfs(rx,ry,bx,by))


############ 주어진 조건'만', 그리고 주어진 조건'은' 완벽하게 구현해야함
#
# 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.----------> 파란 구슬이 들어가는 건 무조건 continue
# 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. ----------------------------------------------------> 
# 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다.  

# 구슬이 2개라 구슬의 움직임을 구현하는 부분이 어려울 수 있는데, 
# 이 부분은 구슬이 하나만 있다고 생각하고 move 함수를 구현한 뒤, 
# 만약 두 구슬의 이동 위치가 같을 경우 적절히 방향에 맞게 예외처리를 해주면 됩니다.

# !!!!!!!!!!!공 있는 위치도 벽이 아니니까 0으로 초기화

################################# 알고리즘 흐름&구현해야할 것 정리
# visited는 빨간공 파란공 '둘다' 같은 위치에 방문한 경우만 제외하면 됨 (하나만 겹치는 건 다른 경우기 때문에 큐에 넣어줘야함)(그리고 이건 4차원배열로 구현해야함)
# 왔던 길 일일히 visited=True로 바꿀 필요없음(공은 중간에 멈추지 않고 빈칸이 벽으로 바뀌는 일도 없기 때문)
# 공 있는 위치도 0으로 초기화(공 이동했을 때 R,B 따로 지워줄 필요없음)
# action() 함수 한개만 구현(공 겹치는 경우만 for문에서 예외처리) (rc<bc 비교하면 분기문 더 안 만들어도 됨)
# x,y ---- O(구멍) ---- nx,ny 이런식으로 구멍 지나친 경우
# 1. action에서 지나치지 않도록 구현하는 방법 -> 이걸로 결정!!!
# 2. isOut 함수 따로 구현하는 방법(jinhan814님 방법)

################################# 고쳐야 할 부분
# for문 예외처리 (rc bc로 나누기) 
# action 함수에 cnt(한번 기울일 때 이동하는 거리,횟수) += 1도 구현해야함(그래야 rc,bc 구할 수 있으니까)
# action 함수 구멍 도달하는 경우
        
