import sys
input = sys.stdin.readline
# 문제잘못봐서 또 5분까먹음(한줄끝마다 '.'있음/창작게해서'.'이안보였음)
# 총 22분

while True:
    line = input().rstrip()

    if line=='.': break

    stack = ["empty"]

    for letter in line:
        if letter=='(':
            stack.append("(")
        elif letter==')':
            e = stack.pop()
            if e=='empty' or e=='[':
                print('no')
                break
        elif letter=='[':
            stack.append("[")
        elif letter==']':
            e = stack.pop()
            if e=='empty' or e=='(':
                print('no')
                break
        
        elif letter=='.':
            if len(stack)==1:
                print('yes')
            else:
                print('no')
    
