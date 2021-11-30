# 자카드 유사도 = 두 집합의 교집합 크기/ 두 집합의 합집합 크기
# 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1

# 자카드 유사도는 원소의 중복을 허용하는 다중집합에 대해서 확장할 수 있다

# 27분 한번에 통과 자신감 갖자!!!!!!!!!!!!!!!!!!!!!!!!!!

import re

def solution(str1, str2):
    l1,l2 = len(str1),len(str2)
    ##########  영문자로 된 글자 쌍만 유효하고
    A_li = [str1[i:i+2].lower() for i in range(l1-1) if re.fullmatch('[a-z]{2,2}',str1[i:i+2].lower())] # ['fr', 'ra', 'an', 'nc', 'ce']# 대소문자 차이 무시
    B_li = [str2[i:i+2].lower() for i in range(l2-1) if re.fullmatch('[a-z]{2,2}',str2[i:i+2].lower())] # ['fr', 're', 'en', 'nc', 'ch']
    
    print(A_li)
    print(B_li)

    A_set = set(A_li) # {'an', 'ra', 'nc', 'ce', 'fr'}      
    B_set = set(B_li) # {'en', 'ch', 'nc', 're', 'fr'}

    print(A_set)
    print(B_set)

    inter = A_set&B_set
    union = A_set|B_set

    print(inter)
    print(union)

    top,btm = 0,0
    for i in inter:
        top += min(A_li.count(i),B_li.count(i))
    for u in union:
        btm += max(A_li.count(u),B_li.count(u))
    
    return int(top/btm*65536)

print(solution("FRANCE", "french"))
# 16384
'''
print(solution(handshake,	shake hands))
#
print(solution())
#
print(solution())
#
'''