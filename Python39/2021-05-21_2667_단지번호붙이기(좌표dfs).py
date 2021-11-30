import sys
input = sys.stdin.readline

N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int,input().rstrip())))
#print(graph)

list = []
cnt = 0
def dfs(x,y):
    if x<0 or y<0 or x>=N or y>=N:
        return False
    if graph[x][y]==1:
        #print(x,',',y)
        global cnt
        cnt += 1
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
        
        

result = 0
for i in range(N):
    for j in range(N):
        if dfs(i,j)==True:
            list.append(cnt)
            cnt = 0
            result += 1
print(result)
list.sort() #오름차순 정렬(문제 똑바로 보기!!!!!!!!)
for l in list:
    print(l, end='\n')
    
    
