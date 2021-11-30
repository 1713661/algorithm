# 23분 indexerror나지 않도록 구상하는 거 오래걸렸음.. 
# 그럴때는 쓰면서 경우의 수 확인하자 (머리로만 확인하려고 하면 안됨)
import sys
input = sys.stdin.readline

N = int(input())
positive = []
negative = []
ones = [] 
for _ in range(N):
    num = int(input())
    if num>1:
        positive.append(num)
    # case5. 1이 존재할때 1은 다른수와 곱하지 않고 바로 더하는지 
    # (이유 : 1보다 큰 수 x와 1이 주어진다면 두수를 곱하는것보다 따로 더해주는게 더 크다)
    elif num==1:
        ones.append(num)
    else:
        negative.append(num)

positive.sort(reverse=True)
negative.sort()
p = len(positive)
n = len(negative)
answer = 0

if n%2==0:
    for i in range(0,n,2):
        answer += (negative[i]*negative[i+1])
else:
    for i in range(0,n-1,2):
        answer += (negative[i]*negative[i+1])
    answer += negative[n-1]

if p%2==0:
    for i in range(0,p,2):
        answer += (positive[i]*positive[i+1])
else:
    for i in range(0,p-1,2):
        answer += (positive[i]*positive[i+1])
    answer += positive[p-1]

answer += len(ones)

print(answer)




