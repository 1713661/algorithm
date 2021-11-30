# 8분
import sys
import re
input = sys.stdin.readline

S = ''.join(re.findall("[a-zA-Z]",input().rstrip())) #S = input().rstrip() # 알파벳 소문자, 대문자, 숫자로 이루어진 문자열 S (1 ≤ |S| ≤ 200,000) 
K = input().rstrip() # 성민이가 찾고자 하는 알파벳 소문자, 대문자로만 이루어진 키워드 문자열 K (1 ≤ |K| ≤ 200,000)

if re.findall(K,S):
    print(1)
else:
    print(0)
