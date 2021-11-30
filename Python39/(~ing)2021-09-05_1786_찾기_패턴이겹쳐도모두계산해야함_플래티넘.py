# 11분

import sys
import re
input = sys.stdin.readline

T = input().rstrip()
P = input().rstrip()
#result = re.finditer(P,T)
result = re.match(P,T).group()
print(result)
'''
cnt = 0
answer = ""
for r in result:
    answer += (str(r.start()+1)+" ")
    cnt += 1
print(str(cnt))
print(answer)
'''
### 패턴이 겹쳐도 모두 계산해야함
'''
ABABA
ABA

1
1
이 아니라

2
1 3
으로 출력해야함
'''
