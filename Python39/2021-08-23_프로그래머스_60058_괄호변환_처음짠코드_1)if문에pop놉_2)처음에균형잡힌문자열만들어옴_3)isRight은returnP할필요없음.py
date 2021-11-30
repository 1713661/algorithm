# 11분 문제이해(완전히 못함) 그래도 일단 풀어볼까?
# 20분 컴프리헨션에서 막힘... 파이썬 기본 문법 공부!!!!! (컴프리헨션 쓸 필요 없었음..)
# 28분 구현력 너무 떨어져.. dfs로 푸는건가? 재귀긴한데 dfs는 놉
# 69분 일단 짜라는대로 짜긴 했는데 if(stack.pop()==-1): IndexError: pop from empty list 나옴
# 전체적인 코드 구조를 어떻게 짜야할지 모르겠음.. + # step2 u끄집어내는방법 깔끔하게 못짜겠음....
# 104분 완전 꼬였음..(머리안돌아감)이래서 코테 어떻게보지

########### "균형잡힌 괄호 문자열" p가 매개변수로 주어질 때,
# 문제를 잘 읽으시오...(근데 문제가 너무 길어서 조건 찾기 쉽지않아..)
# 이코테 코드 보니까 나도 거의 다 잘짰음!! 자신감갖자!!!

def getBalanceIdx(string): # '개수'만 같은 경우
    num1,num2 = 1,0 # num1=string[0]와같은괄호의개수 num2=반대괄호의개수 0,0이라고 썼으면 안됐음!!!!!!
    # 이런 디테일한 거에서 구현력 좌우되는거임!!!
    for i in range(1,len(string)): #for item in p:
        if string[i]==string[0]: 
            num1 += 1
        else:
            num2 += 1

        if num1==num2:
            return i


# 구현하기 전에 생각생각!!!!
# 인덱스로 안구하고 이렇게 u를 리턴하는 경우에는 v 구하기가 좀... 그냥 인덱스 구하는게나을듯?
'''
def getBalance(string): # '개수'만 같은 경우
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
'''

def isRight(p): # 올바른괄호문자열
    stack = ['-1']
    print("hi=",p)
    for i in range(len(p)):#for item in p:
        if p[i]=='(':
            stack.append('(')
        else:
            stack.pop()#if(stack.pop()==-1): ######그리고 if문안에다 stack.pop() 쓰면 안되는듯 pop()함수 원소 리턴하기는 하는데..
        if len(stack)==0: #-1까지 뽑혔다는 거니까
            return
    return p 

def step(w):
    print("hi step")
    # step1
    if w=="": return ""

    # step2 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    idx = getBalanceIdx(w)
    '''
    if idx == -1: #처음에 균형잡힌 괄호 문자열로 준다고 했으므로 이거 고려안해도됨
        print("what should I do?")
        return w ####################################
    else:
    '''
    u = w[:idx+1]   # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며
    v = w[idx+1:] # v는 빈 문자열이 될 수 있습니다. 
    print("step2 u=",u,"v=",v)

    # step3
    if isRight(u): #3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
        # step3-1
        newstr = u+step(v)
        print("step3 u+step(v)=",newstr)
        return newstr

    # step4
    else:
        str = '(' #4-1.
        str += step(v) #4-2.#########idx는 같은 idx인가? (문제 자체를 이해를 못했음)
        str += ')' #4-3.
        u = u[1:len(u)-1].replace('(','.').replace(')','(').replace('.',')') #악!!!!!!!!마지막에 )라고 써야하는데 (라고 썼음!!!! 혹시 이것땜에 틀렸었을까?
        #.은 temp # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서  
        print("after 4-4 u=",u)
        str += u #뒤에 붙입니다.
        print("str=",str)
        return str # 4-5. 생성된 문자열을 반환합니다.


def solution(p):
    if isRight(p)==None: #반환값이 없으면
        print("start step"
        
        )
        answer=step(p) #######바로 return step(p) 하면 안됨!!!!!!!!!
        return answer
    else: #처음 주어진 문자열이 올바른 괄호 문자열이면
        return p


print('1',solution("(()())()")) #"(()())()"
print('2',solution(")("))       #"()"
print('3',solution("()))((()")) #"()(())()"
