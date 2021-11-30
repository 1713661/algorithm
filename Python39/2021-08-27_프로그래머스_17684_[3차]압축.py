# 40분(밤에 졸릴 때 풀어서 오래걸렸던 것 같음)
# LZW 압축설명만 있으면 알고리즘 못짤것같음
def solution(msg):
    dict = [chr(i+65) for i in range(26)] #ord('A')=65
    length = len(msg)
    idx = 0
    str = msg[idx] # 첫글자부터 비교
    answer = []

    while idx<length:

        if str in dict:
            idx += 1 

            if idx==length: # 끝에 도달했으면 str
                answer.append(dict.index(str)+1) # str를 인덱스 answer에 추가 (1번부터 시작하므로 index+1)
                break

            str += msg[idx]

        else:
            answer.append(dict.index(str[:-1])+1) # 바로 직전 str의 인덱스 answer에 추가
            dict.append(str) # 사전에 등록
            str = msg[idx] # 초기화
    #print(dict)
    return answer

print(solution("KAKAO"))    # [11, 1, 27, 15]
print(solution("TOBEORNOTTOBEORTOBEORNOT")) # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print(solution("ABABABABABABABAB")) # [1, 2, 27, 29, 28, 31, 30]

