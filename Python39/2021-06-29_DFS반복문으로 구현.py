from collections import deque

stack = deque()
visited = [False]*9
'''
def dfs:
    visited[start] = True
    stack.push(start)
    k=start
    for i in graph[k]:
        if not visited[i]:
            visited[i] = True
            stack.push(k)
            continue
        stack.pop()
'''
'''
def dfs():
    while stack:
        k = stack.pop()
        #for i in graph[k]: ###########while문으로 구현하면 for문 쓸 필요가 없지!!!! 생각을 해 생각을!!!!!
            if not visited[i]:
                visited[i]=
                
                stack.push(i)
'''
def dfs():
    stack = [1] ###deque는 배열형태임. 'int' object is not iterable
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(node,end=' ')
            stack.extend(graph[node]) ###중요!!! ###얘가 for문 역할 하는거지!!!! stack.extend(node)가 아니라 stack.extend(graph[node])인거임!!!!!!
    return

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
dfs()
