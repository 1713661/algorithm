import sys
import string
input = sys.stdin.readline

str = input()
l = []
for s in str:
    if s in string.ascii_uppercase:
        l.append(s)
print("".join(l))