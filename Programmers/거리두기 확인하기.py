def solution(places):
    answer = []
    
    for p in places:
        p_locate = []
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    p_locate.append([i,j])
        
        if len(p_locate) == 0:
            answer.append(1)
            continue
        
        break_point = 0
        for i in range(len(p_locate)-1):
            for j in range(i+1, len(p_locate)):
                r = p_locate[i]
                c = p_locate[j]
                r1, c1, r2, c2 = r[0], r[1], c[0], c[1]
                dist = (abs(r1 - r2)) + (abs(c1 - c2))
                
                if dist == 1:
                    print('changed.')
                    break_point = 1
                    break
                    
                if dist == 2:
                    
                    # 행이 같을 때
                    if (r1 == r2) and p[r1][(c2+c1)//2] != 'X':
                        break_point = 1
                    # 열이 같을 때
                    elif (c1 == c2) and p[(r1+r2)//2][c1] != 'X':
                        break_point = 1
                    
                    # 행과 열이 모두 다를 때
                    elif (r1 != r2) and (c1 != c2):
                        # 2번째 지점의 컬럼이 1번째 지점보다 뒤에 있을 때
                        if (c1 < c2) and p[r1][c2] != 'X' or p[r2][c1] != 'X':
                            
                            break_point = 1
                        # 앞에 있을 때
                        elif (c1 > c2) and p[r1][c2] != 'X' or p[r2][c1] != 'X':
                            break_point = 1
                            
            if break_point == 1:
                break

        if break_point == 1:
            answer.append(0)
        else:
            answer.append(1)
    return answer

# 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2|

# 걍 완전 탐색인가

# 첫 번째 대기실 예시

# P가 없으면 그냥 1임 끝.

# P의 위치를 집는다 = (0, 0), (0, 4), (2,1), (2,3) (4,0), (4,4)
# 2중 포문 돌려
# (0,0) (0,4) 비교 = 4임 -> 맨해튼 아님.
# (0,0) (2,1) 비교 = 3임 -> 맨해튼 아님.
# (2,1) (2,3) 비교 = 2임 -> 어 벽있나? 그 사이인 (2,2)를 뒤져봄. -?> 벽있음 -> 맨해튼 아님.
# (4,3) (4,4) 비교 = 1임 -> 벽의 유무와 상관 없이 맨해튼임
# (0,0), (1,1) 비교 = (0,1)과 (1,0)에 벽이 있으니 맨해튼 아님.
# (0,3), (1,2) 비교 = 2임 -> 어 벽있나? 그 사이인 (0,2), (1,3)을 뒤져봄 -> 둘다 X면 -> 맨해튼 아님
