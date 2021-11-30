graph1 = [["INF" for _ in range(5)] for _ in range(5)]
graph2 = [["INF"*5 ] for _ in range(5)]
graph3 = [["INF"]*5 for _ in range(5)]
graph4 = ["INF"*3]
graph5 = ["INF" for _ in range(5) for _ in range(5)] #[]안붙여주면 2차원 배열 안됨!! 생각을 해 생각을
graph6 = [1,2,3]

print(graph1)
[['INF', 'INF', 'INF', 'INF', 'INF'], ['INF', 'INF', 'INF', 'INF', 'INF'], ['INF', 'INF', 'INF', 'INF', 'INF'], ['INF', 'INF', 'INF', 'INF', 'INF'], ['INF', 'INF', 'INF', 'INF', 'INF']]
print(graph2)
[['INFINFINFINFINF'], ['INFINFINFINFINF'], ['INFINFINFINFINF'], ['INFINFINFINFINF'], ['INFINFINFINFINF']]
print(graph3) #출력은 graph1과 똑같이 나오는데 레퍼런스 참조vs값 복사 차이있을듯
[['INF', 'INF', 'INF', 'INF', 'INF'], ['INF', 'INF', 'INF', 'INF', 'INF'], ['INF', 'INF', 'INF', 'INF', 'INF'], ['INF', 'INF', 'INF', 'INF', 'INF'], ['INF', 'INF', 'INF', 'INF', 'INF']]
print(graph4)
['INFINFINF']
print(graph5)
['INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF', 'INF']

for g in graph6:
    g=4             #이런식으로 하면 값 안바뀜!!!!!!!
print(graph6)
'''
graph = [ [] for _ in range(N)]
for i in range(N):
    graph[i].append(list(map(int,input().split()))) #파이썬문법노트다시보기!
print(graph) 
#[[[0, 0, 0, 0, 0, 0, 0]], [[0, 2, 4, 5, 3, 0, 0]], [[0, 3, 0, 2, 5, 2, 0]], [[0, 7, 6, 2, 4, 0, 0]], [[0, 0, 0, 0, 0, 0, 0]]] 
'''
'''
N,M = map(int,input().split())

graph=[ [[False] for _ in range(M)] for _ in range(N) ]
for i in range(N):
    temp = list(map(int,input().rstrip()))
    for j in range(M):
        graph[i][j].append(temp[j]) #데이터 띄어쓰기 안하고 주어지면 split() 못씀!!!!!!!!(왜자꾸까먹니)

for i in range(N):
    print(graph[i])
'''