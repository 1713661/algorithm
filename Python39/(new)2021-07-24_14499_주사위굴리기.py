# 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 
# 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 

# 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 
# 칸에 쓰여 있는 수는 0이 된다.

# 10분 피곤해서 못하겠음..집에가자
import sys
input = sys.stdin.readline

N,M, x,y, K = map(int,input().split()) 
#세로,가로, 주사위를 놓은 곳의 좌표 x y,명령의 개수 K

board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

# 주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다. 

# 마지막 줄에는 이동하는 명령이 순서대로 주어진다. 
# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.
cmds = list(map(int,input().split()))

for cmd in cmds:
    if cmd=='1':
        print("동")
    elif cmd=='2':
        print("서")
    elif cmd=='3':
        print("북")
    elif cmd=='4':
        print("남")