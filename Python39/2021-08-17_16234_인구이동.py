# 48분 마지막케이스안됨
# +7분 틀렸습니다. 마지막에 코드 너무 어거지로 짰음
# +7분 #L미만이면 다 다르게 인덱싱 붙음(종료조건)
# +10분 시간초과해결방법(옆에갈곳없으면 아예 bfs부르지않는걸로)
########## move 함수 따로 만들지말고 bfs에서 해결하기(인덱싱한 점 또 완전탐색하는거 너무오래걸려)
# +31분 80%에서시간초과 ->pypy
import sys
from collections import deque
input = sys.stdin.readline

N,L,R = map(int,input().split()) 
# 땅크기,두 나라의 인구 차이가 L명 이상, R명 이하 (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)

def bfs(startX,startY,cnt): #bfs

    global graph,index

    q = deque()
    q.append((startX,startY))

    points = []
    sum = 0
    count = 0

    points.append((startX,startY))
    sum += graph[startX][startY]
    count += 1
    index[startX][startY]=cnt

    while q:
        x,y = q.popleft()
        #print("now=",x,y)
        for (nx,ny) in (x,y+1),(x,y-1),(x+1,y),(x-1,y): # 동서남북
            if 0<=nx<N and 0<=ny<N:
                if index[nx][ny]==0 and L<=abs(graph[nx][ny]-graph[x][y])<=R: ##조건맞나?
                    index[nx][ny]=cnt
                    q.append((nx,ny))

                    points.append((nx,ny))
                    sum += graph[nx][ny]
                    count += 1
    
    avg = sum//count

    for point in points:
        graph[point[0]][point[1]] = avg




graph = []
index = [ [0]*N for _ in range(N) ]
for _ in range(N):
    graph.append(list(map(int,input().split())))    

day = 0
points = []
while True:
    #print("day",day)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if index[i][j]==0:
                check=False
                cnt += 1
                for (ni,nj) in (i,j+1),(i,j-1),(i+1,j),(i-1,j): # 동서남북
                    if 0<=ni<N and 0<=nj<N:
                        if index[ni][nj]==0 and L<=abs(graph[ni][nj]-graph[i][j])<=R: ##조건맞나?
                            check=True
                            break
                if check:
                    bfs(i,j,cnt) 
                else:
                    index[i][j]=cnt
        
                
                    
    if cnt==N*N: 
        print(day)
        break

    '''
    print("index")
    for i in range(N):
        print(index[i])
    
    print("graph")
    for i in range(N):
        print(graph[i])
    '''
    day += 1

    #국경선닫기
    for i in range(N):
        for j in range(N):
            index[i][j]=0
    '''
    for point in points:
        index[point[0]][point[1]]=0
    '''
    