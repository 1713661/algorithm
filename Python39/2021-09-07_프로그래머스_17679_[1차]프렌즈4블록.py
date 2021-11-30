# 34분 fall()함수 괜히 만든듯
# 37분 처음부터 다시해야지.. 실전에서 이러면 안되는데.. (rotate함수짜려고했는데 더 산으로 가는 것 같아서 포기)
# +23분 악! 이렇게 푸는 게 맞나? 구현할 거 많아서 짜증나
# +23분 while문 포함 겨우겨우 구현..(실전에서도 이러면 안되는데)
# 내 코드에 확신이 없으니까 하나하나 print문으로 확인하게 되고, 그러니까 시간 오래걸리는듯
# +20분
def solution(m, n, board): #높이,폭

    def fall():
        revise = [[] for j in range(n)]
        for j in range(n):
            for i in range(m):
                if board[i][j]=='x':
                    revise[j].append(i)
        return revise
    for i in range(m):
        board[i] = list(map(str,board[i])) ###########
    '''
    for i in range(m):
        print(board[i])
    '''

    cnt = 0
    while True: 
        delete = set()
        for x in range(m):
            for y in range(n):
                if 0<=x<m-1 and 0<=y<n-1:
                    if board[x][y]==board[x][y+1]==board[x+1][y]==board[x+1][y+1] and board[x][y]!='x':
                        delete.add((x,y, x,y+1, x+1,y, x+1,y+1))
        #print("delete=",delete)
        if len(delete)==0: break
        for d in delete:
            for i in range(0,8,2):
                if board[d[i]][d[i+1]]!='x':
                    board[d[i]][d[i+1]]='x'
                    cnt += 1
        
        print("afterdelete")
        for i in range(m):
            print(board[i])
        
        same = 0
        arr = fall()
        #print("arr=",arr)
 
        for j in range(n): 
            if len(arr[j])==0 or len(arr[j])==n:
                same += 1
            else:
                for i in range(arr[j][-1],-1,-1):
                    idx = i
                    if board[i][j]=='x':
                        continue
                    else:
                        while board[idx+1][j]=='x':
                            idx += 1
                            if idx==m-1: break
                        board[idx][j]=board[i][j]
                        board[i][j]='x'
        '''
        print("afterfall")
        for i in range(m):
            print(board[i])
        '''

        if same == n:
            break      

    return cnt

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"])) #높이,폭 2 ≦ n, m ≦ 30 900*4 완전탐색 충분히가능
# 14
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]) ) 
# 15