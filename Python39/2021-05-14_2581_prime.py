M = int(input())
N = int(input())
sum = 0
min = 10001
for i in range(M,N):
    prime = True
    if i==1: continue
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            prime = False
            break
    if prime == True:
        if i < min: min=i
        #print(i)
        sum += i

if sum==0 and M<=N:
    print("-1")
elif M<=N:
    print(sum)
    print(min)
        
