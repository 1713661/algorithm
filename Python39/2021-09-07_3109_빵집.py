import sys
input = sys.stdin.readline

R,C = map(int,input().split()) # 1 ≤ R ≤ 10,000, 5 ≤ C ≤ 500
# 첫째 열은 근처 빵집의 가스관이고, 마지막 열은 원웅이의 빵집이다.????
# '.'는 빈 칸이고, 'x'는 건물이다. 처음과 마지막 열은 항상 비어있다.
# 파이프라인을 최대한 여러 개 설치할 것이다. 
# 이 경로는 겹칠 수 없고,서로 접할 수도 없다. 
# 즉, 각 칸을 지나는 파이프는 하나이어야 한다.
## 11분 일단 경로를 다 구하고 경로 가능 조합 구해야하나? 일단 해보자!
# 47분 풀이 구글링 하니까 난 항상 너무 어렵게가려고 그래...
######### 불량 사용자랑 다르게 얘는 nxt_route의 point들 하나하나 확인해야하기 때문에 백트래킹 어려움.. 이 방법 포기하자
### route하나 완벽히 일치하는 게 아니라 포인트 하나라도 겹치면 안되니까
board = []
for _ in range(R):
    board.append(list(map(str,input().rstrip())))

for i in range(R):
    print(board[i])

routes_list = [ set() for _ in range(C) ]
def findRoute(startX,x,y,route):
    if y==C-1:
        routes_list[startX].add(tuple(route[:]))
        return
    for (nx,ny) in (x-1,y+1),(x,y+1),(x+1,y+1):
        if 0<=nx<R and 0<=ny<C and board[nx][ny]=='.':
            route.append((nx,ny))
            findRoute(startX,nx,ny,route[:])
            route.remove((nx,ny))

def findCombi(i,points,answer):
    if i==C-1:
        return answer
    for nxt_route in routes_list[i+1]:
        for nxt_point in nxt_route:
            if nxt_point in points:
                return 0
        else:
            points.update(nxt_point)
            answer += 1
        
        findCombi(i+1,points,answer)

for i in range(R):
    findRoute(i,i,0,[(i,0)])
print(routes_list)

answer = 0
for start in range(R):
    for route in routes_list[start]: # route = ((0, 0), (1, 1), (2, 2), (2, 3), (1, 4))
        answer = max(answer,findCombi(0,set(route),answer))
print(answer)
        
'''
for i in range(C):
    print(routes[i])
    print("\n")
'''
'''
for i in range(R):
    for j in range(C):
'''   
