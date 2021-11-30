# 입력으로 괄호가 올바르게 처진(괄호가 서로 쌍이 맞는) 수식이 들어옴
##### 괄호를 제거할 때는, 항상 쌍이 되는 괄호끼리 제거해야 한다.
# 14분 흠..... 잠깐자기
# 30분 재귀함수 못짜겠어.....
# 43분 내가짠코드는 for문도 돌려야함..(재귀함수 실력 언제느냐ㅜㅜ)
# 수식길이 최대 200이니까 sys.recursionlimit안써도되겠지?
# https://huiung.tistory.com/37 (C++ 재귀함수로 푼거)
# (재귀로 푼 경우에도 괄호짝다저장하고 재귀함수돌려야함)

##### 재귀함수없이 combinations로 다시 짬
# 33분 틀렸습니다... 괄호 여러겹인 경우 중복이기 때문!!
from itertools import combinations

stack = [] # 괄호넣을스택 
index = [] # 쌍이 되는 괄호의 인덱스 튜플로 저장 

formula = list(input().rstrip()) 

l = len(formula)
for i in range(l):
    if formula[i]=='(':
        stack.append(i)
    if formula[i]==')':
        index.append((stack.pop(),i)) #######

length = len(index)
answer = set() # 사전순으로 출력해야하므로
for num in range(1,length+1): # 괄호 한쌍이상제거해야하니까
    for combi in combinations(index,num):
        li = [] ###더 효율적인 방법없을까?
        for c in combi:
            li.append(c[0])
            li.append(c[1])
        li.sort(reverse=True)
        
        #print("num=",num,"combi=",li)
        f = formula[:]
        for i in li:
            f.pop(i)
        answer.add("".join(f))

answer = sorted(answer) #(((1)))(2) 처럼 괄호 여러개인 경우 ((1))(2) 중복으로 들어감
for ans in answer:
    print(ans)

'''
#################### 처음에짰던코드인데..
def solution(formula):
    answer = []

    def recur(f,idx,stack):
        #print("f=",f,"idx=",idx,"stack=",stack)
        if idx==len(f):
            answer.append("".join(f))
            return
        
        if f[idx]=='(':
            recur(f[:idx]+f[idx+1:],idx,stack[:])
            stack.append('(')
            recur(f[:],idx+1,stack[:]) 
        elif f[idx]==')':
            if len(stack)>0:
                stack.pop()
                recur(f[:],idx+1,stack[:]) 
            else:
                recur(f[:idx]+f[idx+1:],idx,stack[:])
        else:
            recur(f[:],idx+1,stack[:])


    recur(formula,0,[])

    return answer

print(solution(formula)) # ['2+2*2+2', '2+(2*2)+2', '(2+2*2)+2', '(2+(2*2)+2)'] 이렇게나옴.. 포기
'''



   

        
