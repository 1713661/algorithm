# len(ops)차원 리스트로 만들어야 계산하기 편함

from itertools import permutations

def solution(expression):
    ops = []
    
    # 연산자 종류가 꼭 3개가 아닐 수 있음(문제를 제대로 보자)
    checkPlus = expression.split("+")
    if len(checkPlus)>1:
        ops.append("+")
    checkMinus = expression.split("-")
    if len(checkMinus)>1:
        ops.append("-")
    checkTimes = expression.split("*")
    if len(checkTimes)>1:
        ops.append("*")

    # 연산자 종류가 하나면 바로 계산하고 "절댓값"을 리턴    
    if len(ops)==1: 
        return abs(eval(expression))

    cand = [] 
    for operators in permutations(ops,len(ops)):
        expr = expression.split(operators[0]) # expr= ['100-200', '300-500+20']
        
        for i in range(len(expr)):
            expr[i] = expr[i].split(operators[1])
            
            for j in range(len(expr[i])):
                expr[i][j] = eval(expr[i][j])

            res = expr[i][0]
            for j in range(1,len(expr[i])):
                if operators[1]=="*":
                    res *= expr[i][j]
                elif operators[1]=="+":
                    res += expr[i][j]
                else:
                    res -= expr[i][j]
            expr[i] = res 
            # (28번째 줄)expr[i].split(operators[1])을 가리키던 expr[i]가 res를 가리키도록 바꿈
            # expr[i]에 배열 할당해줬던 게 아니기 때문에 배열크기 신경쓸필요없음
            

        res2 = expr[0]
        for i in range(1,len(expr)):
            if operators[0]=="*":
                res2 *= expr[i]
            elif operators[0]=="+":
                res2 += expr[i]
            else:
                res2 -= expr[i]

        cand.append(abs(res2))
        
    return max(cand)

print(solution("4-5"))