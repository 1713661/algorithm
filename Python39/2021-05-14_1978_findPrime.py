l = []
num = 0

t = int(input())
l = list(map(int, input().split()))

for i in range(t):
    if l[i] == 1: continue
    prime = True
    for j in range(2,int(l[i]**0.5)+1):
        if l[i]%j == 0:
            print(l[i],"%",j,"==",0)
            prime = False
            break
    if prime == True:
        num += 1
    print(l[i],"is",prime)
print(num)
