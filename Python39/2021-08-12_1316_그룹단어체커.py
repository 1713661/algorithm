# 24분 (알고리즘 처음에 제대로 생각못하니까 시간 오래걸리잖아)
import sys
input = sys.stdin.readline
# 단어는 알파벳 소문자로만 되어있고 중복되지 않으며

cnt = 0
for _ in range(int(input())): # N

    check = [False]*26
    s = input().rstrip() #############
    isGroup = True

    check[ord(s[0])-ord('a')]=True
    prev = s[0]
    
    for i in range(1,len(s)):
        if s[i] == prev: 
            continue
        if check[ord(s[i])-ord('a')]: #글자가 떨어져 나타나면
            isGroup = False
            break
        check[ord(s[i])-ord('a')]=True
        prev = s[i]

    if isGroup:
        cnt += 1
print(cnt)



# 파이썬 라이브러리 적극 활용할 수 있어야
# 와우정말참신한풀이
# 실전에서는 이런 풀이 절대 생각못할듯(문제풀때 필요한 알고리즘을 아는것뿐만아니라 '그 알고리즘을 효율적으로 풀수있는방법'도 알아야하기때문)
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find): #괄호안씀
    # ['h','a','p','p','y'] key==['0','1','2','2','4'] key를 기준으로 '요소'(key값아님!!)를 정렬
    # aabbbccb ['a','a','b','b','b','c','c','b']  key==['0','0','1','1','1','5','5','1']   '1'이 앞으로 가니까!!!
        result += 1
print(result)


'''
print(sorted("abcabc", key="abcabc".find)) #key 매개변수: 각 리스트 '요소'에 대해 호출할 함수를 지정(함수이름만씀) 이런거 헷갈리면 안돼..
print(sorted("cbacba", key="cbacba".find))
'''



