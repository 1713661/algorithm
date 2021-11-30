# 5분 VPS 정확한 정의 잘 모르겠음..
# +12분 이런것도 못풀다니.. 짜증나
# 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 
# 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다.
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    stack = ['empty']
    for i in range(len(s)):
        if s[i]=='(':
            stack.append("(")
        elif s[i]==')':
            prev = stack.pop()
            if prev=='empty':
                break
    if len(stack)==1:
        print("YES")
    else:
        print("NO")
       
        


