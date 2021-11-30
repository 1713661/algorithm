# 최소 한 개의 모음(a, e, i, o, u)과 
# 최소 두 개의 자음으로 구성되어 있다고 알려져 있다.

# 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 
# 34분 생각보다 시간오래걸림 (m,n 생각해서 코드짜는 게 오래걸림) range(L+1) +1 해야함
# 7분 (분기문 너무 많아..)
# 다른사람코드보니까 그냥 전체 input combinations 돌려서 v>=1 and c>=2일때만 출력해줬음
from itertools import combinations
import re

L,C = map(int,input().split())
cand = input().split()

if C==3:
    print(sorted(cand))
else:
    vowel = []
    consonant = []
    for c in cand:
        if re.match('[aeiou]',c):
            vowel.append(c)
        else:
            consonant.append(c)

    L -= 3
    answer = []

    for l in range(L+1):
        m = 1+l #모음개수 (최소1개)
        n = 2+L-l
        for vow in combinations(vowel,m):
            for con in combinations(consonant,n):
                answer.append("".join(sorted(vow+con)))
    
    answer.sort()
    for ans in answer:
        print(ans)