# 10진수에서 다른 진법으로 변환은 아쉽게도 직접 코드를 작성해야 합니다.
# 15분 알고리즘 구상 완료(함수는 따로 없다고 함. 내가 직접 구현해야함)
# 39분
change = {
    10:"A",
    11:"B",
    12:"C",
    13:"D",
    14:"E",
    15:"F"
}
def convert(num,base):
    global change
    remains = []
    if num==0: return [0]
    while num>0:
        remains.append(num%base if num%base<10 else change[num%base])
        num //= base
    return remains[::-1]

def solution(n, t, m, p): # 진법=n, 미리구할숫자갯수=t, 참가인원=m, 튜브의순서=p
    numArr = []
    for i in range(m*t):
        numArr.extend(convert(i,n)) # 진법에 맞게 숫자 변환하고 numArr에 저장
  
    answer = ""
    for i in range(p-1,m*t,m):
        answer += str(numArr[i])

    return answer

print(solution(2,4,2,1))    # "0111"
print(solution(16,16,2,1))  # "02468ACE11111111"
print(solution(16,16,2,2))  # "13579BDF01234567"