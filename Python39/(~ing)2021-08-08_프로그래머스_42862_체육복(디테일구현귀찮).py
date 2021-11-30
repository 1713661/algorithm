# 15분 
# 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 
# 'lost, reserve 둘 다 해당하는 학생있는경우' 고려해야함
def solution(n, lost, reserve):
    answer = n-len(lost)
    for l in lost:
        if l+1 in reserve and l+1 not in lost:
            print(l+1, "rent to",l)
            reserve.remove(l+1)
            answer += 1
        elif l-1 in reserve and l-1 not in lost:
            print(l-1, "rent to",l)
            reserve.remove(l-1)
            answer += 1
    return answer

#print( solution(5, [2, 4], [1, 3, 5]) )
print (solution(5, [2, 4], [3]) )
#print( solution(3, [3], [1]) )