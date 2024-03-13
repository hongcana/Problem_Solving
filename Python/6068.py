# 마감 시간 기준 정렬 필요
#17 63 => 47시부터는 해야댐 => 31시에 시작
#32 95 => 63시부터는 해야댐  => 48시에 시작
#38 129 => 91시부터는 해야댐  => 91시에 시작
#11 104 => 93시부터는 해야댐 => 80시에 시작
#답 : 31

# 91시부터 찼음.. 104시를 돌 때 어떻게 처리하느냐... delay time += 13
# 80시부터 찼음.. 95시꺼 돌때... 

# 38 129 : start_time = 91
# 11 104 : start_time = min(91,104) - 11 = 80
# 32 95 : start_time = min(80,95) - 32 = 48
# 17 63 : start_time = min(48,63) - 17 = 31

# 5 20 : start_time = 20 - 5 = 15
# 1 16 : start_time = min(15,16) - 1 = 14
# 8 14 : start_time = min(14, 14) - 8 = 6
# 3 5 : start_time = min(6,5) - 3 = 2

N = int(input())
todo = [ list(map(int, input().split(" "))) for _ in range(N)]

# 정렬하기
todo.sort(key=lambda x : x[1], reverse=True)

# 계산 로직
cnt = 0
delay_time = 0
for start,end in todo:
    if cnt == 0: # 첫 턴일경우
        delay_time = end-start
    else:
        delay_time = min(delay_time, end) - start    
    cnt += 1

if delay_time < 0:
    print(-1)
else:
    print(delay_time)


# 밑에껀 틀리게 생각한 로직.
    
# chklist = [ 0 for i in range(max_S+1)]
# for start,end in todo:
#     for i in range(end-start, end):
#         chklist[i] += 1

# if sum(chklist) == len(chklist):
#     print(0)

# else:
#     break_point = 0
#     for i in chklist:
#         if i > 1:
#             break_point = 1
#             print(-1)
#             break
#     if break_point == 0:
#         for i in range(len(chklist)):
#             if chklist[i] == 1:
#                 print(i)
#                 break

# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 8 14
# 0 0 0 0 0 0 0 0 (0 0 0 0 0 0 0) 0 0 0 0 0 0
# 5 20
# 0 0 0 0 0 0 0 0 (0 0 0 0 0 0 0) 0 (0 0 0 0 0)
# 3 5
# 0 0 (0 0 0) 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 1 16
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
#4
