def solution(a, b):
    answer = 0
    a1 = str(a)
    a2 = str(b)
    answer = max(int(a1 + a2), 2 * int(a1) * int(a2))
    return answer