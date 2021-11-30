# 이 판다는 매우 욕심이 많아서 대나무를 먹고 자리를 옮기면 그 옮긴 지역에 그 전 지역보다 대나무가 많이 있어야 한다.
# 10분.. 졸리다 + 15분+9분
# BFS로 풀면 안되나? 구글링 해보니까 시간초과 난다고 함
# DP 테이블 쓰기!!!!!!!!

import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
dp = [ [1]*n for _ in range(n) ]

# 판다가 최대한 많은 칸을 방문할 수 있는지 고민에 빠져 있다.

def dfs(x,y):
    for (nx,ny) in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]>graph[x][y]:
            dp[x][y] = max(dp[x][y],dfs(nx,ny)+1)
    return dp[x][y] ##############cnt가 아님!!!!!


for i in range(n):
    for j in range(n):
        result = max(result,dfs(i,j))
print(result)
for i in range(n):
    print(dp[i])

