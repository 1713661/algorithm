import sys
input = sys.stdin.readline
# 32분
#에라토스테네스의 체
N = int(input())
isPrime = [True]*(N+1) #1 ≤ N ≤ 4,000,000
for num in range(2,int(N**0.5)+1):
    if isPrime[num]:
        k = 2
        while num*k<=N:
            isPrime[num*k]=False
            k += 1
    '''
    if isPrime[num]:
        isPrime[2*num::num] = [False]*(N//num-1) 
    # https://docs.python.org/ko/3/library/stdtypes.html#sequence-types-list-tuple-range
    # s[i:j:k] = t <- s[i:j:k]의 항목들이 이터러블 t의 항목들로 대체된다고 했으므로 뒤에 (N//num-1)붙여야 하는듯
    '''
li = [num for num in range(2,N+1) if isPrime[num]]
L = len(li)
end,sum,ans = 0,0,0
for start in range(L):
    while end<L and sum<N:
        sum += li[end]
        end += 1
    #if end==L: break ###이거 쓰면 안됨 
    if sum==N: ans += 1
    sum -= li[start]
'''
# 이거 indexError 나옴 li=[]인 경우(N=1일수도 있음!!!!!) 땜에 그런듯! (li[0] 런타임에러)
end,sum,ans = 0,li[0],0
for start in range(L):
    while end<L and sum<N:
        end += 1
        if end!=L: sum += li[end]
    if end==L: break
    if sum==N: ans += 1
    sum -= li[start]
'''
print(ans)


