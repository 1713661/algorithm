    `# 벽을 K개 까지 부수고 이동하여도 된다.
## distance 쓰면 틀렸다고 나오는데 왜 틀렸는지 모르겠음..ㅠㅠ (테스트케이스 다 정답임)
# 8/2(월) distance 초기값 -1로 설정했더니 됨!!(파이썬은 시간초과.파이썬으로 낸 사람 아예없음. pypy3 써야함)
import sys
from collections import deque
input = sys.stdin.readline

N,M,K = map(int,input().split()) #세로의크기,가로의크기,부술수있는벽의개수

graph=[]
for _ in range(N):
    graph.append(list(map(int,input().rstrip())))

def bfs(x,y):
    distance = [ [[-1]*(K+1) for _ in range(M)] for _ in range(N) ]
    distance[x][y][0]=0
    #print(distance)
    queue = deque()
    queue.append((x,y,0))
    while queue:
        x,y,crashed = queue.popleft()
        if x==N-1 and y==M-1:
            return distance[x][y][crashed]+1
        for (nx,ny) in (x,y+1),(x,y-1),(x+1,y),(x-1,y): # 동서남북
            if nx<0 or nx>=N or ny<0 or ny>=M:  # 범위를 벗어나면
                continue
            if graph[nx][ny]==0 and distance[nx][ny][crashed]==-1: # 갈수 있는 칸이고 벽K번부순상태(crashed)로는아직 방문하지 않은 칸이면
                distance[nx][ny][crashed]=distance[x][y][crashed]+1
                #(x,y)와 같은 상태 넣어줘야함
                queue.append((nx,ny,crashed))
            elif graph[nx][ny]==1 and crashed<K and distance[nx][ny][crashed+1]==-1:
                distance[nx][ny][crashed+1]=distance[x][y][crashed]+1
                queue.append((nx,ny,crashed+1))
    return -1



print(bfs(0,0))