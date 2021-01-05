def cumsum_and_erase(a, erase=1):
    B = []
    pred = 0
    for i in a:
        pred += i
        if pred != erase:
            B.append(pred)
    return B


A = [5, 1, 4, 5, 14]
B = cumsum_and_erase(A, erase=10)
assert B == [5, 6, 15, 29], "Something is wrong! Please try again"
print(B)
