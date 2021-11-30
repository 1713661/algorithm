#### 벽을 조합으로 뽑는 거 말고 dynamic programming로 생각해보기!!!!!!
# jinhan814님도 완전탐색으로 풀었음
# 코드 짜는 데에 2시간 좀 안되게 걸린듯(graph 출력확인하고 combinations 라이브러리 쓰는 거에서 시간 많이 썼음)
# 벽 꼭 3개 설치해야 한다고 했으니 근처 8개 방향에 최소 1개 벽이 있어야하나?
# 아냐 파이썬 랭킹 높은 코드들도 결국엔 다 완전탐색하는거였음!!!!!!!!!!!!1

# 0은 빈 칸, 1은 벽, 2는 바이러스
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
# 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

# deepcopy 모듈은 굉장히 느리다고 합니다. 잠깐 검색만 해봐도 많이 느리다고 하는 결과를 볼 수 있습니다. 때문에 객체등을 복사할 때는 복사 메서드를 커스텀으로 만들어서 사용한다고 합니다.
# 결론적으로 배열의 깊은 복사를 사용할때는 slicing을 이용하시는걸 추천합니다.
import sys
#from copy import deepcopy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split()) #3<=세로,가로<=8

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
#print(graph)

# 0의 좌표 (x,y) 튜플을 리스트에 받아서 3개 조합 만든다음에 벽세우고(1로 바꾸고)
zeroList = []
for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            zeroList.append((i,j))
#print(zeroList)

walls_list = list(combinations(zeroList,3))
# walls_list=[((0, 1), (0, 2), (0, 3)), ((0, 1), (0, 2), (0, 6)),...]

def dfs(x,y,graph):
    for (nx,ny) in (x,y+1),(x,y-1),(x+1,y),(x-1,y): # 동서남북
        if 0<=nx<N and 0<=ny<M:
            if graph[nx][ny]==0:
                graph[nx][ny]=2 # 바이러스 퍼짐. !!!!! 이 코드는 for문위에 종료조건 안썼으니까 이렇게 값 바꿔줘도 될듯
                dfs(nx,ny,graph)


def buildWallandSpreadVirus(wall_tuples): # wall_tuples = ((0, 1), (0, 2), (0, 3))
    # 벽을 생성
    newgraph = [item[:] for item in graph]
    for wall_coord in wall_tuples: # wall_coord = (0, 1)
        wall_x,wall_y = wall_coord
        newgraph[wall_x][wall_y] = 1
    
    '''
    print("벽세움 wall_tuples",wall_tuples)
    for i in range(N):
        print(newgraph[i])
    print("\n")
    '''

    # 바이러스 퍼짐
    virusList = []
    for i in range(N):
        for j in range(M):
            if newgraph[i][j]==2: #바이러스이면
                virusList.append((i,j))
    
    for virus in virusList:
        dfs(virus[0],virus[1],newgraph) # 바이러스 퍼뜨리기

    '''
    print("바이러스 퍼진후 wall_tuples",wall_tuples)
    for i in range(N):
        print(newgraph[i])
    '''
    cnt = 0
    for i in range(N):
        for j in range(M):
            if newgraph[i][j]==0: #안전영역
                cnt += 1
    #print("cnt=",cnt)
    return cnt

def solution():
    MAX = 0
    for walls in walls_list: # walls = ((0, 1), (0, 2), (0, 3))
        count = buildWallandSpreadVirus(walls)
        MAX = max(MAX,count)
    print(MAX)
        
solution()


    
# 그때마다 안전 영역의 개수 세는 게 제일 나은 방법일까?