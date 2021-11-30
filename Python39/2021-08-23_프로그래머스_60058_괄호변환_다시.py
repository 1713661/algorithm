#################### 문제 완전히 이해해서 구조 어떻게 되는지 파악한다음 짜야함!!(특히 재귀함수니까 더)

########### None이 아닌듯 이거 문법확인하기
###### 그리고 if문안에다 stack.pop() 쓰면 안되는듯
# 40분 통과

'''
def getBalanceIdx(w): #최초의 균형잡힌괄호의인덱스를반환
    cnt = 1
    for i in range(1,len(w)):
        if w[i]==w[0]:
            cnt += 1
        else:
            cnt -= 1
        if cnt==0:
            return i
'''
def getBalanceIdx(string): # '개수'만 같은 경우
    num1,num2 = 1,0 # num1=string[0]와같은괄호의개수 num2=반대괄호의개수 
    for i in range(1,len(string)): #for item in p:
        if string[i]==string[0]: 
            num1 += 1
        else:
            num2 += 1

        if num1==num2:
            return i

# 근데 인덱스로 안구하고 이렇게 u를 리턴하는 경우에는 v 구하기가 좀... 그냥 인덱스 구하는게나을듯?
def getBalance(string): # '개수'만 같은 경우. 처음 주어진 p가 균형잡힌 괄호라고 했으므로 
    stack = ['-1']
    u = ''
    for i in range(len(string)): #for item in p:
        if string[i]==string[0]:
            stack.append(string[0])
            u += string[i]
        else:
            stack.pop()
            u += string[i]
            if len(stack)==1:
                return u

def isRight(u):
    stack = [-1]
    for i in range(len(u)):
        if u[i]=="(":
            stack.append("(")
        else:
            stack.pop()
        if len(stack)==0: #-1까지 뽑혔다는 거니까
            return False
    return True


def solution(p):
    #step1
    if p=="": return ""
    
    #step2
    idx = getBalanceIdx(p) #idx는 u의 가장 끝 인덱스
    u = p[:idx+1]
    v = p[idx+1:]
    #u = getBalance(p)
    #v = p-u unsupported operand type(s) for -: 'str' and 'str'
    print("u=",u,"v=",v)

    #step3
    if isRight(u):  # 문자열 u가 "올바른 괄호 문자열" 이라면
        return u+solution(v) # 문자열 v에 대해 1단계부터 다시 수행합니다. 
    
    #step4
    else:           # 문자열 u가 "올바른 괄호 문자열"이 아니라면
        str = "("
        str += solution(v)
        str += ")"
        u = u[1:len(u)-1].replace("(",".").replace(")","(").replace(".",")") 
        #len(u)가 아니라 len(u)-1이야!!!! 이런거 실수하면 안돼!
        str += u 
        return str

print(solution("(()())()")) #"(()())()"
#print(solution(")("))       #"()"
#print(solution("()))((()")) #"()(())()"
