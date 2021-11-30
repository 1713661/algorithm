# board에서 비교하는게아니라 newboard로 끌고와서 비교(이렇게되면 코드 훨씬 깔끔함. prev도 쓸필요없음)
# brute말고 dfs도 쓸수있음(재귀함수너무어려워..) 재귀함수 리턴값은 마지막 리턴값만 유효한듯??
# 생각의 전환 필요해!!!!!!
# 24분
def tilt(board):
    newboard = [ [0]*N for _ in range(N)]

    for c in range(N):
        idx = 0 # newboard에 값이 들어올수있는 가장작은인덱스
        for r in range(N):
            if board[c][r]==0: continue

            if newboard[c][idx]==0:             # 빈칸이면
                newboard[c][idx]=board[c][r]    # 일단 그 인덱스에 r값 넣어야함

            elif board[c][r]==newboard[c][idx]: # 숫자같으면
                newboard[c][idx] *= 2           # 합침
                idx += 1                        # 값이 들어올수있는 가장작은인덱스는 하나증가해야함

            else:                               # 숫자다르면
                idx += 1                        # 다음인덱스에 값넣어야함
                newboard[c][idx]=board[c][r]
    return newboard

def rotate(board): #시계반대방향으로 회전
    newboard = [ [0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            newboard[i][j]=board[j][N-1-i]
    return newboard

def dfs(board,depth):
    global MAX

    if depth>5:
        MAX = max(MAX,max(map(max,board))) ###########2차원배열의최댓값구하는법 -> map함수사용
        return 

    for _ in range(4):
        newboard = rotate(board)
        board = newboard #다음번 돌때 재활용하기위해 할당
        newboard = tilt(newboard)
        dfs(newboard,depth+1)



N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

MAX = 0
dfs(board,1)
print(MAX)


