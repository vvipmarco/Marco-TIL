def solution(a, b):
    answer = 0
    answer1 = str(a) + str(b)
    answer2 = str(b) + str(a)
    if int(answer1) >= int(answer2):
        answer = answer1
    else:
        answer = answer2
    answer = int(answer)
    return answer