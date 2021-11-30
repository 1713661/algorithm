node = int(input())
edge = int(input())

graph = [[] for _ in range(node+1)]
for _ in range(edge):
    n, m = map(int,input().split())
    graph[n].append(m) #중복해서 넣어주고 정렬하는 것 잊지말기!
    graph[m].append(n)
    graph[n].sort()
    graph[m].sort()
    
cnt = -1
visited = [False] * (node+1)
def dfs(graph, node, visited):
    global cnt      #전역변수 사용하기!
    #print(node, end=' ')
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            cnt += 1
            dfs(graph, i, visited)
    return cnt
print(dfs(graph, 1, visited))


