# 100만자리까지 가능하니까 combinations는 시간초과날듯
# 8분 원래 생각한 방법은 remove(i)가 O(n)이어서 시간초과날듯
# 26분 답지보고 힌트얻어서 풀었는데 안풀림.. (알고리즘을 제멋대로 이해했기 때문)

# 프로그래머스에 더 간단한 풀이있음(if else문 겹치니까 없앤거임. 내코드가 알고리즘 이해하기에는 더 쉬움)
# https://programmers.co.kr/learn/courses/30/lessons/42883/solution_groups?language=python3

def solution(number, k):

    stack = [number[0]]
    idx = len(number)
    for i in range(1,idx):
        if k==0:
            idx = i
            break
        if int(number[i])<int(stack[-1]):
            stack.append(number[i])
        else:
            while k>0 and len(stack)>0 and int(stack[-1])<int(number[i]):
                stack.pop()
                k -= 1
            stack.append(number[i])
    
    if idx==len(number):
        if k==0: 
            return "".join(stack)
        else: ##k==0이 도달하지 못했다는거니까 stack마지막빼줘야함
            return "".join(stack[:idx-k])
    else:
        return "".join(stack)+number[idx:]
    
'''
(['9', '4'], 4)
(['3', '2'], 5)
(['7', '7', '5', '8'], 8)
(['1', '0', '0', '0'], 4)
'''

print(solution("1924",2))  #len=4
# "94"
print(solution("1231234",3)) #len=7
# "3234"
print(solution("4177252841",4)) #len=10
# "775841"
print(solution("1000",1)) #len=4
# "100"

