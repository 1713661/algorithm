# 전화번호 목록이 일관성을 유지하려면, 한 번호가 다른 번호의 '접두어'인 경우가 없어야 한다.
# 문제 조건을 잘 읽자.......... '접두어'만 아니면 됨
# 트라이 아직 공부 안했는데... 기출에는 나왔던 것 같다. 일단 내가 풀어보고 꼭 공부하자!!


import sys
input = sys.stdin.readline

def solution(arr):
    length = len(arr)
    for i in range(length-1):
        # 정렬되어있으므로 바로 다음전화번호만 확인해도 됨
        # if arr[i] in arr[i+1]: 는 접두어가 아니어도 arr[i] 포함만 하면 NO이기 때문에 안됨
        if arr[i] == arr[i+1][0:len(arr[i])]: 
            return "NO"
    return "YES"

t = int(input())
answers = []
for _ in range(t):
    telArr = []
    n = int(input())
    for _ in range(n):
        telArr.append(input().rstrip().replace(" ",""))
    telArr.sort()
    #telArr = sorted(telArr,key=)
    #print(telArr)
    print(solution(telArr))
   
    



    

    
            
