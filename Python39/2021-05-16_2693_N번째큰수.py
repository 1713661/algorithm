import sys
input = sys.stdin.readline

#T = int(input())

for _ in range(int(input())): #int(input()) 쓰나 T 쓰나 시간 차이 없음!!
    A = list(map(int,input().split(' ')))
    A.sort()
    print(A[-3])
