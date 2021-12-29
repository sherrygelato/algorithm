# https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3 

# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
# s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
# 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 
# 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

def solution(s):
    # 초기화
    answer = True
    p = 0
    y = 0

    # 문자열 소문자로 변경
    s = s.lower()
    
    # 인덱스로 p, y 갯수 구하기
    for i in s:
        if (i == 'p') :
            p += 1
        elif (i == 'y'):
            y += 1
    
    # 갯수 확인
    print(p)
    print(y)
    
    # False 조건
    if ( p != y):
        answer = False

    return answer