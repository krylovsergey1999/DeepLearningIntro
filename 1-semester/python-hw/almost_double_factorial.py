def almost_double_factorial(n):
    res = 1
    for i in range(3, n + 1, 2):
        res *= i
    return res


print(almost_double_factorial(5))
