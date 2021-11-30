# 위 목록에 없는 알파벳은 한 글자씩 센다.
# 5분

import sys
input = sys.stdin.readline

s = input().rstrip()

alphas = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for alpha in alphas:
    s = s.replace(alpha,"1")

print(len(s))