def solution(my_string, overwrite_string, s):
    my_string = list(my_string)
    overwrite_string = list(overwrite_string)
    answer = overwrite_string
    answer = my_string[:s] + answer + my_string[s+len(overwrite_string):]
    answer = "".join(answer)
    return answer