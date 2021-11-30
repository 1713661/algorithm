import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split()) 
    graph[x].append(y) 
    graph[y].append(x)  # 내가 배운 방식대로는 값 중복해서 넣어야함!
    graph[x].sort()
    graph[y].sort()     # 정렬해줘야함 흠.. 이거 데이터 많아지면 오래 걸릴 것 같은데
    
# print(graph)

visited_d = [False] * (n+1)
def dfs(graph, x, visited_d):
    visited_d[x] = True
    print(x, end=' ')
    for i in graph[x]:
        if not visited_d[i]:
            dfs(graph, i, visited_d)


visited_b = [False] * (n+1)
def bfs(graph, start, visited_b):
    queue = deque([start])
    visited_b[start] = True
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if not visited_b[i]:
                queue.append(i)
                #print(queue)
                visited_b[i] = True
                
dfs(graph, v, visited_d)
print()
bfs(graph, v, visited_b)
