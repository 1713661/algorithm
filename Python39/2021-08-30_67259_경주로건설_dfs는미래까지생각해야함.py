# 17분정도??(중간에 타이머 다시 안킴ㅠ) 초벌 만들었는데 맞는지는 모르겠다...
# dfs는 최소거리 찾지 못함!!!!!!!!!!!!!!!!!!!!!!! 돌아가더라도 최소거리로 가야하는거면 bfs로 푸는 게 맞음

# 0초부터 다시 셌음
# 19분 costs 원소 가리키는 idx 이용해서 구하려고 했는데 아닌 것 같음...(이틀 후에 보니 이거 무슨 말인지 모르겠다)
# 31분 악!!!!!!!! 왜 cost[x][y]마다 저장할 생각을 안했지?????? 나 이 유형 항상 까먹는다.. 이 문제는 이렇게 풀면 될 것 같고, N-Queen 문제(백트래킹) 복습하자!!!
# +12분 잠깐.... bfs로 풀어야할 것 같은데.. 망했다 하..... 
##### 검색해보니 bfs로 푸는 게 맞는 것 같다

# dfs로 풀면 테스트케이스3의 경우 미래에 발생할 수 있는 비용차이까지 고려해야함
# 그래서 road[x][y]=(straight,corner) 이런식으로 튜플로 관리하려고 하면 pop,append 하는거 번거로움
# 비용이 같을 경우 road에 새로운 튜플 넣어주는 게 맞는 것 같은데, 그러면 dfs를 쓰는 메리트가 없어지는 것 같다.
# 따라서 bfs로 푸는 게 맞는 것 같다....(근데 이건 bfs도 마찬가지. 그리디적으로 풀면 안된다. 끝날때까지 끝난 게 아니다)
# 실전에서는 이를 어떻게 생각해야할까? dfs가 맞는 것 같아서 dfs로 풀었는데 bfs로 푸는 게 맞는 방법이었을때......... 왠만하면 dfs보단 bfs쓰는게나은것같다

INF = int(10e9)
def solution(board):
    N = len(board)
    answer = []
    # costs = [0]*(N*N) ##### 경로 몇개까지있을수있지?
    cost=[ [INF]*N for _ in range(N)]
    cost[0][0]=0
    dx = [0,1,0,-1] # 동남서북
    dy = [1,0,-1,0] 

    def dfs(x,y,dir):
        #print("now=",x,y,"cost=",cost[x][y])

        if x==N-1 and y==N-1:
            answer.append(cost[x][y])

        for newdir in range(4):
            nx = x+dx[newdir]
            ny = y+dy[newdir]
            if 0<=nx<N and 0<=ny<N and board[nx][ny]==0:
                if newdir==dir: #직선도로이므로 cost==100
                    if cost[nx][ny]>=cost[x][y]+100: 
                        # 최소거리가 아니면 자동으로 소멸... 근데 이렇게 그리디적으로 보면 안돼...
                        cost[nx][ny]=cost[x][y]+100
                        dfs(nx,ny,newdir)
                else:
                    if (nx+ny)==1:
                        cost[nx][ny]=cost[x][y]+100
                        dfs(nx,ny,newdir)
                    elif cost[nx][ny]>=cost[x][y]+600:
                        cost[nx][ny]=cost[x][y]+600 #코너+진행비용
                        dfs(nx,ny,newdir)
                    
                    # return
                    # 여기서 리턴안하면 (5,4)에서 분기한 코드가 (0,0)까지 가서 cost[0][0]=6000으로 초기화한 다음에 파란경로를 가기때문에
                    # 파란경로가 (1,0)을 가려고 하면 조건 아무것도 만족 못함
                    # return 남발하면 안됨!!!!!!!!!!!!!!!!!
    
    # if (nx+ny)==1 안쓰려고.... 처음에 모든 방향에 대해 탐색
    # 근데 그럼 처음에 다른 방향으로 가는 경우는 막아야해서 어차피 코드 더 써야함.. 
    # 그냥 (nx+ny)==1 쓰기.....
    dfs(0,0,0) # 동 #x,y,direction,cost(현재경로의개수)
    return min(answer)

# 44분(망했으..) (straight,corner) 백트래킹으로 푸는 거 어렵나?
# road = [ [[0,0] for _ in range(N)] for _ in range(N)] 
# 얘도 마찬가지. 
############### 결국 비용이 같으면 road.append(straight,corner)해야하는데 만만치 않음
############## 백트래킹 말고는 왠만하면 dfs/bfs 중 bfs쓴다고 생각하기
def solution2(board):
    N = len(board)

    dx = [0,0,1,-1] #동서남북
    dy = [1,-1,0,0]
        
    answer = []
    road = [ [[0,0] for _ in range(N)] for _ in range(N)] 
    # 나중에 값 쉽게 변경하기 위해서 tuples대신 리스트 씀

    def dfs(x,y,dir,straight,corner):
        if x==N-1 and y==N-1:
            answer.append((straight,corner))
            return
                
        print("now=",x,y,"straight=",straight,"corner=",corner)

        for newdir in range(4):
            nx = x+dx[newdir]
            ny = y+dy[newdir]
            if 0<=nx<N and 0<=ny<N and board[nx][ny]==0:
                if newdir==dir:
                    if (straight+6*corner)<(road[x][y][0]+6*road[x][y][1]):
                        road[nx][ny][0]=road[x][y][0]+1
                        road[nx][ny][1]=road[x][y][1]
                        dfs(nx,ny,newdir,straight+1,corner)
                    else:
                        return
               
                else:
                    if (nx+ny)==1:
                        if (straight+6*corner)<(road[x][y][0]+6*road[x][y][1]):
                            road[nx][ny][0]=road[x][y][0]+1
                            road[nx][ny][1]=road[x][y][1]
                            dfs(nx,ny,newdir,straight+1,corner)
                        else:
                            return
 
                    else:
                        if (straight+6*corner)<(road[x][y][0]+6*road[x][y][1]):
                            road[nx][ny][0]=road[x][y][0]
                            road[nx][ny][1]=road[x][y][1]+1
                            dfs(nx,ny,newdir,straight,corner+1)
                        else:
                            return
       
    dfs(0,0,4,0,0) #x,y,dir,road,straight,corner
    return answer
    


print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))