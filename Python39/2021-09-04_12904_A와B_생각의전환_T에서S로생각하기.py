## 생각의 전환 S->T가 아니라 T->S

import sys
input = sys.stdin.readline

S = input().rstrip()
T = list(input().rstrip())

while len(S) != len(T):
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()

### S가 1이 아닐 수 있잖아! 진짜 이런것도 생각못하면 안돼...
if S == "".join(T):
    print(1)
else:
    print(0)



    