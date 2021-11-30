import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())

##모든 city값을 저장할 필요가 없었음!!!!!
city=[]
for _ in range(N):
    city.append(list(map(int,input().split())))

houses_tuple=[]
chickens_tuple=[]
for i in range(N):
    for j in range(N):
        if city[i][j]==1:
            houses_tuple.append((i,j))
        elif city[i][j]==2:
            chickens_tuple.append((i,j))

chickens_combinations = combinations(chickens_tuple,M)

# 각 변수 초기화 시점 주의(3차원이라서 헷갈릴 수 있음)
min_dist=int(10e9)
for chickens in chickens_combinations: # M개의 치킨 골라서
    city_dist=0                        # 도시의 치킨거리는 치킨조합마다 초기화해야함
    for house in houses_tuple: # 각 집당 거리 구하기
        chicken_dist_cand=[]   # 각 집당 치킨거리는 M개의 치킨거리 중 최소거리
        for chicken in chickens: 
            chicken_dist_cand.append(abs(house[0]-chicken[0])+abs(house[1]-chicken[1]))
        chicken_dist_cand.sort()
        chicken_dist=chicken_dist_cand[0]
        city_dist += chicken_dist
    if city_dist<min_dist:
        min_dist = city_dist
print(min_dist)