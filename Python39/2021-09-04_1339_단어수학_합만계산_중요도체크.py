# 모든 단어에 포함되어 있는 알파벳은 최대 10개이고, 
# 수의 최대 길이는 8이다.
# 15분 글자수별로 s에 넣고 각각의 s[n] combinations돌려서 dict에 저장한다음 max()출력하려고 했음
######### 합만 구하면 되기 때문에 내가 생각한 방법은 비효율적! 중요도체크
# +15분 아놔 d.get[word[i]]라고 써서 10분 낭비
# 20분
N = int(input()) #1<=N<=10
d = dict()

for _ in range(N):
    word = input().rstrip()
    l = len(word)
    for i in range(l):
        if word[i] not in d:
            d[word[i]] = pow(10,l-1-i)
        else:
            d[word[i]] = d.get(word[i])+pow(10,l-1-i)

d = sorted(d.items(), key=lambda x:x[1],reverse=True)
# [('A', 10000), ('C', 1010), ('G', 100), ('D', 100), ('E', 10), ('F', 1), ('B', 1)]
cnt = 9
answer = 0
for _,value in d:
    answer += cnt*value
    cnt -= 1
print(answer)


'''
N = int(input()) #1<=N<=10
s = [[] for _ in range(8+1)] #s[n]=[n글자인단어]리스트 n은 최대
for _ in range(N):
    word = input().rstrip()
    s[len(word)].append(word)
'''
'''
N = int(input()) #1<=N<=10
s = []
for _ in range(N):
    s.append(input().rstrip())
s = sorted(s,key=len,reverse=True)
print(s)
'''