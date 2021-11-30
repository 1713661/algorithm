import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    list = input().split() #A,B
    arr.append((list[0],int(list[1])))
arr = sorted(arr,key=lambda list: list[1])

for student in arr:
    print(student[0], end=' ')
    