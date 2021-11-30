# 23분
def solution(m, n, board): # 높이,폭

    for i in range(m):
        board[i] = list(map(str,board[i])) ######
    
    cnt = 0

    while True:
        deletes = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]!='x'and board[i][j]==board[i][j+1]==board[i+1][j]==board[i+1][j+1]:
                    deletes.append([(i,j), (i,j+1), (i+1,j), (i+1,j+1)])
        
        if len(deletes)==0: break

        Xs = [[] for _ in range(n)]
        for delete in deletes:
            for d in delete:
                if board[d[0]][d[1]]!='x':
                    board[d[0]][d[1]]='x'
                    Xs[d[1]].append(d[0])
                    cnt += 1

        print(Xs)

        M = [max(Xs[j]) if len(Xs[j])!=0 else -1 for j in range(n)]

        #print(M) [2, 3, 3, 0, 2, 2]

        for j in range(n):
            for i in range(M[j],-1,-1):
                if board[i][j]=='x': continue
                idx = i
                while idx<M[j] and board[idx+1][j]=='x':
                    idx += 1
                board[idx][j]=board[i][j]
                board[i][j]='x'

        # M 안쓴 버전
        '''
        for j in range(n):
            for i in range(m-1,-1,-1):
                if board[i][j]=='x': continue
                idx = i
                while idx<m-1 and board[idx+1][j]=='x':
                    idx += 1
                if idx!=i:
                    board[idx][j]=board[i][j]
                    board[i][j]='x'
        '''
        
        print("afterfall")
        for i in range(m):
            print(board[i])
            
        
        

    return cnt
   

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"])) #높이,폭 2 ≦ n, m ≦ 30 900*4 완전탐색 충분히가능
# 14
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]) ) 
# 15