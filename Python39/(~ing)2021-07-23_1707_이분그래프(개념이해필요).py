########## 문제이해 완전 잘못했었음.. 이따 다시 풀기!!!!(44분 씀)

# 일단 한 점 찍고 BFS 해서 집합 만든다음에 
# 그 집합에 속하지 않는 점들끼리도 묶을 수 있는지 보면 되나?
# 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때 -> 그러니까 모든 간선의 꼭지점 2개가 서로 다른 집합에 속해야 한다는 말
# 번역해서 잘 못알아들었음.. 그냥 "이분그래프" 정의 잘 알고있어야할듯!!!!

import sys
input = sys.stdin.readline

# K = int(input()) # 테스트케이스 개수 (2≤K≤5)

def dfs(node):
    global graph
    global visited
    for nextnode in graph[node]:
        if not visited[nextnode]:
            visited[nextnode]=True
            #print(nextnode,end=' ')
            dfs(nextnode)



#dfs로 구현해보기???
#def IsBipartite(graph):
    
for _ in range(int(input())):
    V,E = map(int,input().split()) #정점,간선개수 1≤V≤20,000 1≤E≤200,000
    graph=[[] for _ in range(V+1)] #정점개수만큼 배열 초기화
    for _ in range(E): #간선에대한정보(각 줄에 인접한 두 정점의 번호가 주어짐)
        N,M = map(int,input().split())
        graph[N].append(M)
        graph[M].append(N)
    #print(graph)
    cnt=0
    visited = [False]*(V+1) #1차원배열인거 까먹으면 안됨!!
    for start in range(1,V+1):
        if not visited[start]:
            visited[start]=True
            #print(start,end=' ')
            dfs(start)
            #print("\n")
            cnt += 1
    if cnt==2:
        print("YES")
    else:
        print("NO")
        
    


