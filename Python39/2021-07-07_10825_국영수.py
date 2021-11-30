import sys
input = sys.stdin.readline

students=[]
for _ in range(int(input())):
    students.append(input().split())
print(students)
students.sort(key=lambda x: ( -int(x[1]),int(x[2]),-int(x[3]),x[0] ))
# 국어(감소), 영어(증가), 수학(감소), 이름사전순증가 

for student in students:
    print(student[0])
