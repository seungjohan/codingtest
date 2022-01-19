def solution(s, op):
    answer = []

    for i in range(1, len(s)):
        s_left = s[0:i]
        s_right = s[i:len(s)]

        if op == "+":
            answer.append(int(s_left) + int(s_right))
        elif op == "-":
            answer.append(int(s_left) - int(s_right))
        elif op == "*":
            answer.append(int(s_left) * int(s_right))

    return answer
