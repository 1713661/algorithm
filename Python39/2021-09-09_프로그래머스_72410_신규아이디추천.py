# 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때, 
# 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발

# 3자 이상 15자 이하여야 합니다.
# 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 
# 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.




# 7단계
# 24분 일단 썼는데 완전 다르게 나옴..짜증
# 36분 88.5점 망했다.. 왜이렇게 못하지??? 숫자 0안붙여줬기때문!!! 급하게 풀면 안된다!!!!!
############## sub은 정규표현식안됨???? 

# 9분
import re
def solution(new_id):
    step1 = new_id.lower()
    step2 = re.sub("[^a-z0-9-_.]",'',step1) ######-_.말고 _-.로쓰면 bad character로 인식함. - 가운데에만 안쓰면 괜찮은듯
    step3 = re.sub("[.]{2,}",".",step2)
    step4 = step3.strip('.')
    step5 = step4[:]
    if step5=='':
        step5 += 'a'
    step6 = step5[:15]
    if step6[-1]=='.':
        step6 = step6[:-1]
    step7 = step6[:]
    while len(step7)<=2:
        step7 += step6[-1]

    return step7

'''
import re
import string
def solution(new_id):

    #step1
    new_id = new_id.lower()
    
    #step2
    step2 = ''
    filter = string.ascii_lowercase+"0123456789-_." ######### 숫자0이빠졌잖아....실전에서 이러면 안되는데...
    for s in new_id:
        if s in filter:
            step2 += s

    #print("afterstep2=",step2)
    p2 = re.compile('[.]{2,}') ##### 그룹화해야하나?
    step3 = p2.sub('.',step2)
    print("afterstep3=",step3)
    step4 = step3.strip('.')
    print("afterstep4=",step4)
    step5 = step4[:]
    if len(step5)==0:
        step5 +='a'
    #print("afterstep5=",step5)
    step6 = step5[:]
    if len(step6)>=16:
        step6 = step6[:15]
        if step6[-1]=='.':
            step6 = step6[:-1]
    #print("afterstep6=",step6)
    step7 = step6[:]
    if len(step7)<=2:
        last = step7[-1]
        while len(step7)<=2:
            step7 += last
    
    return step7
''' 

print(solution( "...!@BaT#*..y.abcdefghijklm" )) # "bat.y.abcdefghi"
print(solution( "z-+.^." )) # "z--"
print(solution( "=.=" )) # "aaa"
print(solution( "123_.def" )) # "123_.def"
print(solution( "abcdefghijklmn.p" )) # "abcdefghijklmn"
