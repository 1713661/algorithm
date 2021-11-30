# 15분

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        item1 = str(bin(arr1[i]))[2:].zfill(n) # 01001 rjust함수도 있음!!!
        item2 = str(bin(arr2[i]))[2:].zfill(n) # 11110
        newitem = ""
        for j in range(n):
            newitem += "#" if int(item1[j]) | int(item2[j])==1 else " "
        answer.append(newitem)
       

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# ["#####","# # #", "### #", "# ##", "#####"]

## 파이썬 알고리즘 인터뷰

'''
from typing import List


def solution(n: int, arr1: List[int], arr2: List[int]) -> List[str]:
    maps = []
    for i in range(n):
        # OR 연산 후 이진수 변환
        maps.append(
            bin(arr1[i] | arr2[i])[2:]
                .zfill(n)
                .replace('1', '#') ## replace함수를 왜 생각을 못했을까
                .replace('0', ' ')
        )
    return maps
'''