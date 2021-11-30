# 26분 banned_id_list가 중복되는 경우를 고려하지 못해서 좀 시간걸림
# 33분 경우의 수 곱하지 말고 answer_list[i]마다 팝하고 경우 더하는 게 좋을듯
# +29분 자료형으로 경우 나눠서 곱해줬음
# +1시간 5분 nCr 구현 54.5%... 내가 알고리즘 잘못 생각한듯.. 슬프다

from math import factorial

def solution(user_id_list, banned_id_list):
    answer_list = [[] for _ in range(len(banned_id_list))]
    for user_id in user_id_list:
        isBanned = True
        for i in range(len(banned_id_list)):
            if len(user_id)!= len(banned_id_list[i]): continue
            for j in range(len(user_id)):
                if banned_id_list[i][j]=="*": continue
                elif user_id[j]!=banned_id_list[i][j]:
                    isBanned = False
            if isBanned:
                answer_list[i].append(user_id)
            isBanned = True #초기화

    print(answer_list)
    answer_list = sorted([sorted(item) for item in answer_list])
    print("aftersort=",answer_list)
    '''
    aftersort= [['abc123', 'fridic', 'frodoc', 'frodok'], ['crodo', 'frodo', 'krodo'], ['fradi'], ['fradi', 'frodo'], ['fridic', 'frodoc']]
    # 이렇듯 정렬했는데도 뒤에 겹치는 원소가 나올 수 있음!!!!!!!!!!!!! 왜 실전에서는 이 케이스를 생각하지 못할까? 너가 너무 어렵게 생각하는거야...
    # 각 banned_id 당 후보리스트 만들면 나중에 경우의 수 생각하기 어렵다는 걸 빨리 알았어야함!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    ########## (고등학교 때 이런식으로 경우의 수 계산하는 것도 굉장히 어려운 문제였음..)
    ########## dfs 백트래킹으로 풀면 됐었음... https://esoongan.tistory.com/120
    # 사실 금방 알기는 했는데 다른 풀이 방법이 생각나지 않아서 그냥 밀어붙였음(이런 예외 사항 생각하지 않고..)
    # 정규표현식 풀이 https://pslog-eraser.tistory.com/25
    '''
    answer_list = [set(item) for item in answer_list]

    new_answer_list = []
    choose = []
    idx,nextidx=0,1
    while idx<(len(answer_list)):
        if len(answer_list[idx]&answer_list[nextidx])==0: 
            new_answer_list.append(list(answer_list[idx]))
            choose.append(1)
            idx += 1
            nextidx += 1 
        else: #교집합이 있으면
            left = idx
            right = idx+1
            new = answer_list[left]
            while len(new&answer_list[right])>0:
                new = (new|answer_list[right])
                right += 1
                if right==len(answer_list): break
            new_answer_list.append(new)
            choose.append(right-left)
            idx=right
            nextidx = idx+1
        
        if idx==(len(answer_list)-1):
            new_answer_list.append(answer_list[idx])
            choose.append(1)
            break

    print(new_answer_list)
    print(choose)

    answer = 1
    for i in range(len(new_answer_list)):
        a = factorial(len(new_answer_list[i]))
        b = factorial(len(new_answer_list[i])-choose[i])*factorial(choose[i])
        answer *= (int(a/b) if a!=0 and b!=0 else 1)
    
    return answer


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])) # 3