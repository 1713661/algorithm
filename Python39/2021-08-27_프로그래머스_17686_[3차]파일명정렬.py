# 8/26(목)
# 12분 졸려

# 8/27(금)
# 0분
# 17분 전처리 완료
# 32분 tail이 없는 경우 때문에 배열에 넣는 작업은 for문 나와서 해야함(이것땜에 시간낭비)
# 50분

def solution(files):
    # 전처리
    splitFiles = []
    for file in files: # file="img12.png"
        
        length = len(file)
        HEAD,NUMBER,TAIL = "","",""
        for i in range(length):
            if file[i].isdigit(): #########isdigit()은 '문자'가 숫자면 True반환
                if HEAD == "":   # 처음으로 숫자가 나오면
                    HEAD = file[:i]
                    NUMBER = file[i]
                else:
                    NUMBER += file[i]
                
            else: # 숫자가 아니면
                if len(HEAD)>0: # NUMBER까지 정해진 상태
                    TAIL = file[i:]
                    break

        splitFiles.append([HEAD,NUMBER,TAIL])

    # 정렬
    splitFiles = sorted(splitFiles, key=lambda x: (str.lower(x[0]),int(x[1]))) ############# 대소문자 구분없이
    newFiles = []
    for file in splitFiles:
        newFiles.append("".join(file))
    return newFiles

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
#  ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
# ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]