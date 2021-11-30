# 함수 R은 배열에 있는 숫자의 순서를 뒤집는 함수이고, D는 첫 번째 숫자를 버리는 함수
#  배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.
# 1시간 24분(디테일구현힘들어..) 50프로에서 틀림 
# print문 다 \n붙이니까 1프로도 못가고 틀렸다고 나옴..


# 3에서 isCaseEnd돼서 빠져나왔을 경우 print해야하는데.. 
# 아마 다른 번호에서 continue한 경우가 있어서 이렇게 쓴 것 같음
# 암튼 이런 식으로 분기문 많은 코드는 지양해야한다
# reverse 효율적으로 처리하려다 이렇게 꼬인 것 같은데
# 그냥 flag하면 되는거였음.. 
# 글구 deque는 popleft() pop() 둘다 O(1)이니까 막써도 상관없음(괜히 겁먹었던 것 같음)

import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())): #테스트케이스(최대100)
    functions = input().rstrip() # 1<= <=100,000
    n = int(input()) # 배열의원소개수 0<= <=100,000
    
    arr = deque(input().lstrip('[').rstrip(']\n').split(',')) #숫자문자가 원소인 배열
    #print(arr) #['1', '2', '3', '4'] #n=0 []이면 ['']
    if n==0:
        if 'D' in functions:
            print("error\n")
            break
        else:
            print('[]\n')
            break
    cmdR,cmdD = 0,0
    isCaseEnd = False
    for func in functions: #처음엔R부터들어옴
        if func=='R'and cmdD==0:
            #1. R...R
            cmdR += 1

        elif func=='R' and cmdD!=0:
            #3. (R...R)D...DR 마지막R전까지처리
            if cmdR%2==1: # 홀수면 뒤집인 배열이니까 마지막 숫자버림
                for _ in range(cmdD):
                    if len(arr)==0:
                        print("error\n")
                        isCaseEnd=True
                        break #sys.exit()
                    arr.pop()
                if isCaseEnd:
                    break # function for문 나감
            else: # 짝수면 정배열이니까 첫번째 숫자버림 D...DR은 여기에해당
                for _ in range(cmdD):
                    if len(arr)==0:
                        print("error\n")
                        isCaseEnd=True
                        break #sys.exit()
                    arr.popleft()
                if isCaseEnd: 
                    break # function for문 나감
            cmdR = 1 #초기화(마지막R처리해야하니까)
            cmdD = 0 #초기화
            #4. R <-이상태됨

        elif func=='D' and cmdR!=0:
            #2. R...RD..D
            cmdD += 1

        elif func=='D' and cmdR==0:
            #5. D...D
            cmdD += 1
    # function나오면 R...R(D...D)형태일거임

    if isCaseEnd: 
        continue
    if cmdR%2==1:   # 홀수면 뒤집인 배열이니까 마지막 숫자버림
        for _ in range(cmdD):
            if len(arr)==0:
                print("error\n")
                isCaseEnd=True
                break#sys.exit()
            arr.pop()
        if isCaseEnd: 
            continue
        arr.reverse()

    else: # 짝수면 정배열이니까 첫번째 숫자버림 D...DR은 여기에해당
        for _ in range(cmdD):
            if len(arr)==0:
                print("error\n")
                isCaseEnd=True
                break#sys.exit()
            arr.popleft()
        if isCaseEnd: 
            continue
        
    #print("["+item for item in arr)
    #print(str(list(arr)).strip()) 
    answer ='['
    for i in range(len(arr)-1):
        answer += arr[i]
        answer+=','
    answer += arr[len(arr)-1]
    answer += ']\n'
    print(answer)  
    
        
            
             

