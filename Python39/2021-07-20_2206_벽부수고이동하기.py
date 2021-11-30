####### 벽 뚫은 경로 버리는 경우 잘 생각해야!!!

# bfs queue.append할 때 벽 부쉈는지상태도 같이 넣어야할듯
###### graph[N-1][M-1]에 최솟값이 아닌 경우가 되는 경우는 없음(BFS 기본 원리!!!!! 생각을 해 생각을)
# 따라서 '벽을 부쉈는데 그 길이 아닌 경우 check=False로 바꿔준다' -> 이런거필요없음


#### 7/19(월) 오후 11:36 내가 푼 코드는 돌아서 가는 경우 
# "if graph[nx][ny][1]==0: # 갈 수 있는 곳이고 처음 방문한 경우 (2 이상인건 방문했다는 뜻이니까)"에서 잡지 못하기 때문에 틀린 답 나오는듯
# 벽뚫고 온애를 버려야 하는데 혹시 몰라서 버리지 못하는.. -> 버리는 방법: 밑에 처럼 두가지 경우 다 저장하기
# 그래서 graph로만 해결하려고 하면 안되고 graph는 2차원으로 두고 visited를 3차원으로 만들어야 되는듯
# 분기점으로 돌아갈 때 모든 상태를 얻으려면 graph 3차원만으로는 부족함(crashed 상태 뿐만 아니라 visited(거리)값까지 얻어야함)(crashed냐 아니냐에 따라 visited값달라짐)
# visited[x][y][0]='벽을 부순 적이 없을 때의' 최단 경로
# visited[x][y][1]='벽을 한번 부순 적이 있을 때의' 최단 경로


import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split()) #세로의크기,가로의크기

graph=[]
for _ in range(N):
    graph.append(list(map(int,input().rstrip()))) #데이터 띄어쓰기 안하고 주어지면 split() 못씀!!!!!!!!(왜자꾸까먹니)
#print(graph)

def bfs(x,y):
    distance = [ [[0,0] for _ in range(M)] for _ in range(N)]
    '''
    for i in range(N):
        print(distance)
    '''
    queue = deque()
    queue.append((x,y,0))
    while queue:
        x,y,crashed = queue.popleft() # crashed==0 벽 아직 안부숨/ ==1 벽 한번 부숨
        #print("now=",x,y,"crashed=",crashed)
        #print(queue)
        if x==N-1 and y==M-1:
            return distance[x][y][crashed]+1
        for (nx,ny) in (x,y+1),(x,y-1),(x+1,y),(x-1,y): # 동서남북
            #print("(nx,ny)=",nx,ny,"crashed=",crashed)
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if graph[nx][ny]==0 and distance[nx][ny][crashed]==0: #새로 탐색한 칸이 갈 수 있는 칸이면 ##### 뒤에 distance도 꼭 붙여줘야함!!!!!
                ############## distance 배열까지 확인해야함
                #print("(nx,ny)=",nx,ny,"crashed=",crashed)
                distance[nx][ny][crashed] = distance[x][y][crashed]+1
                #print("hi crashed=",crashed)
                queue.append((nx,ny,crashed))
                #(x,y)랑 같은 상태의 crashed 넣어야함

            elif graph[nx][ny]==1 and crashed==0 and distance[nx][ny][crashed+1]==0: # 벽이고 부술 수 있는 상태고 처음 가는 칸이면 distance 조건까지 붙여야 시간줄일 수 있음
                distance[nx][ny][1] = distance[x][y][0]+1
                queue.append((nx,ny,1))
                
        #graph[x][y]=-1 # 이미 방문한 칸은 -1로 바꾸기
        #print("queue after for loop=",queue)
    return -1
            
print(bfs(0,0))

'''
반례입니다.

열심히 노력하면 (벽을 딱 1개만 부수는 이 문제에 한해서) 3차원배열을 안쓰고 풀 수 있는 방법이 있습니다.

1
5 5
2
00000
3
11101
4
00001
5
01111
6
00010
luniro   6달 전좋아요
벽을 10개까지 부수는 벽 부수고 이동하기2까지도 2개의 2차원배열로 풀 수 있기는 합니다'''
