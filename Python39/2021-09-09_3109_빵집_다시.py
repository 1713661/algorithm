################## 위쪽((x-1,y+1))부터 탐색하면 return False일때 visited수정할필요없음
############ 파이프 개수의 최댓값을 구하는거기 때문에 파이프 일단 다 놔야함
import sys
input = sys.stdin.readline

R,C = map(int,input().split()) # 1 ≤ R ≤ 10,000, 5 ≤ C ≤ 500

board = []
for _ in range(R):
    board.append(list(map(str,input().rstrip())))
print(board)
#  '.'는 빈 칸이고, 'x'는 건물
# 처음과 마지막 열은 항상 비어있다.
# 파이프라인의 최대 개수를 출력

# 각 칸을 지나는 파이프는 하나이어야 한다.
### 블로그 내용 https://suri78.tistory.com/187
# 항상 solve()의 결과가 False이면 visit[][]의 값을 False로 바꿔주었는데, 그럴 필요가 없었다.
# 한번 해당 지점을 방문해서 원웅이의 빵집에 도달했으면 
# 이미 연결된 경로이기 때문에 파이프를 둘 수 없는 지점이 되며, 
# 해당 지점을 방문한 이후 원웅이의 방집까지 도달하지 못했으면 
# 또다시 해당 지점에 방문했을 때도 마찬가지로 원웅이의 빵집까지 도달할 수 없기 때문이다.
'''
#https://blog.naver.com/PostView.naver?blogId=jinhan814&logNo=222491650796&categoryNo=11&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=search
이러면 당연히 파이프를 최대한 위쪽으로 밀어서 건설하는게 항상 이득입니다. 
증명은 exchange argument를 이용하면 간단한데, 
만약 파이프를 ---과 같이 건설했을 때가 최적해이면서 위쪽으로 건설할 수 있었다면 
-^-과 같이 건설하는게 더 좋은 해이거나 ""동일한 해""입니다. <- 생각을 하자 생각을

이때 이걸 직접 모든 파이프를 건설해보면서 구현하면 """당연히""" 안되고, ############ 반성하자
현재 칸이 (x, y)일 때 파이프를 연결할 수 있는지 여부를 효율적으로 알아내야 합니다. 
이건 파이프의 왼쪽 상태와 무관하게 
한 번이라도 (x, y)에서부터 오른쪽으로 파이프를 연결할 수 없었다면
(x, y)을 지나는 파이프는 무조건 완성할 수 없다는 사실을 이용하면 됩니다. ####### y==C-1부터 생각

즉, DFS(x, y)가 (x, y)에서 출발해서 파이프를 만들 수 있는지 여부를 반환하도록 하면서 만약 만들 수 있다면 
최대한 위쪽에 붙어서 만들도록 하면 됩니다.
'''

visited = [[False]*C for _ in range(R)]

####### y==C-1부터 생각 
def setPipe(x,y):

    if y==C-1: return True

    # 오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선으로 연결 
    for (nx,ny) in (x-1,y+1),(x,y+1),(x+1,y+1): # 이러면 당연히 파이프를 최대한 위쪽으로 밀어서 건설하는게 항상 이득(생각을해생각을)
        if 0<=nx<R and board[nx][ny]=='.' and not visited[nx][ny]:
            visited[nx][ny]=True
            if setPipe(nx,ny):
                return True
    return False  
    
answer = 0
for x in range(R):
    if setPipe(x,0): 
        answer += 1
print(answer)

for i in range(R):
    print(visited[i])



