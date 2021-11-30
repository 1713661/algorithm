'''
for _ in range(int(input())):
    N, M = input().split()
    digitN = len(N) # 자리수
    digitM = len(M)
    n = int(N)      # 숫자
    m = int(M)
    
    ans = n % (10 ** (digitN-1))
    print(ans)
'''


'''
# 이 방법으로 풀면 5000ms 걸림
for _ in range(int(input())):
    N, M = map(int,input().split())
    cnt = 0
    for i in range(N,M+1):
        string = str(i)
        for s in string:
            if s == '0': cnt += 1
    print(cnt)
'''
#count함수써도 됨

def a(n):
    if n==1: return 1
    return a(n-1)+9*n*10**n-2

def f(x): # x=4567
    digit = len(str(x))
    if digit == 1: return 0
    l = []
    for i in range(1,digit-1,-1):
        print('i=',i)
        b = i*9**(i-1)
        print('b=',b)
        l.append(b)
    k=sum(l)
    print('k=',k)
    return (x//digit)*a(digit-1)+k+f(x%10**(digit-1)) ##이거 내가 적었던 코드인듯 33 1005 입력했더니 7228031라는 엄청난 숫자나옴..ㅋㅋㅋㅋ

for _ in range(int(input())):
    N, M = map(int,input().split())
    print(f(M)-f(N-1))
