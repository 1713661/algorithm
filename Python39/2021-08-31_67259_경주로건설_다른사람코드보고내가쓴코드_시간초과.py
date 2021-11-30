# visited for문안에서 확인해주면 큐에 들어가는 게 차이 나니까 틀린 값 나올 수도 있는듯
### 아냐 그게 아니라 마지막에 >cost라고 써서 그런 것 같은데?? cost+100이나 cost+600써줘야 하니까!!!! 
# 근데 그러면 이렇게 또 분기문 나뉠 바에 for문 앞에서 써주는 게 낫지
# 약간 다익스트라랑 비슷한 느낌. (큐에 있는 값이 최단거리테이블값보다 크면 볼 필요없다.. 이런식으로)
from collections import deque

def solution(board):
    N = len(board)
    
    q = deque()
    q.append((0,0,0,(1,1))) # x,y,cost,vec
    visited = {}
    visited[(0,0,(1,1))]=0 # 3차원 배열은 튜플 저장하기 힘드니 딕셔너리 쓰는거임

    
    dx = [0,0,1,-1] # 동서남북
    dy = [1,-1,0,0]
    
    answer = []
    
    while q:
        x,y,cost,vec = q.popleft()
        print("now=",x,y,"cost=",cost,"vec=",vec)
            
        for newdir in range(4): #동서남북
            nx = x+dx[newdir]
            ny = y+dy[newdir]
            if 0<=nx<N and 0<=ny<N and board[nx][ny]==0: ### 이거 조건문 계산하는 것땜에 시간초과 나오는듯. 
                if not (nx,ny,(dx[newdir],dy[newdir])) in visited or visited[(nx,ny,(dx[newdir],dy[newdir]))]>cost: # 이 코드 for문 안에서 쓰면 안되는 이유는?
                    if dx[newdir]*vec[0]+dy[newdir]*vec[1]==0: # 90도로 꺾이면 
                        ##180도로 바뀌는것도 생각해야됨!!!!!!! 그래서 벡터썼던거였음..
                        visited[(nx,ny,(dx[newdir],dy[newdir]))]=cost+600  ### 근데 이렇게 쓰는 것도 틀리다고 나옴. 그냥 다른사람코드보고 외우고 bfs 틀 감잡는 게 좋을듯
                        q.append((nx,ny,cost+600,(dx[newdir],dy[newdir])))
                    else:
                        visited[(nx,ny,(dx[newdir],dy[newdir]))]=cost+100
                        q.append((nx,ny,cost+100,(dx[newdir],dy[newdir])))
                        
    return [visited[(N-1,N-1,(dx[dir],dy[dir]))] for dir in range(4) if (N-1,N-1,(dx[dir],dy[dir])) in visited]

#print("1",solution([[0,0,0],[0,0,0],[0,0,0]]))
#print("2",solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print("3",solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
#print("4",solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))

print("expect 3000",solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]))