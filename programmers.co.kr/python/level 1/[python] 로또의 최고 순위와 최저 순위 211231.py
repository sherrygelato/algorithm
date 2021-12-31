# https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3 

def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero = lottos.count(0)
    
    # lottos와 win_nums 중 맞힌 갯수
    for i in lottos:
        if i in win_nums:
            cnt += 1
    
    # 5등  + 1개 번호 + 0개 번호 => 7가지
    # 최소
    answer.append(7-(cnt+zero))
    # 최대
    answer.append(7-(cnt))
    
    print(answer)
    
    # 최소, 최고 순위 메기기
    # 7이 있을 수 있음
    # 모든 번호를 모르는 경우
    if zero == 6:  
        answer = [1, 6]
    # 모든 번호가 있고, 전부 맞지 않은 경우
    elif zero == 0 and cnt == 0: 
        answer = [6, 6]
    
    print(answer)
    
    return answer