# 3분 24초
import re

if re.fullmatch('(100+1+|01)+',input().rstrip()):
    print("SUBMARINE")
else:
    print("NOISE")
