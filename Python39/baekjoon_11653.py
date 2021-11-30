'''
numbers = [72, 3, 6, 2, 9991, 17]

for number in numbers:
    print("number:",number)
    n = int(number ** 0.5)
    for i in range(2,n+1):
        if number==1: break
        while number%i == 0:
            print(i)
            number //= i
    if number != 1:
        print(number)
'''

N = int(input())
for i in range(2, int(N**0.5)+1):
    if N==1: break
    while N%i==0:
       print(i)
       N //= i
if N != 1: print(N)
   
