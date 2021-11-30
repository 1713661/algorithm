# 논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능하다.

import sys
input = sys.stdin.readline

houses=list()
for _ in range(int(input())):
    houses = list(map(int,input().split()))
    # houses=list() houses = input().split() 이런식으로 쓰면 안됨!!!!!!!!!!!!!!!! 파이썬 기본 문법부터 공부하자
print(houses)

'''
sum = 0
min = int(1e12) #너무 큰 숫자인가..
print("HI")
for house in houses:
    for i in range(len(houses)):
        sum += abs(house-houses[i])
    if sum<min:
        min=sum
print(min)
'''
