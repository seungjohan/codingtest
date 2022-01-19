def solution(n, horizontal):

    answer = [[0]*n for i in range(n)]

    seconds = 0

    x = 0
    y = 0

    for i in range(1, n):
        if horizontal % 2 != 0:

            x += 1
            seconds += 1

            answer[y][x] = seconds

            for j in range(i):

                x -= 1
                y += 1

                seconds += 2

                answer[y][x] = seconds

        else:

            y += 1
            seconds += 1

            answer[y][x] = seconds

            for j in range(i):

                x += 1
                y -= 1

                seconds += 2

                answer[y][x] = seconds

        horizontal += 1 

    for i in range(n-2, 0, -1):
        if horizontal % 2 == 0:

            x += 1
            seconds += 1

            answer[y][x] = seconds

            for j in range(i, 0, -1):

                x += 1
                y -= 1

                seconds += 2

                answer[y][x] = seconds

        else:

            y += 1
            seconds += 1

            answer[y][x] = seconds

            for j in range(i, 0, -1):

                x -= 1
                y += 1

                seconds += 2

                answer[y][x] = seconds

        horizontal += 1 

        answer[n-1][n-1] = seconds + 1
               
    return answer