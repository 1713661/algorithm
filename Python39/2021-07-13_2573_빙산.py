import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split()) #행,열

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
#print(graph)

def bfs(x,y,melt,visited):
    dx = [-1,0,1,0] #북동남서(시계방향으로탐색)
    dy = [0,1,0,-1]
    queue = deque()
    if visited[x][y]: 
        #print("return False")
        return False
    queue.append((x,y))
    visited[x][y]=True
    while queue:
        #print("beforepop=",queue)
        x,y = queue.popleft()
        #print("afterpop=",queue)
        #print("now=",x,y)
        for i in range(4):  #북동남서(시계방향으로탐색)
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M: #인덱스범위를 벗어나면
                continue
            if graph[nx][ny]==0: #새로 탐색한 배열이 바다면
                melt[x][y] += 1
                continue #큐에는 추가하면 안되니까
            if not visited[nx][ny]: # 아직 방문하지 않은 노드라면(빙산만 추가됨)
                queue.append((nx,ny))
                visited[nx][ny]=True

    #print("return True")
    return True

#1~N,1~M 브루트포스탐색하면서 bfs로 numberOfIce 구하고 melt배열 구하기
def oneYearLater():
    check = False   # 전부 녹았는지 확인하는 변수
    melt = [[0]*M for _ in range(N)] # 1년 후 각각의 빙산이 얼마나 녹는지 저장할 배열
    visited = [[False]*M for _ in range(N)] #방문한 노드를 graph에 표시할 경우 melt를 적용하기 어려움 
    numberOfIce = 0
    for i in range(1,N):    # 모서리는 바다니까 탐색할 필요없음
        for j in range(1,M):
            if graph[i][j] != 0:
                check = True
                #print("(i,j)=",i,j)
                if bfs(i,j,melt,visited):
                    #print("visited=",visited)
                    numberOfIce += 1
    '''
    print("melt=")
    for i in range(N):  
        print(melt[i])
    '''

    for i in range(N):
        for j in range(M):
            graph[i][j]-=melt[i][j]     # 처음 0년은 전혀 녹지않음
            if graph[i][j]<0:
                graph[i][j]=0
    '''
    print("graph=")
    for i in range(N):
        print(graph[i])
    '''

    #print("numberOfIce=",numberOfIce)
    return numberOfIce, check

year = -1
while True: 
    year += 1
    #print("<year>=",year)
    num, check = oneYearLater()
    if num>=2:
        print(year)
        break
    if not check:
        print("0")
        break
    
    
