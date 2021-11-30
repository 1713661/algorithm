from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for k in course:
        candidates=[] # k개마다 생성해야함(생각을 해 생각을)
        for order in orders:
            for cand in combinations(order,k):
                cand = "".join(sorted(cand))
                candidates.append(cand)
        sorted_candidates = Counter(candidates).most_common()  # If n is None, then list all element counts. 
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    
    return sorted(answer)

print("answer=",solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print("answer=",solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print("answer=",solution(["XYZ", "XWY", "WXA"],[2,3,4]))