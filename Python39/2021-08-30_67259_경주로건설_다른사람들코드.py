from collections import deque

#### 이코드 공부하기!!!!
dr, dc = (-1,1,0,0), (0,0,-1,1)#udlr
def solution(board0):
    n = len(board0)
    board = [[1 for x in range(n+2)] for xx in range(n+2) ]
    for r in range(n):
        for c in range(n):
            board[r+1][c+1] = board0[r][c]
    answer = 0

    q= [(0,(1,1),(1,1))]
    q = deque(q)
    visited = {} # 아 나는 (r,c,vec) for문 어떻게 돌려야지.. 하고 있었는데 딕셔너리 쓰면 되는거였음
    # 25*25*4 = 2500이니까 완전가능??
    while q:
        cnt,cur,vec = q.popleft()
        # cnt,cur,vec = heappop(q)
        r,c = cur

        if (r,c,vec) in visited and visited[(r,c,vec)] <= cnt:
            continue
        visited[(r,c,vec)]=cnt

        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]            
            dot = vec[0]*dr[d] + vec[1]*dc[d]

            if board[nr][nc]<1:
                if dot==0: #90도로 꺾이면
                    q.append((cnt+100+500,(nr,nc),(dr[d],dc[d])))
                    # heappush(q, (cnt+100+500,(nr,nc),(dr[d],dc[d])))
                else:
                    q.append((cnt+100,(nr,nc),(dr[d],dc[d])))
                    # heappush(q, (cnt+100,(nr,nc),(dr[d],dc[d])))
    # print(visited)  
    return min([visited[(n,n,(dr[x],dc[x]))] for x in range(4) if (n,n,(dr[x],dc[x])) in visited])

def solution2(board):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    answer = []

    N = len(board)
    start, end = (0, 0), (N - 1, N - 1)
    costs = [[float('inf')] * N for _ in range(N)]

    deq = deque()
    deq.append((0, 0, 0, 1))
    deq.append((0, 0, 0, 3))
    costs[0][0] = 0
    while deq:
        x, y, cost, dir = deq.popleft()
        if x==N-1 and y==N-1: 
            answer.append(cost)
            continue
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            tmp_cost = cost + 100 if dir == k else cost + 600
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 0 and tmp_cost <= costs[nx][ny]:
                    costs[nx][ny] = tmp_cost
                    deq.append((nx, ny, tmp_cost, k))

    return min(answer)

print("1",solution([[0,0,0],[0,0,0],[0,0,0]]))
print("2",solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print("3",solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print("4",solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))

print("expect 3000",solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]))