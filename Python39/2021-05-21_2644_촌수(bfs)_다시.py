import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
x,y = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
kin = [0]*(n+1)
for _ in range(int(input())):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

def bfs(i):
    queue = deque([i])
    while queue:
        x = queue.popleft()
        if x==y: return kin[x]
        for g in graph[x]:
            if not visited[g]:
                visited[g] = True
                queue.append(g)
                kin[g] = kin[x]+1
    return -1
print(bfs(x))
