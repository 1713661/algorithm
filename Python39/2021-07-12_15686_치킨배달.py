import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split()) #NXN 도시 #M=치킨집개수의최대값


####입력받는거 다시 연습하기!!!!!!!
'''
#왜 이렇게 쓰면 안되지?
city=[[]*N]
for k in range(N):
    city[k].append(list(map(int,input().split())))
print(city)
'''
city=[]
for _ in range(N):
    city.append(list(map(int,input().split())))
print(city)

houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if city[i][j]==1:
            houses.append((i,j))
        elif city[i][j]==2:
            chickens.append((i,j))
#print("houses=",houses)
#print("chickens=",chickens)

'''
for house in houses:
    for chicken in chickens:
        selected_chickens = 
        '''

min_dist=int(10e9)
selected_chickens_combinations=list(combinations(chickens,M)) ##########################
for selected_chickens in selected_chickens_combinations:
    print("selected_chickens=",selected_chickens)
    city_dist=0
    for house in houses:
        dist_cand = []
        for chicken in selected_chickens:
            dist_cand.append(abs(house[0]-chicken[0])+abs(house[1]-chicken[1]))
        dist_cand.sort()
        chicken_dist = dist_cand[0]
        print("chicken_dist=",chicken_dist)
        city_dist += chicken_dist
        print("city_dist=",city_dist)
    if city_dist<min_dist:
        min_dist=city_dist
        
print(min_dist)
        

# 각 집의 최소 치킨거리를 만드는 치킨집 배열 저장하고
