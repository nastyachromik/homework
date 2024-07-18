def plusOne(digits):
    res = str(int(''.join([str(i) for i in digits]))+1)
    lst = []
    for i in res:
        lst.append(i)
    return lst
print(plusOne([1, 2, 4]))

