# DFS로 탐색해서 최대값 찾기??
# 블록을 상하좌우로 이동하는 방법이 아닌, 보드를 90도 돌리고 무조건 왼쪽으로 합치는 방법
# dfs : 보드에서 최댓값을 저장하고 convert, rotate함수를 부름
# convert : list에서 같은값이 있다면 왼쪽으로 이동시켜서 합침
# rotate : 보드를 90도 회전시킴

# 다른사람코드
from copy import deepcopy

N = int(input())
Board = [list(map(int, input().split())) for _ in range(N)]

def rotate(N, B):
    new_lst = deepcopy(B)
    for i in range(N):
        for j in range(N):
            new_lst[j][N-i-1] = B[i][j]
    return new_lst

def convert(N, B):

    new_lst = [i for i in B if i!=0]    

    for i in range(1, len(new_lst)):
        if new_lst[i-1] == new_lst[i]:
            new_lst[i-1] *= 2
            new_lst[i] = 0

    new_lst = [i for i in new_lst if i!=0] # 위에서 0으로 만들었으니까 

    return new_lst + [0]*(N-len(new_lst))    #list길이만큼 오른쪽에 0추가

def dfs(N, B, count):
    result = max([max(i) for i in B])
    if count == 0:
        return result
    
    for _ in range(4):
        C = [convert(N, i) for i in B]    #list한줄씩 변환한뒤 합침
        result = max(result, dfs(N, C, count-1))
        B = rotate(N, B)
    return result

print(dfs(N, Board, 5))
