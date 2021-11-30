# -*- coding: utf-8 -*-

def solution(cacheSize, cities):
    if cacheSize==0:
        return len(cities)*5
    cities = [city.lower() for city in cities]
    cache = {}
    cache_tuples = []
    answer = 0
    l = len(cities)
    for i in range(l):
        if cities[i] not in cache:
            if len(cache)>=cacheSize: 
                del cache[cache_tuples[0][0]]
            answer += 5
        else:
            answer += 1
        cache[cities[i]] = i
        cache_tuples = sorted(cache.items(), key=lambda x:x[1]) # Í∞??û• ?ò§?ûò?êú?àú?úºÎ°? ?†ï?†¨
    
        #print("cache=",cache)
        #print("cache_tuples=",cache_tuples)
        #print("answer=",answer)
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) #
# 50

print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])) #
# 21

print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) #
# 60
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) #
# 52
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])) #
# 16
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) #
# 25
