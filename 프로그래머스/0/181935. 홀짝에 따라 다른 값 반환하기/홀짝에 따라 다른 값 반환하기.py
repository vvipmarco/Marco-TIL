def solution(n):
    answer = 0
    if n % 2 == 1:
        for i in range(1, n+1):
            if i % 2 == 1:
                answer = answer + i
            else:
                continue
            print(answer)
    else:
        for i in range(1, n+1):
            if i % 2 == 0:
                answer = answer + i**2
            else:
                continue
            print(answer)
    return answer