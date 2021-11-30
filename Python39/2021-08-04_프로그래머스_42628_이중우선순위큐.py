# 34분
# 15분
# heapq.nsmallest heap.nlargest이용하기!!!!!!! 역시 라이브러리 모르는 게 문제였음.. 아까 분명 확인했는데 왜 못봤을까????????????????????????????????????????
# heapq.nlargest(n, iterable, key=None)
# iterable에 의해 정의된 데이터 집합에서 n 개의 가장 큰 요소로 구성된 리스트를 반환

from heapq import heappush,heappop,nlargest
def solution(operations):
    queue = []
    for operation in operations:
        command,num = operation.split()
        num = int(num)

        if command=='I':
            heappush(queue,num)
        elif command=='D' and len(queue)!=0:
            if num==1:
                queue.remove(int(nlargest(1,queue)[0]))
            else: #num==-1
                heappop(queue)
    if len(queue)==0:
        return [0,0]
    l = []
    l.append(int(nlargest(1,queue)[0]))
    l.append(heappop(queue))
    return l

'''
from heapq import heappush,heappop
def solution(operations):
    maxQ = []
    minQ = []
    for operation in operations:
        command,num = operation.split()
        num=int(num)
        if command=='I':
            print("I")
            heappush(maxQ,-num) #최대값 우선순위 큐이기 때문에
            heappush(minQ,num)
            print("maxQ=",maxQ)
            print("minQ=",minQ)
        elif command=='D' and len(maxQ)!=0 and len(minQ)!=0:
            if num==1:
                print("최댓값 삭제")
                heappop(maxQ)
                print("maxQ=",maxQ)
                print("minQ=",minQ)
            else: #num==-1
                print("최솟값 삭제")
                heappop(minQ)
                print("maxQ=",maxQ)
                print("minQ=",minQ)
    print("terminal")
    print("maxQ=",maxQ)
    print("minQ=",minQ)
    answer = []
    if len(maxQ)==0 or len(minQ)==0:
        return [0,0]
    answer.append(-heappop(maxQ))
    answer.append(heappop(minQ))
    return answer
'''
print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))

print(solution(["D 1"]))

print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))
