# 15분(시간초과)+9분(라이브러리 어떤거 써야할지 모르겠음)+11분(1,2,3,...이런식으로지우면안됨)+8분(적절한알고리즘같다가도아님. 구글링해야겠음!)
# 악! 문제 잘못이해했음(5분동안 생각해봤는데 딱히 좋은 풀이 안떠오름..)
# 스택으로 푼다는데? 오마이갓.. 내가 제일 싫어하는 재귀...

'''
def solution(number, k):
    digit = len(number)-k # 자리수
    #delete = list(set(sorted(list(number))[:k]))
    # 이 방법은 remove(i)가 O(n)이어서 시간초과날듯
    digitList = list(map(int,number))
    print(digitList)
    cnt = 0
    for i in range(10):
        x = digitList.count(i)
        if cnt+x>k:
            idx = i
            break
        cnt += x
    print("idx=",idx,"cnt=",cnt,"k=",k)

    return str(digitList)
'''


# 코드 자체를 하나하나 따지지 말고 step2 잘 읽기!!
'''
아래 코드는 다른 사람의 아이디어를 참고 후 코드로 구현한 내용이다.

step1) 스택(stack)의 자료구조를 이용하였으며 number의 첫 번째 값을 스택에 넣은 상태에서 시작!
ex) number = '32123' | stack = ['3'] | k = 2

step2) number의 두 번째 값부터는 스택의 마지막 값과 비교

if 스택의 마지막 값 >= number[i]의 값이면 스택에 추가한다.(append)
ex) stack[-1] = 3 > number[1] = 2
stack = ['3', '2']
else
스택에 원소가 존재하며 k > 0이고 스택의 마지막 값이 number[i] 보다 작을 경우 스택의 마지막 원소를 뺀다.(pop)
뺀 원소만큼 k를 1씩 빼준다.
ex) stack = ['3', '2', '1'] | number[3] = 2
stack[-1] = 1 < number[3] = 2
stack = ['3', '2'] | k = 1
반복문을 마쳤을 때 스택에 남아있는 값을 순서대로 하나의 문자열로 묶어주면 그 값이 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자다.
number = '32123' | k = 2의 경우 정답은 323
'''

def solution(number, k):
    answer = ''
    stack = [number[0]]
    while k:
        for i in range(1, len(number)):
            if int(stack[-1]) >= int(number[i]):
                stack.append(number[i])
            else:
                while len(stack) and k and int(stack[-1]) < int(number[i]):
                    stack.pop(-1)
                    k -= 1
                stack.append(number[i])
        else:
            return ''.join(stack[:len(number)-k])
    return ''.join(stack)

print(solution("1924",2))
# "94"
print(solution("1231234",3))
# "3234"
print(solution("4177252841",4))
# "775841"


'''
from itertools import combinations

def solution(number, k):
    digit = len(number)-k # 자리수
    combination = list(combinations(list(number),digit))
    #print(combination) #[('1', '9'), ('1', '2'), ('1', '4'), ('9', '2'), ('9', '4'), ('2', '4')]

    l = []
    for tupl in combination: #tupl=('1', '9')
        number = ''
        for i in range(len(tupl)):
            number += tupl[i]
        l.append(number)
        #l.append(int(number))
    l.sort(reverse=True)
    return l[0]
'''