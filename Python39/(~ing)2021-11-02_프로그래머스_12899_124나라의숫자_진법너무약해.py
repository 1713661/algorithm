def solution(n):
    n = n-1
    li = []
    if n==0: li.append(0)
    while n>0:
        li.append(n%3)
        n //= 3
        
    print("li reverse=",li[::-1])  
    answer = '';                              
    l = len(li)
    for item in li[::-1]:
        if item==0:
            answer += '1'
        elif item==1:
            answer += '2'
        elif item==2:
            answer += '4'
       
    return answer