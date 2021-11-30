from collections import deque

# case1) deque에서 바로 초기화시키기
snake = deque([(1,1)]) #리스트 자료구조는 아니지만, 리스트로 초기화시켜야함!! heapq도 마찬가지!
snake.append((2,2))
snake.append((3,3))
x,y = snake.popleft()

print(x,y)   # 1 1
print(snake) # deque([(2, 2), (3, 3)])



# case2) deque에서 초기화시키지 않기
snake = deque()
snake.append((2,2))
snake.append((3,3))
x,y = snake.popleft()

print(x,y)   # 2 2
print(snake) # deque([(3, 3)])