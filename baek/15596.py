# 정수 n개의 합 구하기

# Python 2, Python 3, PyPy, PyPy3: def solve(a: list) -> int
# a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
# 리턴값: a에 포함되어 있는 정수 n개의 합 (정수)



def solve(a):
    ans = 0

    for i in range(len(a)):
        ans += a[i]


    return print(ans)

a = [1,2,3,4,5,6,7,8,9, 10]

solve(a)