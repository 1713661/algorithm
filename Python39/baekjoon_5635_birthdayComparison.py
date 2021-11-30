import sys
input = sys.stdin.readline
INF = int(1e9)

youngestYear = 1989
youngestMonth = 0
youngestDay = 0
youngestStudent = "YOUNG"
oldestYear=2010
oldestMonth = 13
oldestDay = 32
oldestStudent = "OLD"

t = int(input())

print(youngestYear, youngestMonth, youngestDay, youngestStudent)
print(oldestYear, oldestMonth, oldestDay, oldestStudent)

while t:
    
    student, day, month, year = input().split()
    day = int(day)
    month = int(month)
    year = int(year)
    
    print(year, month, day, student)
    print(youngestYear, youngestMonth, youngestDay, youngestStudent)
    print(oldestYear, oldestMonth, oldestDay, oldestStudent)
    
    if (year>youngestYear) or (year==youngestYear and month>youngestMonth) or (year==youngestYear and month==youngestMonth and day>youngestDay) :
        #year>youngestYear and month>youngestMonth and day>youngestDay 이렇게 쓰면 안되지!!!!!!!!!
        print("im young")
        youngestYear = year
        youngestMonth = month 
        youngestDay = day
        youngestStudent = student
    
    if (year<oldestYear) or (year==oldestYear and month<oldestMonth) or (year==oldestYear and month==oldestMonth and day<oldestDay):
        print("I'm old")
        oldestYear = year
        oldestMonth = month
        oldestDay = day
        oldestStudent = student
        
    t -= 1
    print(t)
    
print("finalyoung:",youngestStudent)
print("finalold",oldestStudent)
