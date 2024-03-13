def solution(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    answer = []
    for i in range(0, len(str1)):
        answer = answer + str1[i:i+1] + str2[i:i+1]
        i = i + 1
    answer = "".join(answer) 
        
    return answer