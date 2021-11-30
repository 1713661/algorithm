# 내가 구상한 방법은 같은 그룹의 1이어도 중간에 0이 있으면 True로 인식함
# 그룹핑부터 구현해야함!!!!! 
# jinhan814님은 섬의 가장자리일때만 bfs돌아가도록 구현하였음
# 섬의 가장자리 구할 때는 큐 쓸필요는없고 동서남북에 0이있으면 flag하는식으로 구현했음

# 참신한 풀이법: https://suri78.tistory.com/133 -> 이 방법도 꼭 풀어보기!! (근데 지금은 딴 게 더 급하니 딴 것부터 풀기)
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []
visited = [[False]*N for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int,input().split())))
print(graph)

# 0=바다 1=육지
# 모든 칸을 탐색하는데 
# 처음에 인접한 칸이 1이면 종료
# 0이면 계속 실행(바다로 나아갔으니까)

def bfs(x,y):
    answer = 0
    queue = deque()
    queue.append((x,y,False,0))
    while queue:
        x,y,check,cnt = queue.popleft()
        print("now=",x,y,"check=",check,"cnt=",cnt)
        if check: 
            cnt += 1
        if not check and cnt!=0:        # 조건 만족하는 애는 무조건 최소거리이므로(bfs 기본원리) 바로 return하면 됨
            return cnt              
        for (dx,dy) in (0,1),(0,-1),(1,0),(-1,0):   #동서남북
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                visited[nx][ny]=True
                if graph[x][y]==1 and graph[nx][ny]==0:
                    graph[nx][ny]=1
                    queue.append((nx,ny,True,cnt))
                if graph[nx][ny]==1:
                    queue.append((nx,ny,False,cnt))
                '''
                if graph[x][y]==0 and graph[nx][ny]==1:
                    queue.append((nx,ny,False,cnt))
                '''

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j]=True
            print("(i,j)=",i,j)
            print("answer=",bfs(i,j))       

# 두번째시도
'''

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
print(graph)

# 0=바다 1=육지
# 모든 칸을 탐색하는데 
# 처음에 인접한 칸이 1이면 종료
# 0이면 계속 실행(바다로 나아갔으니까)

def bfs(x,y):
    visited = [[False]*N for _ in range(N)]
    queue=deque()
    queue.append((x,y,0))
    while queue:
        x,y,cnt = queue.popleft()
        if graph[x][y]==1 and cnt!=0: # for문에서 1을 안넣는데 이 조건 어떻게 만족하겠어!!
            return cnt
        print("now=",x,y,"cnt=",cnt,"graph=",graph[x][y])
        for (nx,ny) in (x,y+1),(x,y-1),(x+1,y),(x-1,y): #동서남북
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if graph[nx][ny]==0:
                    visited[nx][ny] = True
                    queue.append((nx,ny,cnt+1))
                    print(queue)
    #print(cnt)


   
                

for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            print("(i,j)=",i,j)
            print("answer=",bfs(i,j))
            break
                        '''