def solution(cap, n, deliveries, pickups):
    '''
    그리디 + 스택으로 푸는 문제
    Level 2라고 하는데, 도중에 분기 처리 해주는 것때문에 체감 난이도는 살짝 더 높았음
    아직 까지 스택으로 문제를 해결하는 것에는 익숙치 않은듯..

    최대 cap을 넘어갔을 때 배달/수거에서 그만큼 빼주는거 생각하는게 힘들었음
    (deliveries[-1] -= d_cap)
    '''
    answer = 0
    while deliveries and not deliveries[-1]:
        deliveries.pop()
    while pickups and not pickups[-1]:
        pickups.pop()

    while pickups or deliveries:
        answer += max(len(pickups), len(deliveries)) * 2

        d_cap = cap
        p_cap = cap

        while deliveries:
            if deliveries[-1] <= d_cap:
                d_cap -= deliveries.pop()
            else:
                deliveries[-1] -= d_cap
                break

        while pickups:
            if pickups[-1] <= p_cap:
                p_cap -= pickups.pop()
            else:
                pickups[-1] -= p_cap
                break
    return answer
