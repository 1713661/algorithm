l = []
d = {}
idx = []

for i in range(8):
    score = int(input())
    l.append(score)
    d[score] =  i+1
    
l.sort(reverse=True)

print(l[0]+l[1]+l[2]+l[3]+l[4])

for i in range(5):
    idx.append(d[l[i]])
idx.sort()

for i in idx:
    print(i, end=' ')



'''
list = []
dict = {}
sum = 0

for i in range(8):
    score = int(input())
    list.append(score)
    dict[score] = i

list.sort()
sum = list[4]+list[5]+list[6]+list[7]+list[8]
print(sum)
print(dict[list[4]], dict[list[5]], dict[list[6]], dict[list[7]], dict[list[8]])
'''

"""
import operator

d = dict() 

for i in range(8):
    score = int(input())
    d[i] = score
'''
for key,value in d.items() :
    print(key,value)
'''

ds = sorted(d.items(), key=operator.itemgetter(0), reverse=True)
print(ds[0]+ds[1]+ds[2]+ds[3]+ds[4])
print(ds[0:4].keys(), end=' ')
"""




