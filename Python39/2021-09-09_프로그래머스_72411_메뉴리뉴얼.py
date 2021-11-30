# 코스요리 형태로 재구성 (최소 2가지 이상의 단품메뉴)
# (2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만)
# 이전에 각 손님들이 주문할 때 
# '가장 많이 함께 주문한 단품메뉴들'??을 코스요리 메뉴로 구성
# 8분 문제읽기
# 25분 여러개 어떻게 갖고오는지 모르겠음..
from collections import Counter
from itertools import combinations
def solution(orders, course):
    # 오름차순으로 정렬되어 있습니다.a
    # course 배열에는 같은 값이 중복해서 들어있지 않습니다.

    courses = [[] for _ in range(len(course))]
    for order in orders: #order="ABCFG"
        order = sorted(order)
        for i in range(len(course)):#for num in course: #num= 2,3,4
            if len(order)<course[i]: break
            courses[i].extend(list("".join(combi) for combi in combinations(order,course[i])))
            '''
            for combi in combinations(order,num):
                courses.append(combi)
            '''
    answer = []
    for num in range(len(courses)):
        if len(courses[num])==0: continue
        m = sorted(Counter(courses[num])) #이건 그냥 key들만 정렬해서 리턴(딕셔너리랑 똑같음)
        most = Counter(courses[num]).most_common() #Counter객체의 value값 큰 순으로 정렬하고 리턴
        key = most[0][1]
        if key==1: continue # (2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만)
        answer += [menu for (menu,cnt) in most if cnt==key ] # 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 

    return sorted(answer) # 사전 순으로 오름차순 정렬해서 return
'''
print(solution( ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])) 
# ["AC", "ACDE", "BCFG", "CDE"]

print(solution( ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])) 
# ["ACD", "AD", "ADE", "CD", "XYZ"]
'''

print(solution( ["XYZ", "XWY", "WXA"], [2,3,4])) 
# ["WX", "XY"]

