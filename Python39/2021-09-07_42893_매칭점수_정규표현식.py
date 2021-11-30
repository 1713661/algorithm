# 한 웹페이지에 대해서 1.기본점수, 2.외부 링크 수, 3.링크점수, 그리고 4.매칭점수를 구할 수 있다.
# 1. 기본점수는 해당 웹페이지의 텍스트 중, 검색어가 등장하는 횟수이다. (대소문자 무시)
####### 텍스트는 body안에 있는 애들만 말하는건가? 노노 "HTML 내에" 라고 나와있음
# 검색어 word는 하나의 영어 단어로만 주어지며 
# 검색어는 단어 단위로 비교(단어는 알파벳을 제외한 다른 모든 문자로 구분한다.)하며, 단어와 '완전히' 일치하는 경우에만 기본 점수에 반영한다
# (fullmatch 쓰기)
# 예를들어 검색어가 "aba" 일 때, "abab abababa"는 단어 단위로 일치하는게 없으니, 기본 점수는 0점이 된다.
# 만약 검색어가 "aba" 라면, "aba@aba aba"는 단어 단위로 세개가 일치하므로, 기본 점수는 3점이다.

####### 텍스트만 뽑아내는법????????? -> 그냥 문자만 뽑기!!!!
# <body>안에 텍스트만 뽑아도 어차피 abababa 걸러내야하니까 re.findall이랑 re.fullmatch써야함
### '단어는 알파벳을 제외한 다른 모든 문자로 구분한다'는 조건 그대로 구현하면 됐었음!!!
# https://velog.io/@ckstn0778/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-42893%EB%B2%88-%EB%A7%A4%EC%B9%AD-%EC%A0%90%EC%88%98-X-1-Python

import re
def solution(word, pages):

    numOfPage = len(pages) 

    contents = ["" for _ in range(numOfPage)] # 자기 웹페이지 이름 저장하는 배열
    basicScores = [0 for _ in range(numOfPage)] # 1. 기본점수
    exlinks_list = [ [] for _ in range(numOfPage) ] # 2. 외부링크(url로 저장)
    linkScores = [0 for _ in range(numOfPage)] #  3. 링크점수
    matchScores = [0 for _ in range(numOfPage)] #  4. 매칭점수

    findContent = re.compile("<meta property=\"og:url\" content=\"https://[a-zA-Z0-9./]+(?=.*)",re.M)  
    findExlink = re.compile("<a href=\"https://[a-zA-Z0-9./]+",re.M) 

    for i in range(numOfPage):
        ####### 텍스트만 뽑아내는법????????? -> 그냥 문자만 뽑기!!!!
        for w in re.findall("[a-zA-Z]+", pages[i], re.M): 
            if re.fullmatch(word,w,re.I):
                basicScores[i] += 1
        contents[i] = findContent.search(pages[i]).group()[33:] # https://a.com
        exlinks_list[i]=[link[9:] for link in findExlink.findall(pages[i])] # ['https://b.com']
        # 2. 외부 링크 수는 해당 웹페이지에서 다른 외부 페이지로 연결된 링크의 개수이다.

    for i in range(len(contents)):  
        for idx in range(len(exlinks_list)):
            if contents[i] in exlinks_list[idx]:
                linkScores[i] += ( basicScores[idx] / len(exlinks_list[idx]) )
        matchScores[i]=basicScores[i]+linkScores[i]
    '''
    print(contents) #['https://a.com', 'https://b.com', 'https://c.com']
    print(exlinks_list) #[['https://b.com'], ['https://a.com', 'https://c.com'], ['https://a.com']]
    
    print("basicScores=",basicScores,"exlinks_list=",exlinks_list) # 1. 기본점수
    print("linkScores=",linkScores) #  3. 링크점수
    print("matchScores=",matchScores) #  4. 매칭점수
    '''
    score = max(matchScores)
    for answer in range(len(matchScores)): # 가장 작은 인덱스가 답
        if matchScores[answer]==score: 
            return answer

print("10000",solution("blind",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print("20000",solution("Muzi",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))