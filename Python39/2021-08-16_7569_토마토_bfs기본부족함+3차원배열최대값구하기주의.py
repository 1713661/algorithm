# 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

# 3차원배열 초기화 애먹음...(무조건 2차원배열에 +1만 한다고 생각하자)
# print문찍어서 문제해결하려고 하지말고 알고리즘의 논리적 오류를 찾자!!!

import sys
from collections import deque
input = sys.stdin.readline

M,N,H = map(int,input().split()) # 2<=가로,세로,높이<=100

tomato = [ [] for _ in range(H)]
for i in range(H):
    for _ in range(N):
        tomato[i].append(list(map(int,input().split())))


def bfs():
   
    global q
    global tomato
   
    while q:
        z,x,y = q.popleft()
        for (nz,nx,ny) in (z+1,x,y),(z-1,x,y),(z,x+1,y),(z,x-1,y),(z,x,y+1),(z,x,y-1):
            if 0<=nz<H and 0<=nx<N and 0<=ny<M:
                if tomato[nz][nx][ny]==0:
                    tomato[nz][nx][ny]=tomato[z][x][y]+1 #########
                    q.append((nz,nx,ny))

q = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m]==1:
                q.append((h,n,m)) ################## 처음에 1인 애들 다 넣어야함!!!(bfs 기본기 부족해) 
                # 이코테 미로탈출이랑 비슷한것같은데?
bfs()

check=False
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m]==0:
                check=True
                break # 여기까지만 하면 제일 바깥 for문만 나가기 때문
        if check:
            break
    if check:
        break

if check:
    print("-1")
else:
    MAX = 0
    # print(max(list(max(map(max,[l for l in tomato]))))-1) #[l for l in tomato]는 그냥 tomato랑 똑같지않나?
    # SyntaxError: Generator expression must be parenthesized
    # print(max(map(max,map(max,tomato)))-1)
    print(max([max(map(max,l)) for l in tomato])-1)
    '''
    for l in tomato:
        MAX = max(MAX,max(map(max,l)))
    print(MAX-1)
    '''

