# 10분

d = [0]*11
d[1]=1      # 1
d[2]=2      # 1+1 2
d[3]=4      # 1+1+1 1+2 3
for i in range(4,11):
    d[i]=d[i-1]+d[i-2]+d[i-3]
#print(d)

for _ in range(int(input())):
    n = int(input())
    print(d[n])