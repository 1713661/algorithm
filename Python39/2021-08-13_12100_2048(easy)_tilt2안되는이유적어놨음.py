# 아 나는 board에서 비교해서 넣을 생각했는데 barkingdog님은 newboard로 끌고와서 비교(이렇게되면 코드 훨씬 깔끔함)
# 생각의 전환 필요해!!!!!!

# 8분 왜 난 이렇게 생각하지 못했을까?
def tilt(board):
    newboard = [[0]*N for _ in range(N)]
    
    for c in range(N):
        idx = 0 # newboard 배열에서 어디에 삽입해야 하는지 가리키는 변수
        for r in range(N):
            if board[c][r]==0: continue

            if newboard[c][idx]==0: 
                newboard[c][idx] = board[c][r]
            elif newboard[c][idx]==board[c][r]: ####### 이렇게 비교하면 prev 쓸필요없음!!!!! 왜 이 생각을 못했을까?
                newboard[c][idx] *= 2
                idx += 1                # 이렇게되면 8 8 16 이런식이어도 16이 또 합쳐지지 않음(idx가 다음으로 넘어갔으니까)
            else: # 다른값인경우
                idx += 1
                newboard[c][idx] = board[c][r]
    return newboard

def tilt2(board): #이코드 틀렸습니다 나옴..깔끔하게잊자 어떻게생각해도수습할방법이안떠오름(분기가 많은 코드기 때문에 절대 좋은 코드가 아님)

    newboard = [ [] for _ in range(N)]

    for c in range(N):
        r=N-1
        # 한 가로줄에서 처음으로 0이 아닌 수를 저장
        for i in range(N):
            if board[c][i]==0: continue
            prev = board[c][i] 
            r = i+1
            break
        #print("r=",r)

        while r<N: #for r in range(idx,N): 
            if board[c][r]==0:
                r += 1
                continue
            if board[c][r]==prev:
                newboard[c].append(board[c][r]*2)
                if r<N-1: 
                    prev = board[c][r+1] #인덱스에러때문에 조건문넣음
                r += 2 # prev 건너뛰고 탐색 여기서 건너뛰어서
                '''
                beforeTilt
         [2, 2, 2]        
         [2, 2, 2]        
         [2, 2, 2]        
        afterTilt
         [4, 0, 0]        
         [4, 0, 0]        
         [4, 0, 0] '''   #이렇게나오는거임

            elif board[c][r]!=prev:
                newboard[c].append(prev)
                if r==N-1: #마지막칸일 때에만 넣어야함
                    newboard[c].append(board[c][r]) 
                prev = board[c][r]
                r += 1

        newboard[c].extend([0]*(N-len(newboard[c])))

    return newboard


def rotate(board): #반시계방향으로 90도회전
    newboard = [[0]*N for i in range(N)] 
    for i in range(N):
        for j in range(N):
            newboard[i][j]=board[j][N-1-i]
    return newboard

def dfs(graph,depth):
    global MAX
    if depth > 5:
        #MAX = max(MAX,max(map(max,graph))) ####
        return max(MAX,max(map(max,graph)))
        
    for i in range(4):
        newgraph = rotate(graph)
        graph = newgraph #for문 돌때마다 한번씩만 돌리기 위해
        newgraph = tilt2(newgraph)
        dfs(newgraph,depth+1)

N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

MAX = 0
item = dfs(board,1)
print("item=",item)
#print(MAX)