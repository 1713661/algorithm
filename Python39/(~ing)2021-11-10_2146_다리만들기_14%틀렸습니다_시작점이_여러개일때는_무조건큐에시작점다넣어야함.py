# 파이썬 14%에서시간초과 pypy 14% 틀렸습니다
# 밑의경우처럼 정답이 for문 제일 마지막에서 나오면 틀렸습니다 뜸
###### 시작점이 여러개일때는 무조건 큐에 시작점 다 넣어야함
# 이렇게 했더니 결국엔 메모리 초과.. 바킹독님 코드대로 짜자
'''
for x in range(N):
    for y in range(N):
        if graph[x][y]==value:  
5
1 0 0 0 0
1 0 0 0 1
1 1 1 0 1
0 0 0 0 0
0 0 0 1 0
[2, 0, 0, 0, 0]
[2, 0, 0, 0, 3]
[2, 2, 2, 0, 3]
[0, 0, 0, 0, 0]
[0, 0, 0, 4, 0]
[2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, -1]
[0, 0, 0, -1, -1]
[1, 1, -1, -1, -1]
[2, -1, -1, -1, -1]
[-1, -1, -1, 2, 1]
[-1, 3, 2, 1, 0]
[-1, -1, -1, 1, 0]
[-1, -1, -1, -1, 1]
[-1, -1, -1, -1, -1]
[-1, -1, -1, -1, -1]
[-1, -1, -1, -1, -1]
[-1, -1, -1, 2, -1]
[-1, -1, 2, 1, 2]
[-1, 2, 1, 0, 1]
2
'''
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

def OOB(x,y):
    return x<0 or x>=N or y<0 or y>=N

def indexing(x,y,idx):
    q = deque()
    q.append((x,y))
    graph[x][y] = idx

    while q:
        x,y = q.popleft()
        for (nx,ny) in (x,y+1),(x,y-1),(x+1,y),(x-1,y): #동서남북
            if OOB(nx,ny): continue
            if graph[nx][ny]==1:
                graph[nx][ny] = idx
                q.append((nx,ny))

def solution():
    
    def bfs(value):
        ans = int(10e9)
        q = deque()
        for x in range(N):
            for y in range(N):
                if graph[x][y]==value:
                    q.append((x,y))
                    
        dist = [ [-1]*N for _ in range(N) ] #visited =  [ [False]*N for _ in range(N) ]
        dist[x][y] = 0 #visited[x][y] = True

        while q:
            x,y = q.popleft()
            #print("now=",x,y,dist[x][y])

            for (nx,ny) in (x,y+1),(x,y-1),(x+1,y),(x-1,y): #동서남북
                if OOB(nx,ny): continue
                if dist[nx][ny]!= -1 and dist[x][y]+1>dist[nx][ny]: continue
                if graph[nx][ny] == value: 
                    dist[nx][ny]=0
                    q.append((nx,ny))
                elif graph[nx][ny] == 0: 
                    dist[nx][ny]=dist[x][y]+1
                    q.append((nx,ny))
                else:
                    ans = min(ans, dist[x][y]+1)
                    '''
                    for i in range(N):
                        print(dist[i])
                    '''
                    return ans
                
    idx = 2
    for i in range(N):
        for j in range(N):
            if graph[i][j]==1:
                indexing(i,j,idx)
                # {(3, 4), (4, 3), (1, 1), (2, 0), (2, 3), (0, 2), (2, 2), (3, 2), (1, 3)}
                idx += 1
    '''
    for i in range(N):
        print(graph[i])
    '''
    li = [i for i in range(2,idx)]
    #print(li)
    answers = []
    for idx in li:
        answers.append(bfs(idx))
    
    return min(answers)-1

print(solution())