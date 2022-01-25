def solution(operations):
    result = []
    for i in operations:
        text = i.split(' ')
        if text[0] == 'I':
            result.append(int(text[1]))
        else:
            if result:
                if text[1] == "1":
                    result.remove(max(result))
                if text[1] == "-1":
                    result.remove(min(result))
    return [max(result), min(result)]


print(solution(["I 7","I 5","I -5","D -1"]))