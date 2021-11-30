import sys
input = sys.stdin.readline

expr = input().rstrip()
l = expr.split('-')
for i in range(len(l)):
    l[i] = sum(map(int,l[i].split('+'))) # eval은 숫자 0으로 시작하면 인식하지못함 
print(l[0]-sum(item for item in l[1:]))
'''
# 5자리보다 많이 연속되는 숫자는 없다. 아 뭐야.... 또 문제 잘못봤어 내가 5자리 숫자 이하로 파싱할 필요가 없는거임... 그래도 쓴 코드 아까우니까 지우지 말아야지
# 수는 0으로 시작할 수 있다.
# 10분 syntaxerror
# 14분 파싱 까다로움
import sys
input = sys.stdin.readline

expr = input().rstrip()
#l = list(map(eval,expr.split('-')))
#print(l)
l = expr.split('-')
for i in range(len(l)):
    l[i] = l[i].split('+')
    for j in range(len(l[i])):
        if len(l[i][j])>5:
            l[i][j] = [l[i][j][:1],l[i][j][1:]] if int(l[i][j][1:])>int(l[i][j][:len(l[i][j])-1]) else [l[i][j][:len(l[i][j])-1],l[i][j][len(l[i][j])-1]] #파싱 10글자보다 더 많아지면?
print(l)

for i in range(len(l)):
    for j in range(len(l[i])):
        l[i] = eval(item for item in l[i])
'''



#print(l[0]-sum(item for item in l[1:]))


#print(int("010")) #10