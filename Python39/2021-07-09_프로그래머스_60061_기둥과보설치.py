##1시간 13분 제한시간 50분이라는데 조건이 너무 많아서 그거 확인하느라 시간 많이 쓴 느낌
#   wall[x][y+1].append(0)
#   IndexError: list index out of range 
#   2차원 배열이 아니라 3차원 배열이야 바보야!!!!!!
#   그나마 다행인 건 문제5번 정답률 1.9%라는거..
def solution(n, build_frame):
    wall = [ [[] for _ in range(n+1)]  for _ in range(n+1)] 
    print(wall)
    answer = []
    for frame in build_frame:
        x,y,a,b = frame
        print(x,y,a,b)
        if (a==0 and y>=n) or (a==1 and x>=n): 
            continue
        if b==1: #구조물 설치
            print("<설치>")
            if a==0: #기둥 설치
                print("기둥 설치")
                if y==0: 
                    print("기둥은 바닥 위에 있거나")
                    wall[x][y+1].append(0) #   IndexError: list index out of range
                elif 1 in wall[x][y]:
                    print("보의 한쪽 끝 부분 위에 있거나")
                    wall[x][y+1].append(0)
                    wall[x][y].remove(1)
                elif 0 in wall[x][y]:
                    print("다른 기둥 위에 있어야 합니다.")
                    wall[x][y+1].append(0)
                    wall[x][y].remove(0)
                else:
                    print("기둥 설치 불가능")

            elif a==1 and y!=0:      #보 설치              
                print("보 설치(바닥에 보를 설치 하는 경우는 없습니다.)")
                if 0 in wall[x][y]:
                    print("보는 한쪽 끝 부분이 기둥 위에 있거나(왼쪽)")
                    wall[x+1][y].append(1) 
                    wall[x][y].remove(0)
                elif 0 in wall[x+1][y]: #위랑 이거 둘 다 만족하는 경우는 한번만 수행해야하기 때문에(중복되면 안되기 때문에) elif써야함!!!
                    print("보는 한쪽 끝 부분이 기둥 위에 있거나(오른쪽)")
                    wall[x][y].append(1) 
                    wall[x+1][y].remove(0)
                elif 1 in wall[x][y] and 1 in wall[x+1][y]:
                    print("또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.")
                    wall[x][y].remove(1)
                    wall[x+1][y].remove(1)
                else:
                    print("기둥 설치 불가능")
            answer.append([x,y,a])

        elif b==0: #구조물 삭제
            print("<삭제>")
            for ans in answer:
                print("이어서 작성해야함")
                
        
    
    answer.sort()
    return answer

print('answer=',solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
# 기둥은 보의 한쪽 끝부분
# 만약 (4, 2)에서 오른쪽으로 보를 먼저 설치하지 않고, (3, 2)에서 오른쪽으로 보를 설치하려 한다면 2번 규칙에 맞지 않으므로 설치가 되지 않습니다. 
# 기둥과 보를 삭제하는 기능도 있는데 기둥과 보를 삭제한 후에 남은 기둥과 보들 또한 위 규칙을 만족해야 합니다. 만약, 작업을 수행한 결과가 조건을 만족하지 않는다면 해당 작업은 무시됩니다.

# 벽면의 크기 n, 기둥과 보를 설치하거나 삭제하는 작업이 순서대로 담긴 2차원 배열 build_frame이 매개변수로 주어질 때, 모든 명령어를 수행한 후 구조물의 상태를 return 하도록 solution 함수를 완성해주세요.

# build_frame의 원소는 [x, y, a, b]형태입니다.
#x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
#a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
#b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.
#벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다.
###바닥에 보를 설치 하는 경우는 없습니다.

## [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0]#기둥삭제#,[1,1,1,0]#이 보를 삭제하면 규칙에 어긋나므로 삭제되지 않음#,[2,2,0,1]#기둥설치안됨#]