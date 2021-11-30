# 18분
from collections import deque
def solution(numbers, target):
    cnt = 0
    length = len(numbers)
    queue = deque()
    queue.append((numbers[0],0,str(numbers[0])))
    queue.append((-numbers[0],0,"-"+str(numbers[0])))
    while queue:
        num,idx,eval = queue.popleft()
        #print("num=",num,"idx=",idx)
        if idx==length-1:
            if num==target:
                cnt += 1
                print(eval)
            continue
        for nxt in (numbers[idx+1],-numbers[idx+1]):
            # num += nxt 쓰면 안돼!!!!!! for문이 -numbers[idx]돌 때 num이 틀린값 들어가니까    
            queue.append((num+nxt,idx+1,eval+str(nxt)))
        #print("queue=",queue)
    return cnt

#print("case1=",solution([1,1,1,1,1], 3)) #답=5
print("case2=",solution([2,3,5,7,9], 2)) #답=3
#print("case3=",solution([1], 1)) #답=1
#print("case4=",solution([6,2,3,6,7,1], 7)) #답=5


'''
그냥 Brute Force로 풀면 되는 문제 아닌지요 굳이 DFS일 필요가...?

def solution(numbers, target):
    answer = 0
    current_list = [numbers[0], -numbers[0]]

    for i in range(1, len(numbers)):
        next_number = numbers[i]
        next_list = []
        for num in current_list:
            next_list.append(num + next_number)
            next_list.append(num - next_number)

        current_list = next_list

    for num in current_list:
        if num == target:
            answer += 1
    return answer
'''


