#### 공백 없애야함
import sys
import re
input = sys.stdin.readline

# (100+1+|01)+
p =  re.compile('(100+1+|01)+')

for _ in range(int(input())): # 테스트케이스 T개
    if p.fullmatch(input().rstrip()):
        print("YES")
    else:
        print("NO")
