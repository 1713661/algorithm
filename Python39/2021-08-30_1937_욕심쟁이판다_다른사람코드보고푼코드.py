import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # depth 제한하는 게 아니라 늘리는거였음!
'''
런타임에러 원인은 파이썬에서 디폴트로 최악의 경우인 25000( 500x500)정도의 recursion depth를 허용하지 않습니다.
그래서 recursion depth를 늘려줘야함
이렇게 상위에서 설정하시면 런타임에러 해결하실수 있습니다.
'''
'''
최장거리를 구해야하기 때문에 방문했던 곳을 또 방문해야할지 모릅니다.
예를 들어 2-1을 먼저 방문해서 1에서의 최장거리를 2라고 계산한 상태에서 4-3-1이라는 경로가 있을 경우 1에서의 최장거리가 3이라고 판단하지 못합니다.
dfs와 dp를 통해 답을 구하거나 말단 노드부터 역으로 계산하시는걸 추천합니다.
'''

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dp = [[0]*n for _ in range(n)] 

def dfs(x,y):
    if dp[x][y]: return dp[x][y]
    dp[x][y]=1
    for (nx,ny) in (x,y+1),(x,y-1),(x+1,y),(x-1,y): #동서남북
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]>graph[x][y]:
            dp[x][y] = max(dp[x][y],dfs(nx,ny)+1)
    return dp[x][y]

result = 0
for i in range(n):
    for j in range(n):
        result = max(result,dfs(i,j))
print(result)

