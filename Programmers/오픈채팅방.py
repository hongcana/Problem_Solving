def solution(record):
    '''
    문자열과 구현? 에 가까운 2019 카카오 문제
    split(" ")[-1]을 이용하면, Leave 명령어에서 닉네임이 주어지지 않을때도 대비할 수 있음.
    '''
    user = {}
    stack = []
    for r in record:
        command, uid, nickname = r.split(" ")[0], r.split(" ")[1], r.split(" ")[-1]
        
        if command == "Enter":
            user[uid] = nickname
        elif command == "Change":
            user[uid] = nickname
        
    for r in record:
        command, uid = r.split(" ")[0], r.split(" ")[1]
        if command == "Enter":
            stack.append(f"{user[uid]}님이 들어왔습니다.")
        elif command == "Leave":
            stack.append(f"{user[uid]}님이 나갔습니다.")
    return stack

if __name__=="__main__":
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))