# 1시간 5분
############ 왜 BFS를 써야하는지 모르겠음... -> 최단거리 구하기용!!! 무얼 구해야하는지 알고 코드짜야함!!!!!!! 메타인지!!!!!
# 문제 조건이 많아서 그거 정리하는것도 오래걸렸음..
# 문제 세부사항 구현하는데에 시간낭비하지말자(able_to_eat, able_to_pass도 구할 필요 없었음)
# 연구소 풀때도 조합 라이브러리 익숙치 않아서 출력문 확인하느라고 시간 오래 잡아먹음(그건 결과적으로 잘 풀기는 했지만..)
# 수학문제 푸는 거랑 똑같음. 디테일에 빠져들면 안됨!!!!!!!!!!!!!!!!!!

# 문제이해부터 잘하고, 구상한거 일단 주석으로 쓴 다음에(잘 돌아갈까 먼저 생각해보고) 그담에 코드로 구현하기!!!!!!!!

# 아기 상어의 크기는 2
# 지나가기: 아기상어>=물고기
# 먹기: 아기상어>물고기
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.(이때 BFS 이용하기 able_to_eat배열 구현할 필요없었음!!!!)
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다. 
# 북서동남 순으로 탐색!!!! (밑에칸은 맨 나중에 탐색해야되잖아)
# 물고기를 먹으면, 그 칸은 빈 칸이 된다.

# 아기 상어는 자신의 크기와 '같은 "수"'의 물고기를 먹을 때 마다 크기가 1 증가한다. 

# 북서동남순으로 탐색해도 '위에서부터,왼쪽에서부터' 법칙 성립안할 수 있음
# 이코테 풀이는 dist배열 리턴함(BFS로 거리값 다 구하고 그 중 최솟값&위왼쪽값을 다음값으로)
# 나는 dist배열말고 next배열써서 visited배열도 선언했어야했음
############# dist >> visited >> graph에 바로 / 배열 >> 큐  
# BFS로 거리가 dist(1,2,...)인 물고기 중에서 먹을 수 있는 애(자기보다 작은애)를 탐색하는 거기 때문에 
# able_to_eat, able_to_pass 배열 만들 필요없음 (bfs 기본개념!!!!)

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))
'''
for i in range(N):
    print(graph[i])
'''
for i in range(N):
    for j in range(N):
        if graph[i][j]==9:
            sharkX,sharkY=i,j
            graph[i][j]=0
#print("sharkX,sharkY=",sharkX,sharkY)

def bfs(x,y):
    global graph,next,sharkSize
    min_dist = int(10e9) # 4*N도 부족함!!
    dist = 0
    visited = [[False]*N for _ in range(N)]
    temp = [i[:] for i in graph]
    queue = deque()
    queue.append((x,y,dist))
    while queue:
        x,y,dist = queue.popleft()
        if 0<temp[x][y]<sharkSize and min_dist>=dist:
            next[x][y]=True
            min_dist=dist
        for (nx,ny) in (x,y+1),(x,y-1),(x+1,y),(x-1,y): #동서남북
            if 0<=nx<N and 0<=ny<N and 0<=temp[nx][ny]<=sharkSize and not visited[nx][ny]:
                visited[nx][ny]=True #갈수없는값
                queue.append((nx,ny,dist+1))
        #print(queue)
    '''
    for i in range(N):
        print(visited[i])
    '''
    return min_dist

def move(x,y):
    global next
    for i in range(N):
        for j in range(N):
            if next[i][j]:
                return i,j
    return -1,-1

sharkSize = 2
time = 0
cnt = 0
while True:
    next = [[False]*N for _ in range(N)]
    min_dist = bfs(sharkX,sharkY)
    '''
    for i in range(N):
        print(next[i])
    '''
    sharkX, sharkY = move(sharkX,sharkY)
    #print("sharkX,sharkY=",sharkX,sharkY)
    graph[sharkX][sharkY]=0
    cnt += 1
    '''
    for i in range(N):
        print(graph[i])
    '''
    if sharkX==-1 and sharkY==-1:
        print(time)
        break
    if cnt==sharkSize:
        sharkSize += 1
        cnt = 0
        #print("sharkSize=",sharkSize)
    time += min_dist
    #print("time=",time)
