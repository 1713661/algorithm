############ 가장 오래된 시간 기록할 필요없음
############# 그냥 제일 오래된 애를 내보내면 되니까..........
########### 난 왜이렇게 어렵게 생각할까.......
##### deque maxlen 속성 알아두기!!!!!!!!!!!

def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s) 
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time