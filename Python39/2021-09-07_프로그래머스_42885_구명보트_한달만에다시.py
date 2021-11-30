# 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 
# 사람들을 구출할 수 없는 경우는 없습니다.

def solution(people, limit): 
    people.sort(reverse=True) # 무거운 순으로 정렬
  
    left = 0
    right = len(people)-1
    cnt = 0

    while left<=right:
        if people[left]+people[right]<=limit: 
            right -= 1
        cnt += 1
        left += 1

    return cnt 

'''
def solution(people, limit): # 뭐얏 이코드도 통과했어..
    people.sort(reverse=True) # 무거운 순으로 정렬
  
    left = 0
    right = len(people)-1
    cnt = 0

    while left<=right:
        if people[left]+people[right]<=limit: 
            cnt += 1
            left += 1
            right -= 1
        else: # people[left]는 혼자 타야함
            cnt += 1
            left += 1

    return cnt 
'''

print(solution( [70, 50, 80, 50], 100)) # 3
print(solution( [70, 80, 50], 100)) # 3
# print(solution( [50, 50, 50, 50, 50, 70], 100))
# print(solution( [40, 40, 40, 60, 60, 60], 100))

#print(solution([101,101,101,80,40,40],100))
# 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 
# 사람들을 구출할 수 없는 경우는 없습니다. (101올 수 없음)

print(solution([99,99,99,80,80,40],100))