def process(sentences):
    result = []
    for line in sentences:
        result.append(' '.join(list(filter(lambda x: x.isalpha() == True, line.split()))))
    return result


x = ['1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100', '888']

res = process(x)
assert res == ['thousand devils', 'My name is', 'Room costs', ''], "Something is wrong! Please try again"
