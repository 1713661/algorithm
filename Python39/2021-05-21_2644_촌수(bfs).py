import sys
from collections import deque 
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

x,y = map(int,input().split())

for _ in range(int(input())):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
print(graph)

visited = [False]*(n+1)
kin = [0]*(n+1)
#dfs/bfs 둘 다 구현 가능한듯
def bfs(i):
    queue = deque([i])
    visited[i] = True
    #print(queue)
    while queue:
        i = queue.popleft()
        #print(i, end=' ')
        if i==y: return kin[i]
        for g in graph[i]:
            if not visited[g]:
                visited[g]=True
                queue.append(g)
                kin[g] = kin[i]+1
                print(kin)
    return -1

print("kin=",bfs(x))
       
    
    
        
    
'''
def dfs(i):
    global cnt
    #print(i)
    visited[i]=True
    for g in graph[i]:
        if g==b: return cnt
        if not visited[g]:
            cnt += 1
            print(cnt)
            dfs(g)
        
print("cnt=", dfs(x))
'''
