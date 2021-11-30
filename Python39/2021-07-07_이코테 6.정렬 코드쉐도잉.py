# 선택 정렬
def selectionSort():
    array = [7,5,9,0,3,1,6,2,4,8]
    
    for i in range(len(array)):
        min = i
        for j in range(i+1,len(array)):
            if array[j]<array[min]: # array[i]랑 비교하는 거 아님!!!
                min=j
        array[i],array[min]=array[min],array[i]
    print(array)

# 삽입 정렬
def insertionSort():
    array = [7,5,9,0,3,1,6,2,4,8]
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if array[j]<array[j-1]:
                array[j],array[j-1] = array[j-1],array[j]
            else:   # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤(더이상 스와핑할 필요가 없으니까!)
                break
    print(array)

# 퀵 정렬
# arrleft가 arrpivot보다 큰 경우, arrright가 arrpivot보다 작은 경우 arrleft arrright 서로 바꿔줌
# 각각 작은 경우, 큰 경우는 이미 맞는 자리에 있는것이므로 그냥 넘어감 
# 부등호 등호 잘 써야함!!!!!! 
def quickSort():
    array = [7,5,9,0,3,1,6,2,4,8]
    divideAndConquer(array,0,len(array)-1)
    print(array)
    return

def divideAndConquer(array,start,end):
    if start>=end:  # 재귀함수 종료조건 빼먹으면 안돼!!!!! 안그러면 프로그램 안 끝난다~~~~
        return
    pivot = start
    left = start+1
    right = end

    while left<=right:
        while left<=end and array[left]<=array[pivot]: ####left<=end 조건 빼먹으면 안돼!!!!! 제발~~~~~
            left += 1
        while right>start and array[right]>=array[pivot]:
            right -= 1
        if left>right: #4
            array[pivot],array[right] = array[right],array[pivot]
        else:
             array[left],array[right] = array[right],array[left]
        
        #right을 기준으로 쪼개야 함!!!! (생각을 해 생각을)
    divideAndConquer(array,start,right-1)
    divideAndConquer(array,right+1,end)

def radixSort():
    array = [7,5,9,0,3,1,6,2,4,8,0,5,2]
    count = [0]*(max(array)+1)
    array_sorted = []

    for i in range(len(array)):
        count[array[i]] += 1
    
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')

selectionSort() 
insertionSort()
quickSort()  
radixSort()
          