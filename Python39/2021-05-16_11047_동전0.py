import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

cnt = 0
for coin in coins[::-1]:
    i = K//coin
    if not i: continue
    cnt += i
    K %= coin
print(cnt)
    
