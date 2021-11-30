# 네트워크의 개수(덩어리개수구하기)를 return 하도록 
# 일단 dfs로 구현하고, bfs로 어떻게 구하는지도 찾아보기
# 13분(무난)
def dfs(node,graph,visited):
    visited[node] = True
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt,graph,visited)

def solution(n, computers):
    graph=[ [] for _ in range(n) ]
    visited = [False]*n
    for i in range(n):
        for j in range(i+1,n):
            if computers[i][j]==1:
                graph[i].append(j)
                graph[j].append(i)
    # print(graph)

    cnt = 0
    for i in range(n):
        if not visited[i]:
            dfs(i,graph,visited)
            cnt += 1
    return cnt

'''
# 프로그래머스 tjrwnwkd21님 풀이
def solution(n, computers):
    temp = []
    for i in range(n):
        temp.append(i)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]
    return len(set(temp))
'''

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))