import math

def solution(fees, records):
    '''
    그냥  simulation 문제
    문자열 파싱 + 해시 + 구현을 적절하게 할 수 있느냐? 를 물어봤던 문제인듯
    '''
    dict_in = {}
    result = {}
    
    basic_time = fees[0]
    basic_fee = fees[1]
    additional_time = fees[2]
    additional_fee = fees[3]
    
    for i in records:
        if i.split()[2] == 'IN':
            dict_in[i.split()[1]] = [int(i[0:2]), int(i[3:5])]
        elif i.split()[2] == 'OUT':
            result[i.split()[1]] = result.get(i.split()[1], 0) + (int(i[0:2]) - dict_in[i.split()[1]][0]) * 60 + (int(i[3:5]) - dict_in[i.split()[1]][1])
            dict_in[i.split()[1]] = -1 # 출차로 체크
            
    # 23:59분 출차 처리
    for d in dict_in:
        if dict_in[d] != -1:
            result[d] = result.get(d, 0) + (23 - dict_in[d][0]) * 60 + (59 - dict_in[d][1])
            
    result = sorted(result.items()) # 차량 번호가 작은 순서로 정렬
    fee = []
    for i in result:
        fee.append(i[1])

    for i in range(len(fee)):
        if fee[i] <= basic_time:
            fee[i] = basic_fee
        else:
            fee[i] = basic_fee + math.ceil(((fee[i] - basic_time) / additional_time)) * additional_fee # math ceil 이용하여 올림처리
    return fee