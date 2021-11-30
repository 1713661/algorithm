def caculateSum(x):
    sum = 0
    num = 1
    # 이 문제는 while t: t--보다 그냥 for _ in range(t)쓰는 게 가독성 더 좋은듯
    for _ in range(x):
        count = num
        for _ in range(count):
            if x==0: break  
            sum += num
            x -= 1
        num += 1
    return sum

A,B = map(int, input().split())
print(caculateSum(B)-caculateSum(A-1))

