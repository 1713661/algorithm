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

    answer_list = sorted([set(item) for item in answer_list])
    answer_list.sort()
    print(answer_list)

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
        answer *= int(factorial(len(new_answer_list[i]))/factorial(choose[i]))
    
    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])) # 3