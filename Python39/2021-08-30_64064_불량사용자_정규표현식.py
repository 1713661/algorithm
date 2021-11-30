# 23분

from itertools import permutations
import re

def check(user_list,banned_list):
    for i in range(len(banned_list)):
        #if len(user_list[i])!=len(banned_list[i]): return False
        if not re.fullmatch(banned_list[i].replace('*','.'),user_list[i]): 
            #길이가 다르면 오류나나?? 아냐 위에 주석처리해도 괜찮음
            return False
    return True

def solution(user_id_list, banned_id_list):
    answer = []
    for user_list in permutations(user_id_list,len(banned_id_list)): 
        # 순열 banned_id_list길이 만큼만 만들어야함
        # user_id_list만큼 만들면 밑에 애 tuple로 만들어도 앞에 banned_id_list만큼만 겹치면 무조건 다 들어가니까....(생각을 해 생각을)
        if check(user_list,banned_id_list) and set(user_list) not in answer:
            answer.append(set(user_list))
    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])) # 3

