import sys
input = sys.stdin.readline
L = []
idx = -1

for _ in range(int(input())):
    N = int(input())
    if N:
        L.append(N)
        idx += 1
    else:
        del L[idx] # pop 너무 오래 걸려....
        idx -= 1
        
# lambda로는 표현 못하는듯 그냥 sum 쓰면 돼!!!!!!!
print(sum(L))

        
